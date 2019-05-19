import numpy as np
import math
import random
import cv2
from tkinter import filedialog
import codecs
import shutil
import os


filename = filedialog.askopenfile()
dirold = filedialog.askdirectory()
dirnew = (dirold +"/wallpaper")
print(filename.name)
class img(object):
    def __init__(self,file):
        self.file = file
    def run(self):
        self.file = cv2.imread(filename.name)
        weight,height =self.file.shape[1],self.file.shape[0]#(w,h)
        if(weight > height):
            os.rename(dirold,dirnew)
            #shutil.move(dirold,dirnew)

    if not os.path.exists(dirnew):
        os.makedirs(dirnew)   

if __name__ == "__main__":
    img(filename)

    
    