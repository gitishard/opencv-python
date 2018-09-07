#-*- coding: utf-8 -*-
import numpy as np
import cv2

img = cv2.imread('/home/yuan/Desktop/opecvdemo/demo/th.jpeg',0)

'''resize(img,dst_size,fx,fy,interpolation) you can just give dst_size, fx,fy will compute from that;
resize(src,dst,dst_size(),0,0,interpolation）
you can specify fx,fy and let the function compute the destination image size
resize(src,dst,Size(),fx,fy,interpolation)'''

#res = cv2.resize(img, None,fx = 2, fy = 2, interpolation = cv2.INTER_CUBIC)
rows, cols = img.shape
#M = np.float32([[1,0,100],[0,1,50]])
M = cv2.getRotationMatrix2D((cols/2, rows/2),90,1)

#the third argument of warpAffine() is the size of the output image
dst = cv2.warpAffine(img, M,(cols,rows))
cv2.imshow('origion',img)
cv2.imshow('res',dst)

cv2.waitKey(0)
cv.destoryAllWindows()
