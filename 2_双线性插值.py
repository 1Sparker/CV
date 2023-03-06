#双线性插值(几何中心对齐)

import numpy as np
import cv2

def bilinear_interpolation(img, out_dim):
    src_h, src_w, channel = img.shape
    dst_h, dst_w = out_dim[0], out_dim[1]
    print("src_h, src_w =", src_h, src_w)
    print("dst_h, dst_w =", dst_h, dst_w)
    if src_h == dst_h and src_w == dst_w:
        return img.copy()  #当目标图片与原图片大小一致时，返回将原图片复制后的图片
    dst_img = np.zeros((dst_h, dst_w,3), dtype = np.uint8)  #数据类型为 np.uint8，也就是0~255
    scale_x, scale_y = float(src_w / dst_w), float(src_h / dst_h)  #计算原图与目标图长宽的缩放倍数
    for i in range(3):
        for dst_y in range(dst_h):
            for dst_x in range(dst_w):
                #根据目标像素点坐标求出对应原像素点坐标
                src_x = (dst_x + 0.5) * scale_x - 0.5  #让原图片与目标图片坐标中心对齐
                src_y = (dst_y + 0.5) * scale_y - 0.5
                #利用双线性插值求出插值点坐标对应的像素值
                src_x0 = int(np.floor(src_x))  #np.floor:对输入的多维数组逐元素向下取整
                src_x1 = min(src_x0 + 1, src_w -1)
                src_y0 = int(np.floor(src_y))
                src_y1 = min(src_y0 + 1, src_h -1)
                temp0 = (src_x1 - src_x) * img[src_y0, src_x0,i] + (src_x - src_x0) * img[src_y0,src_x1,i]
                temp1 = (src_x1 - src_x) * img[src_y1, src_x0,i] + (src_x - src_x0) * img[src_y1,src_x1,i]
                dst_img[dst_y,dst_x,i] = int((src_y1 - src_y) * temp0 + (src_y - src_y0) * temp1)
    return dst_img

if __name__ == '__main__':
    img = cv2.imread('lenna.png')
    dst = bilinear_interpolation(img,(700,700))
    cv2.imshow('bilinear interp',dst)
    cv2.waitKey()  #waitkey控制着imshow的持续时间，注释该条code,图片闪下就没，括号内填1000，停留1s,不填，一直存在









