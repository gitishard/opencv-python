import numpy as np
import cv2

img = np.zeros((512,512,3),np.uint8)
#function(img,position,color,tickness,linetype)
#line(img,sartPostion,endPostion,color,tickness,linetype)
cv2.line(img,(0,0),(511,511),(255,0,0),3,cv2.LINE_AA)
#rectangle(img,top-leftPostion,right-bottomPosition,color,tickness)
cv2.rectangle(img,(384,0),(510,128),(0,255,0),-1)
#ellipse(img,(x,y),(major axis length,minor axis length),angle,startangle,endangle,color,tickness)
cv2.ellipse(img,(255,255),(100,50),45,0,180,255,1)
#circle(img,(x,y),radius,color,tickness)
cv2.circle(img,(447,63),62,(0,0,255),1)
pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255))
#putText(img,text,position,fonttype,fontScale,color,tickness,linetype)
cv2.putText(img,'SiYuan',(10,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),2,cv2.LINE_AA)
cv2.imshow('img',img)
if cv2.waitKey(0) & 0xFF == ord('q'):
	cv2.release()
	cv2.destoryAllWindows()
