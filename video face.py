import numpy as np
import cv2
import math

cap = cv2.VideoCapture('D:/123.mp4')
# face
faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
while(True):
    # Capture frame-by-frame
    ret, newimage = cap.read()
    newx,newy = math.floor(newimage.shape[1]/2),math.floor(newimage.shape[0]/2) #new size (w,h)
    resize = cv2.resize(newimage ,(newx,newy))

    # Our operations on the frame come here
    gray = cv2.cvtColor(newimage, cv2.COLOR_BGR2GRAY)
    '''
    # face detect
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor =1.1,
        minNeighbors = 5,
        minSize = (30,30),
        flags = cv2.CASCADE_SCALE_IMAGE
    )
    print (faces)

    font = cv2.FONT_HERSHEY_SIMPLEX
    for(x,y,w,h) in faces:
        cv2.rectangle(newimage,(x,y),(x+w,y+h),(14,201,255),2)
        '''
    # Display the resulting frame
    cv2.imshow('frame',newimage)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
