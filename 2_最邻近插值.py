# 最邻近插值

import cv2
import numpy as np

def function(img):
    height,width,channels = img.shape
    emptyImage = np.zeros((700,700,channels), np.uint8)
    sh = 700/height  #对比原图的长度需要放大的倍数
    sw = 700/width  #对比原图的宽度需要放大的倍数
    for i in range(700):
        for j in range(700):
            x = int(i/sh + 0.5)  #int为向下取整， +0.5可保证插入的新像素点取值为其最邻近的像素点的值(坐标)
            y = int(j/sw + 0.5)  #通过目标图片与原图片的比例大小，找到目标像素点y坐标对应的原像素点的坐标
            emptyImage[i,j] = img[x,y]  #将原像素点值赋值给目标像素点坐标
    return emptyImage

img = cv2.imread("lenna.png")
zoom = function(img)
print(zoom)
print(zoom.shape)  #OpenCv里的shape函数返回图像的行列以及色彩通道数
cv2.imshow("nearest interp", zoom)  #输入中文会乱码
cv2.imshow("image", img)
cv2.waitKey(0)
