"""
彩色图片的灰度化、二值化（自己实现&调用接口）
"""
from skimage.color import rgb2gray
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import cv2

plt.subplot(231)
# img = cv2.imread("lenna.png", False)
img = plt.imread("lenna.png")
plt.imshow(img)
print("--- image original---")
print(img)

#灰度化-自己实现
img = cv2.imread("lenna.png")
h, w = img.shape[:2]  #获取图片的长宽
img_gray1 = np.zeros([h, w], img.dtype)  #创建一张全零的和原图大小一致的单通道图片
for i in range(h):
    for j in range(w):
        m = img[i,j]  #取出当前长宽的BGR坐标
        img_gray1[i,j] = int(m[0]*0.11 + m[1]*0.59 + m[2]*0.3)  #将BGR坐标以浮点坐标转化为gray坐标并赋给新图像
        # img_gray1[i,j] = int((m[0] + m[1] + m[2])/3)  #平均值法
        # img_gray1[i,j] = int(m[0])  #仅取单色法
plt.subplot(232)
plt.imshow(img_gray1, cmap = 'gray')  #cmap是colormap的简称，用于指定渐变色
print("--- image img_gray1---")
print(img_gray1)

#灰度化-调接口
img_gray = rgb2gray(img)
# img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.subplot(233)
plt.imshow(img_gray, cmap = 'gray')
print("--- image img_gray---")
print(img_gray)

#二值化-法一
img_binary1 = img_gray
rows, cols = img_binary1.shape
for i in range(rows):
    for j in range(cols):
        if (img_binary1[i,j] < 0.5):
            img_binary1[i,j] = 0
        else:
            img_binary1[i,j] = 1

plt.subplot(234)
plt.imshow(img_binary1, cmap = 'gray')
print("---img_binary1---")
print(img_binary1)

#二值化-法二

img_binary = np.where(img_gray >= 0.5, 1, 0)
plt.subplot(236)
plt.imshow(img_binary, cmap = 'gray')
print("---img_binary---")
print(img_binary)
plt.show()