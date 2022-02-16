import cv2
from cv2 import circle
import numpy as np


img1 = cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/10HoughDonusumleri/coins.jpg")
img2 = cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/10HoughDonusumleri/balls.jpg")

gray1=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray2=cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

img1_blur= cv2.medianBlur(gray1,5)
img2_blur= cv2.medianBlur(gray2,5)

circles= cv2.HoughCircles(img1_blur,cv2.HOUGH_GRADIENT,1,img1.shape[0]/3,param1=200,param2=10,minRadius=40,maxRadius=90)
#parametrelere dikkat hocam. ilk parametrem en son işlem yaptığım değişkenim,sonraki bir fonksiyon, 3.parametre ise çözünürlük (1), 4. parametre minimum mesafe çemberler arasında burası önemli fazla ve azı da zarar o yüzden bu jargonu kullan img.shape[0]/64
#değerlerle oynarak sağlıklı bi sonuç elde edilebilir
if circles is not None:
    circles= np.uint16(np.around(circles)) #girdiğimiz değeri maksimum değeri artırmak veya azaltmaktır.
    #circles içindeki değerleri yuvarlayıp tekrar circlesa kaydediyoruz
    for i in circles[0,:]:
         cv2.circle(img1,(i[0],i[1]),i[2],(255,0,0),2)

cv2.imshow("img",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()