from re import template
import cv2
import numpy as np
image_path="C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/starwars1.jpg"
template_path="C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/starwars2.jpg"
img= cv2.imread(image_path)

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

img1= cv2.imread(template_path,cv2.IMREAD_GRAYSCALE) #virgül 0 gray'li gösterirken ,1 ise olduğu gibi gösterecektir.
w,h=img1.shape[::-1]
result=cv2.matchTemplate(gray_img,img1,cv2.TM_CCOEFF_NORMED) #matchTemplate fonksiyonu ile görüntünün parçasını bulucak.3.parametre
location=np.where(result >=0.95) #result sayıyı arttıkça doğru noktaya yaklaşıyoruz.
#print(location) # zor bi veri verdi biraz daha düzenlemem gerekiyor.

for point in zip(*location[::-1]): #normalde -1 yazmasaydım yükseklik ve genişliği alıyordu ben bu durumu tam tersine çevirdim.
    print(point) 
    cv2.rectangle(img,point,(point[0]+w,point[1]+h),(0,255,0),3)

cv2.imshow("kafa",img) #istenilen sonuç işte bu  arada.
cv2.imshow("Sonuc",result)


cv2.waitKey(0)
cv2.destroyAllWindows()