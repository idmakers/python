import numpy as np
import cv2
import math

cap = cv2.VideoCapture('D:/123.mp4')
#faceCascade = cv2.CascadeClassifier('C:\opencv-build\install\etc\haarcascades\haarcascade_frontalface_default.xml')
while(cap.isOpened()):
    ret, frame = cap.read()

    newx,newy = math.floor(frame.shape[1]/2),math.floor(frame.shape[0]/2) #new size (w,h)
    newimage = cv2.resize(frame ,(newx,newy))
    gray = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
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
    #cv2.imshow("image",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
