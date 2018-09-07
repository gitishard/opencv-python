import numpy as np
import cv2

#load harr cascade classifier
detector = cv2.CascadeClassifier('/home/yuan/opencv/opencv-3.3.0/data/haarcascades/haarcascade_frontalface_default.xml')

#load eye cascade classifier
eye = cv2.CascadeClassifier('/home/yuan/opencv/opencv-3.3.0/data/haarcascades/haarcascade_eye.xml')

#capture video stream
cam = cv2.VideoCapture(0)

while(True):
    #get a frame
    ret, img = cam.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #detectMultiScale(srcImg,scaleFactor,minNeighbors)
    #this function has three definition and return a vector objects of rectangle
    faces = detector.detectMultiScale(gray, 1.3, 5)
    
    for (x,y,w,h) in faces:
        #draw a rectangle at (x,y) which weight is x+w, and height is y+h, blue,thickness is 2
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h,x:x+w]
        roi_color = img[y:y+h,x:x+w]
        
        # find eyes within the region of the rectangle in faces
        eyes = eye.detectMultiScale(roi_gray)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2) 

    cv2.imshow('frame',img)
    if cv2.waitKey(30) & 0xFF == 27:
        break

cam.release()
cv2.destroyAllWindows()
