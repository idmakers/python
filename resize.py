#%%
import os
import re
import json
import requests
import random
import time
from tkinter import filedialog
from tkinter import Tk
import cv2 as cv
import matplotlib.pyplot as plt
#%%
#run

#%%
f = open('C:/Users/idmakers/Desktop/image/filename.txt','r')
input_string = f.read()
name  = input_string.split()
name.extend("q")
f.close
print(name)
#%%
for i  in  range(len(name)):
        imgname=name[i]
        imgname2=name[i+1]
        
        
        print(imgname)
        if imgname =="q":
            print("test")
            break
        else:
            img = cv.imread('C:/Users/idmakers/Desktop/image/'+imgname)
            img2 =cv.imread('C:/Users/idmakers/Desktop/image/'+imgname2)
            
            img = cv.resize(img,(900,600))
            img2 =cv.resize(img,(900,600))
            img[:,:,0] = img[:,:,0]*0
            img[:,:,1] = img[:,:,1]*0
            img[:,:,2] = img[:,:,2]
            plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))
            print(imgname+" "+str(i))
            print(imgname2+"++ ")
            plt.show()
        
#%%

