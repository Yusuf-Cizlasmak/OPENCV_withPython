
from skimage import exposure
import numpy as np
import argparse             #gerekli kütüphaneleri import ettik.
import imutils
import cv2

ap=argparse.ArgumentParser()
ap.add_argument("-q","--query",required=True,help="Path to the query image") # 
args=vars(ap.parse_args())

#dosyayı çekip boyutlarını ve resize'ladık. 

image=cv2.imread(args["query"])
ratio=image.shape[0] /300.0
orig=image.copy
image=imutils.resize(image,height=300)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.bilateralFilter(gray,11,17,17) #GauusuanBlur ve MedianBlur birleştirilmiş hali birazca görüntüyü hafifleştiriyor.
edged=cv2.Canny(gray,30,200)

cnts=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:10]
screenCnt=None

#contour'ları döndürüyorz.
for c in cnts:
    #yaklaşık contouru bulmak.aşağıdaki fonksiyonlarda o işe yarıyor.
    peri=cv2.arcLength(c,True)                  
    approx=cv2.approxPolyDP(c,0.015*peri,True) 

    if len(approx)==4: 
        screenCnt=approx
        break

cv2.drawContours(image,[screenCnt],-1,(0,255,0),3)
cv2.imshow("Game Boy Screen",image)
cv2.waitKey(0)


