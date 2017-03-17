import cv2
import numpy as np
import math
import random

oriimage = cv2.imread("D:/WALLPAPER/QAadYa1.jpg")
newx,newy = math.floor(oriimage.shape[1]),math.floor(oriimage.shape[0]) #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
faceCascade = cv2.CascadeClassifier('C:/Users/IDMAKERS/Desktop/data/haarcascades/haarcascade_frontalface_default.xml')
gray = cv2.cvtColor(newimage,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor = 1.1,
    minNeighbors = 5,
    minSize = (10,10),
    flags = cv2.CASCADE_SCALE_IMAGE
)
print (faces)

font = cv2.FONT_HERSHEY_SIMPLEX
for(x,y,w,h) in faces:
    cv2.rectangle(newimage,(x,y),(x+w,y+h),(14,201,255),2)

cv2.imshow("resize image",newimage)
cv2.waitKey(0)
