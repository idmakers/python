import cv2 as cv
import numpy as np
from tkinter import Tk
from tkinter import filedialog
import math


 
 
print("456" )
def create_image3():
    img3 = cv.imread("E:\\D4wyR0JXkAAg1O-.jpg")
    newx,newy = math.floor(img3.shape[1]/4),math.floor(img3.shape[0]/4) #new size (w,h)
    newimage = cv.resize(img3,(newx,newy))
    x = int(newx/4)
    newimage[:, :, 0] = newimage[:, :, 0]
    newimage[:, :, 1] = newimage[:, :, 1]
    newimage[:, :, 2] = newimage[:, :, 2]
    cv.imshow("test",newimage)
    newimage = cv.cvtColor(newimage, cv.COLOR_BGR2HLS)
    cv.imshow("test1",newimage)
    newimage[:, :, 0] = newimage[:, :, 0]*0
    newimage[:, :, 1] = newimage[:, :, 1]
    newimage[:, :, 2] = newimage[:, :, 2]
    cv.imshow("test2",newimage)
   

    #img.reshape = (200,200
 
create_image3()

cv.waitKey(0)
cv.destroyAllWindows()