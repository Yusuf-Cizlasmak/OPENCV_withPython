#1 adımda güzel temiz bir görüntü elde etmiştik. Şimdi contourslarla yerini belirleyelim..

import cv2
import numpy as np
def findMaxContours(contours):#(3)
    max_i=0
    max_area=0
    for i in range(len(contours)):
        area_face=cv2.contourArea(contours[i])

        if max_area<area_face:
            max_area=area_face
            max_i=i
        try:
            c=contours[max_i]
        except:
            contours=[0]
            c=contours[0]
        
        return c


cap=cv2.VideoCapture(0)



while 1:
    ret,frame= cap.read()
    frame=cv2.flip(frame,1)
    roi=frame[100:300,250:450] #roi anlamı zaten region of interest yani ilgilenen alan anlamına geliyor..
    #frame[y1:y2,x1:x2] ilgili alan roi
    cv2.rectangle(frame,(250,100),(450,300),(0,255,255),0)
    hsv=cv2.cvtColor(roi,cv2.COLOR_BGR2HSV) #(2)
    lower_color= np.array([23,20,35],dtype=np.uint8)
    upper_color= np.array([66,255,255],dtype=np.uint8)

    mask=cv2.inRange(hsv,lower_color,upper_color)
    kernel=np.ones((3,3),np.uint8)
    mask=cv2.dilate(mask,kernel,iterations=1) # görüntüyü yayma ve genişletme işlemlerinde kullanılır.
    mask=cv2.medianBlur(mask,15)


    contours,_ =cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #bunu yaptıktan sonra yüzümüzün en sağ en sol ve köşelerini arıcaz.
    if len(contours)>0:
        try: #burada en büyük contours bulmak için bir fonksiyon tanımadık (3)
            c=findMaxContours(contours)

            extLeft= tuple(c[c[:,:,0].argmin()[0]])
            extRight= tuple(c[c[:,:,0].argmax()[0]])
            extTop= tuple(c[c[:,:,1].argmin()[0]])
            extBot= tuple(c[c[:,:,1].argmin()[0]])

            cv2.circle(roi,extLeft,5,(0,255,255),2)
            cv2.circle(roi,extRight,5,(0,255,255),2)
            cv2.circle(roi,extTop,5,(0,255,255),2)
            cv2.circle(roi,extBot,5,(0,255,255),2)
            #peki yüzümün kenarlarını birleştiren bir çokgen çizelim.
            cv2.line(roi,extTop,extRight,(0,255,255),2)
            cv2.line(roi,extRight,extBot,(0,255,255),2)
            cv2.line(roi,extBot,extLeft,(0,255,255),2)
            cv2.line(roi,extLeft,extTop,(0,255,255),2)
        except:
            pass
    else:
        pass
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)

    cv2.imshow("ROI",roi) #I DID IT !
    #şimdi görüntümü hsv formatına çeviricem ama frame'i değil bak ROI çeviricem.(2)
    if cv2.waitKey(15) & 0XFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()