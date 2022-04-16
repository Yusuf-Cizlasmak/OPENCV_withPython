# bu kodularda şekillerin merkezlerini bulup, contourlarını bulacağız.

import argparse
import imutils
import cv2

ap= argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the input image")
args=vars(ap.parse_args())

#şimdi de resmi çekip,grayleyip, blur'dan, sonra threshold..

image=cv2.imread(args["image"])
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0) #blur'lacağım ilk paramatrem,ikini kernel size , sigMax paramtrem.
thresh=cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1]

cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #thresCopy'ın yazmamızın işleneceğimiz fotoğraf, diğeri iki parametrem ise literatür..
cnts=imutils.grab_contours(cnts)

#contours'leri işlemek için for döngüsü kuruyoruz.

for c in cnts:
    #contours'ların ortasını bulmak için..
    M=cv2.moments(c)
    cX=int(M["m10"]/ M["m00"])
    cY=int(M["m01"]/ M["m00"])

    #şimdide contours'ların tam ortasını bulmak için  contoursları çizip- yazdıracaam.
    cv2.drawContours(image,[c],-1,(255,0,255),2)
    cv2.circle(image, (cX,cY),7,(255,255,14),-1) #ikinci parametrem centre of circle,
    cv2.putText(image,"center",(cX-20,cY-20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(84,46,81),2)

    cv2.imshow("IMAGE",image)
    cv2.waitKey(0)