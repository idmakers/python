#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt
import math
import os
import random
#%%

f = open('C:/Users/idmakers/Desktop/image/filename.txt','r')
input_string = f.read()
name  = input_string.split()
name.extend("q")
f.close
#root = Tk()
#root.filename =  file.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
for i  in  range(len(name)):
        imgname=name[i]
        oriimage = cv2.imread('C:/Users/idmakers/Desktop/image/'+imgname)
        #rabbit = cv2.imread("D:/WALLPAPER/tumblr_o363gaRyQw1uwi0lpo1_500.png")
        newx,newy = math.floor(oriimage.shape[1]/3),math.floor(oriimage.shape[0]/3) #new size (w,h)
        newimage = cv2.resize(oriimage,(newx,newy))
        plt.imshow(cv2.cvtColor(newimage,cv2.COLOR_BGR2RGB))
        plt.show()
        faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
        gray = cv2.cvtColor(newimage,cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor = 1.1,
            minNeighbors = 5,
            minSize = (30,30),
            flags = cv2.CASCADE_SCALE_IMAGE
        )
        print (faces)

        font = cv2.FONT_HERSHEY_SIMPLEX
        for(x,y,w,h) in faces:
            cv2.rectangle(newimage,(x,y),(x+w,y+h),(14,201,255),2)
        plt.imshow(cv2.cvtColor(newimage,cv2.COLOR_BGR2RGB))
        plt.show()
cv2.waitKey(0)


#%%


#%%
