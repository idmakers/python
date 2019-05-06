import cv2
import numpy as np
import math
from tkinter import filedialog
from tkinter import Tk




root = Tk()
'''
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
print (root.filename)
'''
class change_color(object):
    def __init__(self,oriimage):
        self.oriimage = oriimage
        
    def run(self):
        oriimage = self.oriimage
        oriimage = cv2.imread(oriimage)
        newx,newy = math.floor(oriimage.shape[1]/4),math.floor(oriimage.shape[0]/4) #new size (w,h)
        newimage = cv2.resize(oriimage,(newx,newy))
        self.gray =cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
        self.HSV =cv2.cvtColor(newimage, cv2.COLOR_BGR2HSV)
        self.RGB =cv2.cvtColor(newimage, cv2.COLOR_BGR2RGB)
        self.YCrCb =cv2.cvtColor(newimage, cv2.COLOR_BGR2YCrCb)
        self.XYZ =cv2.cvtColor(newimage, cv2.COLOR_BGR2XYZ)
        self.HLS =cv2.cvtColor(newimage, cv2.COLOR_BGR2HLS)
        self.CIE =cv2.cvtColor(newimage, cv2.COLOR_BGR2Lab)
        self.show()
    

    def show(self):
        cv2.imshow("bgr2gray",self.gray)
        cv2.imshow("bgr2HSV",self.HSV)
        cv2.imshow("bgr2RGB",self.RGB)
        cv2.imshow("BGR2YCbCr",self.YCrCb)
        cv2.imshow("BGR2XYZ",self.XYZ)
        cv2.imshow("BGR2CIE",self.CIE)
        cv2.imshow("BGR2CIE",self.HLS)
       

if __name__ == "__main__":
    while(True):
        
        root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
        print (root.filename)
        if root.filename:
            change = change_color(root.filename)
            change.run()
            
        else:
            break