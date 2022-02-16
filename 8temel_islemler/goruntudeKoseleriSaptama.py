import cv2
from matplotlib.pyplot import gray
import numpy as np

img = cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/unnamed.jpg")
img1 = cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/contour.png")

#daha kolay işlem yapmak için resimleri 'gray'e çevirdik.(sonradan not float32 çevirmem gerekiyormuş contour'leri yapabilmek için)
gray= cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
gray=np.float32(gray)
#şimdi yeni bir fonksiyonu bulucaz.köşeleri saptamak için.

corners= cv2.goodFeaturesToTrack(gray,50,0.01,500) #ikinci parametre max köşe sayısı.üçüncü kalitesi 0.01 değeri kabul edildi, son parametre ise köşeler arasındaki uzaklıktır.
#bunu yapmamız için bir ufak değişiklik yapmamız lazım. corners'ı yine integer tipine dönüştürmem gerekiyor.çemberler çizerken float'lı sayılar kullanamayız.o yüzden integr kullanıyoz.
corners= np.int0(corners)
#şimdi bu corner verilerini çekmesi için döngüye alıcam.
for corner in corners:
    x,y= corner.ravel()  #bunu yapmamamın sebebi aldığım tek bi satıra dökebilmek. 
    cv2.circle(img1,(x,y),3,(255,255,255),-1)

cv2.imshow("CORNER",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()