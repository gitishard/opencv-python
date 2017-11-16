import numpy as np
import cv2
#cam = cv2.VideoCapture(0)
detector=cv2.CascadeClassifier('/home/yuan/opencv/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')
eye=cv2.CascadeClassifier('/home/yuan/opencv/opencv-3.3.0/data/haarcascades/haarcascade_eye.xml')
cam = cv2.VideoCapture(0)
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray=gray[y:y+h,x:x+w]
        roi_color=img[y:y+h,x:x+w]
        eyes = eye.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 
    cv2.imshow('frame',img)
    #wait for 100 miliseconds 
    if cv2.waitKey(30)==27:
        break
cam.release()
cv2.destroyAllWindows()
