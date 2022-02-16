import cv2
import numpy as np

cap=cv2.VideoCapture(0)


while 1:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[100:300,250:450] #roi anlamı zaten region of interest yani ilgilenen alan anlamına geliyor..
    #frame[y1:y2,x1:x2] ilgili alan roi
    cv2.rectangle(frame,(250,100),(450,300),(0,255,255),2)
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV) #(2)
    lower_color= np.array([23,20,35],dtype=np.uint8)
    upper_color= np.array([66,255,255],dtype=np.uint8)

    _,contours= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

    mask=cv2.inRange(hsv,lower_color,upper_color)
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1) # görüntüyü yayma ve genişletme işlemlerinde kullanılır.
    mask=cv2.medianBlur(mask,15)


    

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    cv2.imshow("ROI",roi) #I DID IT !
    #şimdi görüntümü hsv formatına çeviricem ama frame'i değil bak ROI çeviricem.(2)
    if cv2.waitKey(15) & 0XFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()