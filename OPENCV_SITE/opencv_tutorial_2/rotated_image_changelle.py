import numpy as np
import argparse
import imutils
import cv2

#argparse kullanıcaz
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image")

args=vars(ap.parse_args())

#load the image from disk

image=cv2.imread(args["image"]) #şimdi resmi args ve argpars' üzerinden çektik
image=cv2.resize(image,(640,480))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #görüntüyü daha iyi işlemek için gray çektik.
gray=cv2.GaussianBlur(gray,(3,3),0) #görüntüyü 3'e 3'lük kernel size ile yumuşattım.3.parametrem iterasyon
edged=cv2.Canny(gray,20,100) #canny'li kenarları tespit etmemde işime yarıyor.1.parametrem ise kullanacağım resim,2. ve 3.thresholdU(yani eşiklemek-sınıflandırmak demek)

#şimdi de kenarları saptamak için contours'larından faydalandık.
cnts=cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
#print(cnts)
#ensure ==emin olmak bir defa contour bulmak, contourlar ikili değer döndürüyor.
if len(cnts)>0:
    c=max(cnts,key=cv2.contourArea)
    mask=np.zeros(gray.shape,dtype="uint8") #burada 0'lardan oluşan bir alan oluşturduktan sonra gray'in en boy değerlerini aldım. sonra np.zeros uint8 ya da ufloat64 çevirecektim ben de 1cisine çevirdim.
    #şimdi contour çizme vakti.
    cv2.drawContours(mask,[c],-1,(0,255,255),-1)

    #şimdi ROI(region of interest) bakıcaz. ve mask uygulucaz.
    (x,y,w,h)=cv2.boundingRect(c) # Bunun için cv2.boundingRect() metodu ile kontur çerçeve noktalarını hesaplayıp cv2.rectangle() metoduyla etraflarına dikdörtgen çizebiliriz.
    imageROI=image[y:y+h,x:x+w]
    maskROI=mask[y:y+h,x:x+w]
    imageROI=cv2.bitwise_and(imageROI,imageROI,mask=maskROI) #ilk parametrem yapacağım resim iken, ikincisi mask yazdıracağım yer, 3'cüsü ise mask=mask literatürdür.

#şimdi döndürmeliyiz.Şimdi imutils.rotate ve imutils.rotate_bound
for angle in np.arange(0,360,15):
    rotated=imutils.rotate(imageROI,angle)
    cv2.imshow("Rotated(problematic) ",rotated)
    cv2.waitKey(0)

for angle in np.arange(0,360,15):
    rotated=imutils.rotate_bound(imageROI,angle)
    cv2.imshow("Rotated(Correct) ",rotated)
    cv2.waitKey(0)
cv2.destroyAllWindows()
