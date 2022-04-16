#gerekli kütüphaneleri import ediyoruz.
from cv2 import contourArea
import imutils
import cv2

#resimleri çektikten sonra işlemleri yapmak grayscale ve blur'lamak mevzu.

image=cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV_SITE/finding_contours/El1.jpg")
#image=cv2.resize(image,(640,480))
gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(5,5),0) #gaussinBlur fonksiyonumun ilk parametrem üstünde işleyeceğim resim, ikincisi kernel boyutlarım, sonuncusu sigmax değerim.

#aşağıdaki uygulacağımız dilation(Genişleme) ve erozyon fonksiyonları aşağıdaki,
#Erozyon işlemi ön taraftaki nesnenin sınırlarını aşındırmayı sağlar.
thresh=cv2.threshold(gray,45,255,cv2.THRESH_BINARY)[1]
thresh=cv2.erode(thresh,None,iterations=2)
thresh=cv2.dilate(thresh,None,iterations=2)

#contour'ları bulucaz ve en büyük contour'u alıcaz.
cnts=cv2.findContours(thresh.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts=imutils.grab_contours(cnts)
c=max(cnts,key=contourArea)

#contour'ların en uç noktalarına bakarız.
extLeft=tuple(c[c[:,:,0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])

#nesneler dışlarını çizmek için en uç noktalara ihtiyacımız vardır.

cv2.drawContours(image,[c],-1,(0,255,255),2)
cv2.circle(image,extLeft,8,(0,0,255),-1)
cv2.circle(image,extRight,8,(0,255,0),-1)
cv2.circle(image,extTop,8,(0,255,0),-1)
cv2.circle(image,extRight,8,(0,255,0),-1)

cv2.imshow("Image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()

