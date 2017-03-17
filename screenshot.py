import time
import os
import sys
from PIL import Image ,ImageGrab




img = ImageGrab.grab()

img.save('ScreenShot_'+time.strftime("%Y-%m-%d_%H%M%S")+'.jpg',"JPEG")
