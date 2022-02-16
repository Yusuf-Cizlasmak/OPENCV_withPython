import cv2
from cv2 import rectangle 
import numpy as np
#ağırlıklı toplamaya olan bakışımız f(x,y)=x*a+y*b+c şeklinde olacaktır.
circle= np.zeros((512,512,3),np.uint8) +255 #burada boş bir tuval oluşturduk hemde beyaz 
cv2.circle(circle,(256,257),60,(255,0,0),-1) #ilk değişkenimiz tuvalin neresinde olduğu,çapı, sonraki rengi ve en son olan içinin dolu mu boş mu onu gösteriyor. 
#şimdi aynısını
rectangle=np.zeros((512,512,3),np.uint8) +255
cv2.rectangle(rectangle,(150,150),(350,350),(0,255,0),-1) #ilk tuvalin neresinde olacağı, ikincisi uzun kenar aralığı diğeri kısa kenar aralıkları olacaktır.
#resimleri toplamak için cv2.add fonksiyonunu kullanıcam.

add=cv2.add(circle,rectangle)
print(add[256,257])

cv2.imshow("Circle",circle)
cv2.imshow("rectangle",rectangle)
cv2.imshow("add",add) #işte bu şekilde cyan renginde bir dikdörtgen ve bir daire şeklinde elde etmiş olduk.


cv2.waitKey(0)
cv2.destroyAllWindows()