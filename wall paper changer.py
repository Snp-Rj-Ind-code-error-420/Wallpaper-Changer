import ctypes
import os
import time
import random
'''drive = "F:\\"
folder = "raja picture"
image = "IMG-20161207-WA0007.jpg"
image_path = os.path.join(drive, folder, image)
print (image_path)'''
SPI_SETDESKWALLPAPER  = 0x0014
SPIF_UPDATEINIFILE    = 0x0001
SPIF_SENDWININICHANGE = 0x0002
def get_file(image_path):
    lst=["IMG-20161207-WA0007.jpg","IMG-20161207-WA0020.jpg","RAJA.jpg"]
    k=random.choice(lst)
    drive = "F:\\"
    folder = "raja picture"
    image_path = os.path.join(drive, folder, k)
    print("random choice",k)
    print("img path",image_path)
    return image_path
                
#user32 = ctypes.WinDLL('user32')
while True:
    time.sleep(2)
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, get_file(""), SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE)
