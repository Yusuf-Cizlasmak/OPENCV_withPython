import argparse

from numpy import imag
import imutils
import cv2
# construct the argument parser and parse the arguments

ap=argparse.ArgumentParser() #ap değişkenini Arguman Biçimleyici ve bölücü olan bir fonksiyona eşitliyoruz.
ap.add_argument("-i","--input",required=True,help="path to input image")    #argparse yarıdmıyla dosya yolu incelemeden direkt buradan çağırabiliyoruz.
ap.add_argument("-o","--output",required=True,help="path to output image")


args=vars(ap.parse_args()) 
#şimdi diskten dosyayı çekicez.
image=cv2.imread(args["input"])

#şimdi daha rahat işlem yapmak adına bazı işlemler uygulucaz -gray--blur--thres gibi
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
blurred=cv2.GaussianBlur(gray,(5,5),0) #burada görüntüyü blurladık
thresh=cv2.threshold(blurred,60,255,cv2.THRESH_BINARY)[1] #görünyü tam öbekleştirdik.

#şimdi de contours'leri (kenarları) arıcaz 

cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)#ilk parametrem thres'ten aldığı değerleri copyleyerek resimde işleyecek. Diğeri iki parametrem ise daha iyi contour aramak için.. bir jargon olarak kabul edebilriz.
cnts=imutils.grab_contours(cnts)

for c in cnts:
    cv2.drawContours(image,[c],-1,(0,244,255),2)
#üstüne yazı yazdırmak için aşağıdaki fonksiyonu kullandım.
text = "I found {} total shapes".format(len(cnts))
cv2.putText(image,text,(10,20),cv2.FONT_HERSHEY_SIMPLEX,0,5,(255,0,0),2)
cv2.imwrite(args["output"],image)


cv2.destroyAllWindows()



