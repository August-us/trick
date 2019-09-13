import os
from PIL import Image
import matplotlib.pyplot as plt
print( os.getcwd())
print(os.name)
imgname1=r'C:\Users\Administrator\Desktop\拉斐尔他画像.jpg'
imgname2=r'C:\Users\Administrator\Desktop\拉斐尔自画像.jpg'

plt.figure()
img1=Image.open(imgname1)

plt.subplot(1,2,2)
img2=Image.open(imgname2)
plt.imshow(img2)

plt.subplot(1,2,1)
img1=img1.transpose(Image.FLIP_LEFT_RIGHT)
plt.imshow(img1)

plt.show()






