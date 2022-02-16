import cv2
from cv2 import arcLength
from matplotlib.pyplot import hsv
import numpy as np
from pytest import approx
from tblib import Frame

cap= cv2.VideoCapture(0) #kameradan görüntüyü aldık.
font =cv2.FONT_HERSHEY_COMPLEX 
font1 =cv2.FONT_HERSHEY_SIMPLEX 


def nothing(x): #trackbar yapmak için yine boş bir fonksiyon uyguluyorum.
    pass
cv2.namedWindow("Trackbar")

cv2.createTrackbar("Lower-Hue","Trackbar",0,180,nothing)
cv2.createTrackbar("Lower-Saturation","Trackbar",0,180,nothing)
cv2.createTrackbar("Lower-Value","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper-Hue","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper-Saturation","Trackbar",0,180,nothing)
cv2.createTrackbar("Upper-Value","Trackbar",0,180,nothing)

while(True):
    ret,frame= cap.read()
    #flipcode = 0: flip vertically
    #flipcode > 0: flip horizontally
    #flipcode < 0: flip vertically and horizontally
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_h=cv2.getTrackbarPos("Lower-Hue","Trackbar")
    lower_s=cv2.getTrackbarPos("Lower-Saturation","Trackbar")
    lower_v=cv2.getTrackbarPos("Lower-Value","Trackbar")
    upper_h=cv2.getTrackbarPos("Upper-Hue","Trackbar")
    upper_s=cv2.getTrackbarPos("Upper-Saturation","Trackbar")
    upper_v=cv2.getTrackbarPos("Upper-Value","Trackbar")

    lower_color=np.array([lower_h,lower_s,lower_v])
    upper_color=np.array([upper_h,upper_s,upper_v])


    mask=cv2.inRange(hsv,lower_color,upper_color)
    #şimdi erozyon'da yaptıktan sonra(2) countours'leri bulucam.

    contours,_=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area= cv2.contourArea(cnt)
        epilson=0.02*arcLength(cnt,True)
        approx= cv2.approxPolyDP(cnt,epilson,True)
        

        x=approx.ravel()[0] #approx çok boyutlu bir dizi ise tek boyutluya çeviriyor.
        y=approx.ravel()[1]

        #eğer çok küçük alanlara takılmamak adına area bir standart getiriyorum.
        if area >400:
            cv2.drawContours(frame,[approx],0,(0,255,0),5)
            if len(approx)==3:
                cv2.putText(frame,"UCGEN",(x,y),font,1,(0,0,0))
            elif len(approx)==4:
                cv2.putText(frame,"dortgen",(x,y),font,1,(0,0,0))
            elif len(approx)==5:
                cv2.putText(frame,"besgen",(x,y),font,1,(0,0,0))
            else:
                cv2.putText(frame,"elips",(x,y),font,1,(0,0,0))
    #bir kernel oluşturucam burada.
    kernel=np.ones((5,5),np.uint8)
    mask= cv2.erode(mask,kernel)#2

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    

    if cv2.waitKey(20)& 0xFF==ord('q'):#0XFF q'nun makine dilinde karşılığıdır.
        break 

cap.release()
cv2.destroyAllWindows()