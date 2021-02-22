import cv2 as cv
import numpy as np
import time as t

background= np.zeros((750,750,1),dtype='uint8')
background[:]=30
print("press d to exit")
a=70
#changing the background
for i in range(25):
	text="Weber ratio "+ str(round((190-a)/190,2))
	cv.putText(background, text, (100,100), cv.FONT_HERSHEY_TRIPLEX,1.0,(255), 1) #this will how weiber ratio will change by changing changing background
	cv.rectangle(background, (int(750//2-500//2),int(750//2-500//2)),(int(750//2+500//2),int(750//2+500//2)),(a), thickness=-1) #background its color varies with time
	cv.rectangle(background, (int(750//2-250//2),int(750//2-250//2)),(int(750//2+250//2),int(750//2+250//2)),(190), thickness=-1) #foreground its color is fixed
	cv.imshow("mesh", background)
	a+=5
	t.sleep(1)
	cv.rectangle(background, (100,50), (540,200), (30), thickness=-1)
	if cv.waitKey(20) & 0xFF==ord('d'):
		break
		

cv.destroyAllWindows()
	
	
	
