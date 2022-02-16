import cv2
import numpy as np
from pytest import approx
#contourları kullanıp köşeleri bulup ona göre sınıflandırma yapıcaz.
font = cv2.FONT_HERSHEY_SIMPLEX 
font = cv2.FONT_HERSHEY_COMPLEX 

img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/11Alistirmalar_1/polygons.png")
#bunu da contour aramam için ilk önce gray'e sonra da threshold uygulamam lazım.

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,threshold =cv2.threshold(gray,240,255,cv2.THRESH_BINARY) #öndeki _'nin sadece ikili değer döndürdüğünden dolayı aldık.

contours,_= cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

#burda countours'lara daha çok yaklaşmak için cv2.approxPolyDP fonksiyonunu kullanıyorduk.

for cnt in contours:
    epsilon=0.01*cv2.arcLength(cnt,True)
    approx= cv2.approxPolyDP(cnt,epsilon,True) #approx zaten türkçe karşılığı yaklaşma demek.
    
    cv2.drawContours(img,[approx],0,(0),5)

    x= approx.ravel()[0]
    y=approx.ravel()[1]             #approx.ravel koordinatlarına göre x ve y'e eşitledim.

    #approx ne olup olmadığına bakmak fikir sahibi olabiliriz. 
    #print(approx) yazabilirsin 2'li sayılar çıkacaktır.
    #hatta  print("x: ",x)
    #print("y: ",y)
    #print(len(approx))


    if len(approx)==3:
        cv2.putText(img,"Triangle",(x,y),font,1,(0))
    elif len(approx)==4:
        cv2.putText(img,"Rectangle",(x,y),font,1,(0))
    elif len(approx)==5:
        cv2.putText(img,"Pentagon",(x,y),font,1,(0))
    elif len(approx)==6:
        cv2.putText(img,"Hexagon",(x,y),font,1,(0))
    else:
        cv2.putText(img,"Ellipse",(x,y),font,1,(0))


cv2.imshow("contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()