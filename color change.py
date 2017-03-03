import cv2
import numpy as np
import math

oriimage = cv2.imread("your file path")
newx,newy = math.floor(oriimage.shape[1]/8),math.floor(oriimage.shape[0]/8) #new size (w,h)
newimage = cv2.resize(oriimage,(newx,newy))
gray =cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
HSV =cv2.cvtColor(newimage, cv2.COLOR_BGR2HSV)
RGB =cv2.cvtColor(newimage, cv2.COLOR_BGR2RGB)
YCrCb =cv2.cvtColor(newimage, cv2.COLOR_BGR2YCrCb)
XYZ =cv2.cvtColor(newimage, cv2.COLOR_BGR2XYZ)
HLS =cv2.cvtColor(newimage, cv2.COLOR_BGR2HLS)
CIE =cv2.cvtColor(newimage, cv2.COLOR_BGR2Lab)

cv2.imshow("bgr2gray",gray)
cv2.imshow("bgr2HSV",HSV)
cv2.imshow("bgr2RGB",RGB)
cv2.imshow("BGR2YCbCr",YCrCb)
cv2.imshow("BGR2XYZ",XYZ)
cv2.imshow("BGR2HLS",HLS)
cv2.imshow("BGR2CIE",CIE)
cv2.imshow("resize image",newimage)
cv2.waitKey(0)
