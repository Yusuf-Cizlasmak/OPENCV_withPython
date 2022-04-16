import cv2
import argparse
import numpy as np          #kütüphane import etme.
import imutils

ap=argparse.ArgumentParser() #ap değişkenini Arguman Biçimleyici ve bölücü olan bir fonksiyona eşitliyoruz.
ap.add_argument("-i","--input",required=True,help="path to input image")    #argparse yarıdmıyla dosya yolu incelemeden direkt buradan çağırabiliyoruz.

args=vars(ap.parse_args()) #aldığı dosyaları yolunu kullanabileceğimiz hale getiriyor,parçalıyor.

#load the input image disk
image=cv2.imread(args["input"])  

output=image.copy() #burada image kopyaladık
cv2.putText(output,"OpenCv+Text",(10,25),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,255),2) #ilk parametrem işlenecek resim,2. yazıalacak şey,3. yazıalacak alan,yazı tipi(font) olarak düşünülebilir,4.font için bir değer, 5. renk,6. kalınlık.
#neden font_hershey_simplex kullandığımızın kanıtı = https://docs.opencv.org/3.4.1/d0/de1/group__core.html#ga0f9314ea6e35f99bb23f29567fc16e11

cv2.imshow("Text ", output)
cv2.waitKey(0)
