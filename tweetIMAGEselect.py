import os
import re
import json
import requests
import random
import time
from six.moves import queue as Queue
from threading import Thread
from tkinter import filedialog
from tkinter import Tk



root = Tk()
root.filename =  filedialog.askdirectory()
print (root.filename)
 
THREADS_NUM = 10      #多线程数量 
PROXIES={'https': 'https://127.0.0.1:55555','http': 'http://127.0.0.1:55555'}
DEFSAVEDIR=root.filename    #默认保存目录
HEADERS_LIST = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
    'Mozilla/5.0 (compatible, MSIE 11, Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; rv:2.2) Gecko/20110201',
    'Opera/9.80 (X11; Linux i686; Ubuntu/14.10) Presto/2.12.388 Version/12.16',
    'Mozilla/5.0 (Windows NT 5.2; RW; rv:7.0a1) Gecko/20091211 SeaMonkey/9.23a1pre'
]
HEADERS = {'User-Agent': random.choice(HEADERS_LIST)}   
 
class DownloadWorker(Thread):
    def __init__(self, queue, headers):
        Thread.__init__(self)
        self.queue = queue
        self.headers = headers
        #self.proxies = proxies   
 
    def run(self):
        while True:
            
            picurl, savepath = self.queue.get()
            self.downloadfile(picurl, savepath)
            self.queue.task_done()
 
    def downloadfile(self, picurl, savepath):       
        with requests.get(url = picurl, headers = self.headers) as respon:
            with open(savepath, 'wb') as f:            
                print('downloading-->:'+picurl)                
                f.write(respon.content)        
 
class TwitterPicScraper(object):
    #构造函数初始化
    def __init__(self, user, headers):
        self.user = user        
        self.headers = headers
        
        self.userdir = os.path.join(DEFSAVEDIR, user)
        self.queue = Queue.Queue()
        self.scheduling()
 
    def scheduling(self):        
        for i in range(THREADS_NUM):
            worker = DownloadWorker(queue = self.queue, headers = self.headers)            
            worker.daemon = True
            worker.start()        
        self._getpic_list()
        #等待队列为空再返回主线程
        self.queue.join()
        print("用户[ %s ]的图片下载完成" %self.user)
    #获取上次保存于文件中的下载位置
    def getpos(self):     
        pospath =  os.path.join(self.userdir, 'pos.txt')
        with open(pospath, 'r') as f:
            savedpos ,savedpicname = f.read().splitlines(False)        
        return savedpos, savedpicname
    #设置最新下载位置
    def setpos(self, savedpos, savedpicname):
        pospath = os.path.join(self.userdir, 'pos.txt')                      
        with open(pospath,'w') as f:                         
            f.writelines(savedpos + '\n' + savedpicname)    
    #获取图片url列表并加入队列
    def _getpic_list(self):
        #baseurl用于获得第一页推文图片        
        baseurl = 'https://twitter.com/i/profiles/show/{user}/media_timeline?for_photo_rail=true'
        #apiurl用于参数递推获取，相当于下滚翻页
        apiurl = 'https://twitter.com/i/profiles/show/{user}/timeline/tweets?include_available_features=1\
                  &include_entities=1&max_position={pos}&reset_error_state=false'
        re_itemid = r'data-item-id="(.+?)"'
        re_photo = r'data-image-url="(.+?)"'      
        starturl = baseurl.format(user = self.user)
        #该用户首次下载
        if not os.path.exists(self.userdir): 
            os.makedirs(self.userdir)
            savedpos = "0"
            savedpicname = "000000.jpg"
        #更新下载
        else:  
            savedpos ,savedpicname = self.getpos()
        #首页get        
        retjson=requests.get(url = starturl, headers = self.headers).json()
        list_itempos = re.findall(re_itemid, retjson['items_html'])    
        list_picurl = re.findall(re_photo, retjson['items_html'])
        #获取最新下载位置，用于判重
        str_newpos = str_startpos = list_itempos[0]
        #图片列表list_picurl可能为空，最新图片名先赋以前保存值
        str_newpicname = savedpicname      
        str_nextapipos = list_itempos[-1]    
        if (str_startpos <= savedpos):
            print("用户[ %s ]无最新tweets" %self.user)        
        else:
            b_newpic_exists = False           
            while(retjson['new_latent_count'] > 0):
                #获取最新图片名，避免重复下载
                if (b_newpic_exists == False):
                    if (list_picurl != []):
                        str_newpicname = list_picurl[0][28:]
                        b_newpic_exists = True
                #保存的下载位置id在本次get返回列表数据中,但可能图片列表为空
                if (str_nextapipos <= savedpos):
                    if (list_picurl != []):
                        #不为空则在列表中，取出下标
                        if(('https://pbs.twimg.com/media/'+savedpicname)not in list_picurl):
                           # i = list_picurl.index('https://pbs.twimg.com/media/'+str_newpicname)
                           i= len(list_picurl)
                        else:
                            i = list_picurl.index('https://pbs.twimg.com/media/'+savedpicname)   #忘加上'https://pbs.twimg.com/media/' (2018.12.01编辑 )               
                        list_new_picurl = [x + ':orig' for x in list_picurl]
                        for picurl in list_new_picurl[:i]:
                            #len('https://pbs.twimg.com/media/')=28
                            picpath = os.path.join(self.userdir, picurl[28:47])  
                            self.queue.put((picurl, picpath))
                    break               
                else:
                    if (list_picurl != []):
                        list_new_picurl = [x + ':orig' for x in list_picurl]
                        for picurl in  list_new_picurl:                            
                            picpath = os.path.join(self.userdir, picurl[28:47]) 
                            self.queue.put((picurl, picpath)) 
                    #继续get             
                    nextapiurl = apiurl.format(user = self.user, pos = str_nextapipos)                   
                    r = requests.get(url = nextapiurl, headers = self.headers)                   
                    print("get-->statuscode = %d" %r.status_code)    #for debug
                    retjson=r.json()
                    #主线程get太快可能返回404
                    time.sleep(1)                       
                    list_picurl = re.findall(re_photo, retjson['items_html'])
                    list_itempos = re.findall(re_itemid, retjson['items_html'])
                    str_nextapipos = retjson['min_position']
            #保存最新下载位置
            self.setpos(str_newpos, str_newpicname)     
 
if __name__ == "__main__":    
    if not os.path.exists(DEFSAVEDIR):
        os.makedirs(DEFSAVEDIR)    
    while(True):
        username=input('请输入twitter用户名(q退出):')          
        if username=='q':
            break       
        else:   
           TwitterPicScraper(user = username, headers=HEADERS)