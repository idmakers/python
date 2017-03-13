import time
import os
import sys
from PIL import Image ,ImageGrab


SavePath =r'C:\screenShot'

img = ImageGrab.grabclipboard()
saveas=os.path.join(SavePath,'ScreenShot_'+time.strftime("%Y-%m-%d_%H%M%S")+'.jpg')
img.save(saveas)
