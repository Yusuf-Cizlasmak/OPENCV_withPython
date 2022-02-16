import cv2
from cv2 import circle
import numpy as np


img1 = cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/oguzay.jpeg")
img1=cv2.resize(img1,(640,480))

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)

img1_blur= cv2.medianBlur(gray1,5)

circles= cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/5,param1=10,param2=27,minRadius=40,maxRadius=50)
#parametrelere dikkat hocam. ilk parametrem en son işlem yaptığım değişkenim,sonraki bir fonksiyon, 3.parametre ise çözünürlük (1), 4. parametre minimum mesafe çemberler arasında burası önemli fazla ve azı da zarar o yüzden bu jargonu kullan img.shape[0]/64
#değerlerle oynarak sağlıklı bi sonuç elde edilebilir
if circles is not None:
    circles= np.uint16(np.around(circles)) #girdiğimiz değeri maksimum değeri artırmak veya azaltmaktır.
    #circles içindeki değerleri yuvarlayıp tekrar circlesa kaydediyoruz
    for i in circles[0,:]:
         cv2.circle(img1,(i[0],i[1]),i[2],(255,0,0),2)
         cv2.putText(img1,"+",(i[0],i[1]),cv2.FONT_HERSHEY_SIMPLEX,0.6,(0,255,255),2)
cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()