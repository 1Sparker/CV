#直方图

import numpy as np
import cv2
from matplotlib import pyplot as plt

'''
calcHist—计算图像直方图
函数原型：calcHist(images, channels, mask, histSize, ranges, hist=None, accumulate=None)
images：图像矩阵，例如：[image]
channels：通道数，例如：0
mask：掩膜，一般为：None
histSize：直方图大小，一般等于灰度级数
ranges：横轴范围
'''
#灰度图像直方图
#获取灰度图像
img = cv2.imread("lenna.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#灰度图像的直方图，法一
plt.figure()  #新建一个画布
plt.hist(gray.ravel(), 256)  #将gray array用一维数组表示，并以直方图256灰度级显示
plt.show()

#灰度图像的直方图，方法二
hist2 = cv2.calcHist([gray],[0],None,[256],[0,256])  #将gray以灰度级256，横轴范围[0,256]的直方图表示
plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")  #x轴标签
plt.ylabel("# of Pixels") #Y轴标签
plt.plot(hist2)
# plt.xlim([0,256])  #设置x坐标轴范围
plt.show()

#彩色图像直方图
cv2.imshow("Original", img)
cv2.waitKey(0)

chans = cv2.split(img) # 3通道BGR彩色图像分离为 B、G、R单通道图像，
colors = ("b","g","r")
plt.figure()
plt.title("Flattened Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for (chan,color) in zip(chans,colors):  #zip()函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
    hist3 = cv2.calcHist([chan],[0],None,[256],[0,256])
    plt.plot(hist3,color = color)
    # plt.xlim([0,256])
plt.show()

