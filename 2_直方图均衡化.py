#直方图均衡化

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lenna.png", 1) #flag =1, 加载彩色图像，任何图像的透明度都会被忽略，它是默认标志, flag = 0, 以灰度模式加载图像, flag =-1,加载图像，包括 alpha 通道
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#灰度图像直方图均衡化
dst = cv2.equalizeHist(gray)  #equalizeHist(src, dst = None),src:图像矩阵(单通道)；dst:默认即可
# hist = cv2.calcHist([dst],[0],None,[256],[0,256])  #直方图
"""
cv2.calcHist(images,channels,mask,histSize,ranges) 
images:原图像图像格式为 uint8 或 ﬂoat32。当传入函数时应用中括号[]括,例如[img]
channels: 指定待计算直方图的图像的哪一通道用来计算直方图。灰度图它的值就是 [0],RGB图像可以指定[0,1,2]，它们分别对应着BGR
mask: 掩模图像。可以指定图像的范围，如果是全图，默认为none
histSize:为直方图的灰度级数，例如[0,255]一共256级，故参数为256，需用[]包裹
"""
plt.figure()
plt.hist(dst.ravel(), 256)  #dst.ravel()将dst图像的array数组转成一维的数组，256为直方图的灰度级数
plt.show()

cv2.imshow("Histogram Equalization", np.hstack((gray, dst)))  #np.hstack将参数元组的元素数组按水平方向进行叠加
# cv2.waitkey(0)

#彩色直方图均衡化
# cv2.imshow("src", img)
#彩色图像均衡化，需要分解通道，对每个通道均衡化
(b,g,r) = cv2.split(img)  # 3通道BGR彩色图像分离为 B、G、R单通道图像，再分别进行直方图均衡化操作
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
result = cv2.merge((bH, gH, rH))  #将B、G、R单通道合并为 3通道BGR彩色图像
# cv2.imshow("dst_rgb", result)
cv2.imshow("Histogram Equalization2", np.hstack((img, result)))
cv2.waitKey(0)
# cv2.destroyAllWindows() #释放所有窗口









