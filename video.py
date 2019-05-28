import numpy as np
import cv2
import math
 
cap = cv2.VideoCapture("C:/Users/idmakers/Desktop/123.mkv")

# Define the codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*'XVID')



def savedata (data,name):
    with open(name, 'w') as outfile:
    # I'm writing a header here just for the sake of readability
    # Any line starting with "#" will be ignored by numpy.loadtxt
        outfile.write('# Array shape: {0}\n'.format(data.shape))

        # Iterating through a ndimensional array produces slices along
        # the last axis. This is equivalent to data[i,:,:] in this case
        for data_slice in data:

            # The formatting string indicates that I'm writing out
            # the values in left-justified columns 7 characters in width
            # with 2 decimal places.  
            np.savetxt(outfile, data_slice, fmt='%3d')

        # Writing out a break to indicate different slices...
            outfile.write('# New slice\n')


# 关闭文件

count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        height , width , layers =  frame.shape
        new_h=math.floor(height/2)
        new_w=math.floor(width/4)
        frame  = cv2.resize(frame, (new_w*2, new_h))
        frameN  = cv2.resize(frame, (new_w, new_h))
        #np.savetxt("filename1", frame[:, :, 0])
        #for i in range (0,new_w,1):
        frame[:, :, 0] = frame[:, :, 0]
        #for i in range (0,new_w,4):
        frame[:, :, 1] = frame[:, :, 1]
        #for i in range (0,new_w,6):
        frame[:, :, 2] = frame[:, :, 2]
        #np.savetxt("filename", frame[:, :, 0])
        cv2.imshow("frame",frameN)
        c = str(count)
        savedata(frame,"filename"+c+".txt")
        count= count+1
        


    # write the flipped frame
        

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
cap.release()
cv2.destroyAllWindows()