#biz bazen yaptığımız contour'leri şekli çevrelesin istemiyoruz. sadece bir örtü gibi dursun istiyoruz. işte o gibi durumlarda convexHull'u kullanıyoruz.

import cv2
from cv2 import threshold
import numpy as np

img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/9Contours_Convex_Hull_Convexity/map.jpg")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#şimdi şekli yumuşatıcam blur'la.
blur= cv2.blur(gray,(3,3)) #2.parametrem kernel değerim oluyor.
#son olarak da thresh'liyip binary çevirme işlemini bitiriyorum.
ret,thresh= cv2.threshold(blur,39,255,cv2.THRESH_BINARY)

contours,hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

hull=[] #şuan boş bir dizi oluşturup counturs'lardan oluşan indexleri de buraya atıcam.

for i in range(len(contours)):
    hull.append(cv2.convexHull(contours[i],False))
    #şimdi çizimlerimi boş tuvale çizmem lazım.

bg=np.zeros((thresh.shape[0],thresh.shape[1],3),np.uint8) # burada boş bir 

for i in range(len(contours)):
    cv2.drawContours(bg,contours,i,(0,0,255),3,8) #8 kesintisiz çizgiyi gösterir.
    cv2.drawContours(bg,hull,i,(255,0,0),1,8) #8 kesintisiz çizgiyi gösterir.


cv2.imshow("orjinial",bg)

cv2.waitKey(0)
cv2.destroyAllWindows()