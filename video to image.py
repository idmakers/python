#%%
import math
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#%%
for i in range(0,19):
    num = str(i)
    f = open("E:\\filename"+num+".txt", "r")
    line = f.readline()
    wide = int(line[16:19])
    print(wide)
    high = int(line[21:24])
    print(high)
    img4 = np.loadtxt("E:\\filename"+num+".txt")
    img4 = img4.astype(np.uint8)
    img4 = img4.reshape(wide, high, 3)
    for i in range(50,100):        
        img4[:,i,0]=img4[:,i,0]
        img4[:,i,1]=img4[:,i,1]
        img4[:,i,2]=img4[:,i,2]
    plt.imshow(img4)
    plt.show()
#%%
    for i in range(100,300):        
        img4[i,:,0]=img4[i,:,0]
        img4[i,:,1]=img4[i,:,1]
        img4[i,:,2]=img4[i,:,2]
    plt.imshow(img4)
    plt.show()
#%%
    for i in range(150,200):        
        img4[i,:,0]=img4[i,:,0] 
        img4[i,:,1]=img4[i,:,1] 
        img4[i,:,2]=img4[i,:,2]
    plt.imshow(img4)
    plt.show()
#%%
cv.waitKey(0)

#%%
