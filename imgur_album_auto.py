#!/usr/bin/env python

import os
import sys
import json
import argparse
import urllib.request
from multiprocessing.dummy import Pool as ThreadPool


class Options:

	# Required
	client_id = ''

	# Download specific options
	download_threads = 50
	default_dir = os.getcwd()

	# Runtime Options
	gather = False
	custom_name = None

	# Colors
	CYAN = '\033[96m'
	RED = '\033[91m'
	ENDC = '\033[0m'


class Album:

	def __init__(self, album_link, base_download_directory):
		self.album_link = album_link
		self.base_download_directory = base_download_directory
		self.download_path = None
		self.download_list = []
		self.errorlist = []

	def get_links(self):
		album_id = self.album_link.strip('/').rsplit('/', 1)[1]

		# Generate GET request for the imgur API
		url = 'https://api.imgur.com/3/album/{0}'.format(album_id)
		req = urllib.request.Request(url)
		req.add_header('authorization', 'Client-ID 246653cb7cc0b13')
		response = urllib.request.urlopen(req)

		response = json.loads(response.readlines()[0].decode('utf-8'))

		# Get title and image links
		title = response['data']['title']
		if not title:
			title = album_id

		for i in response['data']['images']:
			self.download_list.append(i['link'])

		# Download to path defined by os and the title we just derived
		self.download_path = self.base_download_directory + os.sep + title
		if not os.path.exists(self.download_path):
			os.makedirs(self.download_path)

		print('Downloading to ' + Options.CYAN + self.download_path + Options.ENDC)

		self.initiate_threads()

	def progressbar(self):
		files = os.listdir(self.download_path)
		completed = []
		for i in files:
			if not i.endswith('.pyImgur'):
				completed.append(i)
		current_val = len(completed)

		# The 50 below is the length of the progressbar.
		# The value displayed in the bar proper is a multiple of 50.
		# The percentage value is independent of the length of the bar.
		sys.stdout.write('\r')
		sys.stdout.write("[%-50s] %d%%" % ('=' * int(current_val / len(self.download_list) * 50), int(current_val / len(self.download_list) * 100)))
		sys.stdout.flush()

	def download_file(self, image_link):
		image_name = image_link.rsplit('/', 1)[1]
		# Temporary files are saved to a .pyImgur extension
		# This could be extended to resuming downloads of incomplete files
		image_tempname = image_name.split('.')[0] + '.pyImgur'

		image_order = self.download_list.index(image_link) + 1
		image_order = str(image_order).zfill(3)

		temp_path = self.download_path + os.sep + image_order + ' - ' + image_tempname
		final_path = self.download_path + os.sep + image_order + ' - ' + image_name

		if not os.path.exists(final_path):
			try:
				urllib.request.urlretrieve(image_link, temp_path)
				os.rename(temp_path, final_path)
			except ConnectionResetError:
				self.errorlist.append(image_name)
				os.remove(temp_path)

			self.progressbar()

	def initiate_threads(self):
		# Black magic fuckery
		try:
			pool = ThreadPool(Options.download_threads)
			pool.map(self.download_file, self.download_list)
			pool.close()
			pool.join()
		except KeyboardInterrupt:
			pass

		if self.errorlist:
			print('\nDone with errors: ' + ', '.join(self.errorlist))


def generate_downloads(gathering_dir, list_of_albums):
	if not os.path.exists(Options.default_dir) or Options.default_dir == '':
		base_download_directory = os.getcwd()
	else:
		base_download_directory = Options.default_dir

	if Options.gather is True:
		base_download_directory = base_download_directory + os.sep + gathering_dir

	download_classes = {}
	for count, i in enumerate(list_of_albums):
		download_classes[count] = Album(i, base_download_directory)
		download_classes[count].get_links()
		print()


def main():

	parser = argparse.ArgumentParser(description='Download imgur albums from from your terminal. IT\'S THE FUTURE.')
	parser.add_argument('album_url', type=str, nargs='+', help='Album URL')
	parser.add_argument('-n', type=str, nargs=1, help='Name of album', metavar='custom_name')
	parser.add_argument('--gather', type=str, nargs=1, help='Gather links into one directory', metavar='dirname')
	args = parser.parse_args() #get value from args

	

	if args.album_url:
		if args.gather:
			Options.gather = True
			generate_downloads(args.gather[0], args.album_url)
		else:
			generate_downloads(None, args.album_url)


if __name__ == '__main__':
	main()