import cv2 as cv
import numpy as np
from tkinter import Tk
from tkinter import filedialog
import math
import matplotlib.pyplot as plt



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
#%%
def create_image3():
    img3 = cv.imread("E:\\D4wyR0JXkAAg1O-.jpg")
    newx,newy = math.floor(img3.shape[1]/4),math.floor(img3.shape[0]/4) #new size (w,h)
    newimage = cv.resize(img3,(newx,newy))
    plt.imshow(img3)
    plt.show()
    x = int(newx/2)
    for i in range (0,x*2,1):
        newimage[:, i, 0] = newimage[:, i, 0]*0
        newimage[:, :, 1] = newimage[:, :, 1]
        newimage[:, :, 2] = newimage[:, :, 2]
    print(newimage[:, :,:])
    #np.savetxt("filename1.txt", newimage[:, :,:],newline='\n',fmt='%3d')
    savedata (newimage,"test1.txt")
    plt.imshow(newimage)
    plt.show()
    print("**********************************************" )
    newimage = cv.cvtColor(newimage, cv.COLOR_BGR2HLS)
    for i in range (0,x,1):
        newimage[:, i, 0] = newimage[:, i, 0]
        newimage[:, :, 1] = newimage[:, :, 1]
        newimage[:, :, 2] = newimage[:, :, 2]
    print(newimage[:, :, :])
    #np.savetxt("filename3.txt", newimage[:, :,:],newline='\n',fmt='%3d')
    savedata (newimage,"test2.txt")
    plt.imshow(newimage)
    plt.show()
   

    #img.reshape = (200,200
 
create_image3()

cv.waitKey(0)
cv.destroyAllWindows()

#%%
