import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import sys
import copy

#python 图像翻转,自定义翻转

img = cv.imread(r'C:\Users\Administrator\Desktop\1.png')

def flip():
    if img.all()==None:
        print('No Such image!')
        sys.exit(0)
    size = img.shape
    iCopy = copy.deepcopy(img)
    iCopy1 = copy.deepcopy(img)
    iCopy2 = copy.deepcopy(img)
    h = size[0]
    w = size[1]

    for i in range(h):
        for j in range(w):
            iCopy[i,w-1-j] = img[i,j]#水平镜像
            iCopy1[h-1-i,j] = img[i,j]#垂直镜像
            iCopy2[h-1-i,w-1-j] = img[i,j]#对角镜像
    plt.subplot(221),plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(iCopy)
    plt.title('Remap shuiping Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(iCopy1)
    plt.title('Remap chuizhi Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(iCopy2)
    plt.title('Remap duijiao Image'), plt.xticks([]), plt.yticks([])

    plt.show()
    #python 图像翻转,使用openCV flip()方法翻转
    xImg = cv.flip(img,1,dst=None) #水平镜像
    xImg1 = cv.flip(img,0,dst=None) #垂直镜像
    xImg2 = cv.flip(img,-1,dst=None) #对角镜像
    plt.subplot(221),plt.imshow(img)
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222),plt.imshow(xImg)
    plt.title('Remap shuiping Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(223),plt.imshow(xImg1)
    plt.title('Remap chuizhi Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224),plt.imshow(xImg2)
    plt.title('Remap duijiao Image'), plt.xticks([]), plt.yticks([])

    plt.show()

def Dewatermark():
    src=img
    hsv = cv.cvtColor(src, cv.COLOR_BGR2HSV)
    lower_hsv = np.array([0, 43, 46])
    upper_hsv = np.array([10, 255, 255])
    mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
    mask=cv.bitwise_not(mask)
    # print(mask)
    mask=np.concatenate([mask[:,:,np.newaxis]]*3,axis=2)
    src=cv.bitwise_not(src*mask)
    cv.bitwise_and
    # dst = cv.bitwise_and(src, mask)
    cv.imwrite(r'C:\Users\Administrator\Desktop\1.png', src)
    # cv.imshow("mask", dst)
    cv.waitKey(0)


if __name__=='__main__':
    Dewatermark()