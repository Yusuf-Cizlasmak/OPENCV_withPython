import cv2
import numpy as np

img1= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/aircraft.jpg")

img2= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/aircraft1.jpg")


img1=cv2.resize(img1,(480,640))
img2=cv2.resize(img2,(480,640))

img3=cv2.medianBlur(img1,7)
if img1.shape==img2.shape:
    print("aynı boyuttadır--Same Size")
else:
    print("Not today, not same")


diff=cv2.subtract(img1,img3) #subtract fonksiyonu iki resmi karşılaştırır.eğer simsiyah çıkarsa bir fark yoktur.
b,g,r=cv2.split(diff)
print(b)
if cv2.countNonZero(b)==0 and cv2.countNonZero(g)==0 and cv2.countNonZero(r)==0: # eğer siyah olmayan varsa. buradan farklı olan yerleri bulabilirim.şimdi bi karar yapısı oluşturucam.
    print("this images are completely same.") 
#peki ben renkleri bulabilir miyim ? evet. cv2.countNonZero fonksiyonu ile
else:
    print("this images aren't same")
cv2.imshow("difference",diff)
cv2.waitKey(0)
cv2.destroyAllWindows()
#sayısal değerleri eşitse (pikselleri karşılaştırıcaz yani) eşitse aynıdır.
