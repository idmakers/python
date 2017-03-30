#coding=utf-8
import numpy as np
import math
import random
import cv2
from tkinter import filedialog
import codecs

filename = filedialog.askopenfile()
print(filename.name)
for l in range(2,5):
    img1 = cv2.imread(filename.name)
    img2 = cv2.imread("D:/WALLPAPER/tumblr_o363gaRyQw1uwi0lpo1_500.png")
    newx1,newy1 = math.floor(img1.shape[1]/l),math.floor(img1.shape[0]/l) #new size (w,h)
    img1= cv2.resize(img1,(newx1,newy1))
    if img1.shape[1]<img1.shape[0]:
        newx,newy = math.floor((newy1/2.6)),math.floor(newx1/1.6)
    else :
        newx,newy = math.floor((newx1/2.6)),math.floor(newy1/1.6)
    img2= cv2.resize(img2,(newx,newy))
    faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.1,
        minNeighbors =6,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    

    font = cv2.FONT_HERSHEY_SIMPLEX
    for(x,y,w,h) in faces:
        cv2.rectangle(img1,(x,y),(x+w,y+h),(14,201,255),2)
        #rowsx = math.floor((x+(w/2))-18)
        rowsx = 0
        tempy = math.floor(y/2)
        colsy = math.floor(tempy - 50/175*tempy)+10
    # I want to put logo on top-left corner, So I create a ROI
        rows,cols,channels = img2.shape
        print("l={}\nface={}\nrowsx ={}\ncolsy ={}\nimg1_shape ={}\nimg2_shape ={}\n" .format(l,faces,rowsx,colsy,img1.shape,img2.shape))

        roi = img1[rowsx:rows+rowsx, colsy:cols+colsy]
        # Now create a mask of logo and create its inverse mask also
        img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
        ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
        mask_inv = cv2.bitwise_not(mask)
        # Now black-out the area of logo in ROI
        img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
        # Take only region of logo from logo image.
        img2_fg = cv2.bitwise_or(img2,img2,mask = mask)
        # Put logo in ROI and modify the main image

        dst1 = cv2.add(img1_bg,img2_fg)
        img1[rowsx:rows+rowsx, colsy:cols+colsy] = dst1

    cv2.imwrite('new'+ str(l) +'.jpg',img1)


cv2.destroyAllWindows()
