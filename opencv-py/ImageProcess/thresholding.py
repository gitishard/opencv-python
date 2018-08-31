'''
Name:threshold()
Function:Applies fixed-level thresholding to a multiple-channel array
Return: dstImage
Parameter:	srcImage,	#8bit/32bit float multiple-channel
			thresh,		#threshold value
			maxVal,		#
			type		#thresholding type
Description:
			Assign the value to the pixel according to the threshold_style which the condition is satisfied


Name:adaptiveThreshold()
Function: Applies an adaptive threshold to array, transforms a grayscale image to a binary image
Return: binary image
Parameter:  srcImage,		#8bit single-channel image
			maxValue,		#non-zero value assign to the pixels for which the condition is satisfied
			adaptiveMethod,	#choose the thresholding algorithem to use
			threshold_style,#THRESH_BINARY or THRESH_BINARY_INV
			blockSize,		#size of a pixel neighborhood that is used to calculate a threshold value for the pixel
			C				#constant subtracted from the mean or wighted mean
Description:
			THRESH_BINARY: dst(x,y) =   maxValue	if src(x,y) > T(x,y)
										0			otherwise

			THRESH_BINARY_INV: dst(x,y) =   0				 if src(x,y) > T(x,y)
											maxValue		 otherwise	
			T is calculated by blockSize

Name:medianBlur()
Function:blurs an image using the median filter
Return:dstImage
Parameter:	srcImage,
			ksize,	#aperture(孔),linear size,it must be odd and greater than 1
Description:
			the function smoothes an image using the median filter with the ksize*ksize aperture
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("/home/yuan/Pictures/capture.png",0)
ret, thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles = ['Original','Binary','Binary_Inv','Trunc','Tozero','Tozero_Inv']
images = [img,thresh1,thresh2,thresh3,thresh4,thresh5]

for i in range(6):
	plt.subplot(2,3,i+1)
	plt.imshow(images[i],cmap='gray')
	plt.title(titles[i])
	plt.xticks([])
	plt.yticks([])

plt.show()
