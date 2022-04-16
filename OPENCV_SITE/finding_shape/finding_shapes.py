import argparse
import cv2
import imutils
import argparse
import numpy as np


#argparse_Parser ile terminalde python dosyası--key--value şeklinde gidecektir.

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to the image file")
args=vars(ap.parse_args())

#load the image

image=cv2.imread(args["image"]) #resmi yükledikten sonra args içine key yazılır.

#bütün siyah şekilleri bulmak için resimdeki aşağıdaki şeyleri uygularız.
lower=np.array([0,0,0])
upper=np.array([15,15,15])
shapeMask=cv2.inRange(image,lower,upper)

#şimdi de contour'leri bulmak için..

cnts=cv2.findContours(shapeMask.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #ilk değişken contour'lerin bulunacağı , ikinci ve üçüncü parametrem daha iyi contour bulması için..

cnts=imutils.grab_contours(cnts)

print("I found {} black shape".format(len(cnts)))
cv2.imshow("mask",shapeMask)
#countours'ları bulmak için.
for c in cnts:
    cv2.drawContours(image,[c],-1,(0,255,0),2)
    cv2.imshow("Image",image)
    cv2.waitKey(0)

cv2.destroyAllWindows()
