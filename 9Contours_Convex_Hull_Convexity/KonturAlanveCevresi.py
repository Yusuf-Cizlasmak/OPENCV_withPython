import cv2

img = cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/9Contours_Convex_Hull_Convexity/contour.png")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #daha kolay işlem yapabilmek adına gray'e çevirim görüntüyü 
#şimdi de threshold fonksiyonu ile görüntüyü sınıflandırıcam(öbeklere).
ret,thresh= cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
#şimdi de kontor bulmak için contours diye bir değişken tanımladım. _ değişkeni hiç bir yerde kullanmayacağım için bir özelliği yok şuan.
contours,_= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#şimdi de moments değerleri almak için m değişkeni oluşturuyorum.

cnt=contours[0]
area= cv2.contourArea(cnt) #burada area ile ilgili bir hesaplama yapıp bana geri dönüş yapıyor. fonksiyonun amacı da bu zaten.
print(area)
M=cv2.moments(cnt)
print(M["m00"]) #aaaa burada ikisinde de aynı değer çıkacak ikisi de alan buluyormuş he
#şimdi de çevreyi bulucaz.

perimeter =cv2.arcLength(cnt,True) #önemli bi fonks.
#true yazmamın neden şekil kapalıysa devam et gibisinden bişey aslında.
print(perimeter)
""""
cv2.imshow("ILK OLAN",img)
cv2.imshow("GRAY OLAN",gray)
cv2.imshow("THRESH OLAN",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""