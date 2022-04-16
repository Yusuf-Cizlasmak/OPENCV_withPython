from matplotlib import image
import numpy as np
import cv2
import imutils
import argparse


ap=argparse.ArgumentParser() #ap değişkenini Arguman Biçimleyici ve bölücü olan bir fonksiyona eşitliyoruz.
ap.add_argument("-i","--input",required=True,help="path to input image")    #argparse yarıdmıyla dosya yolu incelemeden direkt buradan çağırabiliyoruz.

args=vars(ap.parse_args()) #aldığı dosyaları yolunu kullanabileceğimiz hale getiriyor,parçalıyor.

#load the input image disk
image=cv2.imread(args["input"])
resized=cv2.resize(image,(200,200))
(h,w,d)=image.shape

for angle in np.arange(0,360,15):
    rotated=imutils.rotate_bound(image,angle) #rotate bound görüntüyü bozmadan döndürür.ikinci parametrem kaç derece döndürdüğünü gösteririr.
    cv2.imshow("ss",rotated)
    cv2.waitKey(0)
cv2.destroyAllWindows()