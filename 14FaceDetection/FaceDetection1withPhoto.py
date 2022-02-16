import cv2
from scipy.misc import face

img=cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/14FaceDetection/face.png")
#şimdi de cascade dosyasını çalışmamıza dahil edelim. bunu da cv2.CascadeClassifier() hallediyorum.
face_cascade=cv2.CascadeClassifier("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/14FaceDetection/frontalface.xml.xml")

#resimde daha iyi oynama yapmak için gray'e çeviricez.

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces= face_cascade.detectMultiScale(gray,1.3,6)  #face_cascade.detecetMultiScale yazmamın nedeni yukarıdaki değişkende tutmamdır.
#2.parametrem ise ölçeklendirme (ne kadar küçültücem ) 3.parametrem belirli bir alanda girilen sayı kadar pencere  bulsun. faces bize tuple olarak değerleri saklıcak şimdi.
#yüzün üstünde bir dikdörtgen çizmek istiyorum. bunun için for döngüsü kurmam lazım.
#Eğer iki yüzden fazla algılarsa 3.parametreyi değiştir.
for(x,y,w,h) in faces:
     cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2) #x demek sağ koordinat demek w demek ise genişlik demek.y demek ise aşağı koordinat demek ve ben ona h (yükseklik) ekliyorum.

cv2.imshow("Sonuc",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
