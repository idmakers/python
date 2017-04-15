# coding=BIG5


import numpy as np
import math
import random
import cv2
from tkinter import filedialog
import codecs

filename = filedialog.askopenfile()
filenamee = filename.name.encode('UTF-8')
print(filenamee)

img1 = cv2.imread(filename.name)
cv2.imshow("test",img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
