import numpy as np
import cv2
import math

cap = cv2.VideoCapture(0)
img2 = cv2.imread("D:/WALLPAPER/tumblr_o363gaRyQw1uwi0lpo1_500.png")
# face
faceCascade = cv2.CascadeClassifier('./data/haarcascades/haarcascade_frontalface_default.xml')
while(True):
    # Capture frame-by-frame
    ret, newimage = cap.read()
    newx1,newy1 = math.floor(newimage.shape[1]),math.floor(newimage.shape[0]) #new size (w,h)
    img1= cv2.resize(newimage ,(newx1,newy1))
    newx,newy = math.floor((newx1/5)),math.floor(newy1/5)
    img2= cv2.resize(img2,(newx,newy))

    # Our operations on the frame come here
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)

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
        cv2.rectangle(img1,(x,y),(x+w,y+h),(20,201,255),2)
        rowsx = 0
        tempy = math.floor(y/2)
        colsy = math.floor(tempy - 50/175*tempy)+10
    # I want to put logo on top-left corner, So I create a ROI
        rows,cols,channels = img2.shape
        print("\nface={}\nrowsx ={}\ncolsy ={}\nimg1_shape ={}\nimg2_shape ={}\n" .format(faces,rowsx,colsy,img1.shape,img2.shape))

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

    # Display the resulting frame
    cv2.imshow('frame',img1)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
