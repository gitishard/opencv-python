#-*- coding: utf-8 -*-
#cv2.cvtColor(image,flage) change image type to flage
#cv2.inRange(image,lower_boundary,upper_boundary) reutrn a ndarry range lower_boundary tp upper_boundary

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    # Take each frame, return a boolean and numpy object
    _, frame = cap.read()

    #Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #define range of blue color in HSV
    #lower_blue = np.array([110,50,50])
    #upper_blue = np.array([130,255,255])
    lower_green = np.array([35,40,50])
    upper_green = np.array([80,255,255])

    #Threshold the HSV image to get only blue colors
    #mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = cv2.inRange(hsv, lower_green, upper_green)
    
    #Bitwise-AND mask and original image
    #dst(i) = src1(i) and src2(i) if mask(i) is not 0
    res = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('frame',frame)
    # show mask region
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destoryAllWindows()


