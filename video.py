#%%
import sys
import numpy as np
import cv2
import math
from tkinter import Tk as tk
from tkinter import filedialog 
import matplotlib.pyplot as plt


root = tk()
root.file = filedialog.askopenfilename()
print(root.file)
cap = cv2.VideoCapture(root.file)

# Define the codec and create VideoWriter object
length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print( length )
#%%
number = 0
#%%


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
#%%
count = 0
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        height , width , layers =  frame.shape
        newh = math.ceil(height/3)
        neww = math.ceil(width/3)
        frame = cv2.resize(frame,(neww,newh))
        #np.savetxt("filename1", frame[:, :, 0])
        #for i in range (0,new_w,1):
        frame[:, :, 0] = frame[:, :, 2]
        #for i in range (0,new_w,4):
        frame[:, :, 1] = frame[:, :, 1]
        #for i in range (0,new_w,6):
        frame[:, :, 2] = frame[:, :, 0]
        #np.savetxt("filename", frame[:, :, 0])
        #cv2.imshow("frame",frame)
        c = str(number+int(count/10))
        if(count%10==0):
            savedata(frame,"E:\\filename"+c+".txt")
        count= count+1
        length = length-1
        plt.imshow(frame)
        plt.show()
        

        
        


    # write the flipped frame
        

        #cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
# Release everything if job is finished
#%%
cap.release()
cv2.destroyAllWindows()

#%%
