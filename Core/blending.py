import numpy 
import cv2

#img1.shape=(185,450,3)
#img2.shape=(99,82,3)
img2 = cv2.imread('logo.png')
img1 = cv2.imread('blending.jpg')

#draw ROI in img1,so img1.width>img2.width and img1.height>img2.height
rows,cols,channels = img2.shape
roi = img1[0:rows,0:cols]

img2gray = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

#threshold(srcimg,threshold value,maxval,type),in THRESH_BIINARY if binary value < thresh dst(x,y)=maxval else dst(x,y)=0 and return threshold value 
#ret = threshold and mask = dstArray 
ret, mask = cv2.threshold(img2gray,10,255,cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

#black-out the area of logo in ROI
img1_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)
#Take only region of logo from logo image
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)

dst = cv2.add(img1_bg,img2_fg)
img1[0:rows,0:cols] = dst
#addWeighted(image1,weight1,image2,weight2,bias)
#dst = cv2.addWeighted(img1,0.7,img2,0.3,0)

cv2.imshow('res',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
