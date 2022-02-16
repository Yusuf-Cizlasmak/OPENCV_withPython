
import cv2
import numpy as np
from matplotlib import pyplot as plt

#resimleri öbeklendiricem. yani ayırıcaz sınıflara gibi düşünebilirsin.

img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/unnamed.jpg",0)#yine kolay işlem yapmak için görüntüyü gray'e çevirdim.
#burada iki değişken kullanmak zorundayız.birisi ret diğeri de threshold dediğimiz değişken. ret== return'den geliyor bu arada.
ret,th1= cv2.threshold(img,50,155,cv2.THRESH_BINARY) #img girdikten sonra threshold değerlerimizi giriyoruz ikinci olarak 255 bizim en yüksek threshold değerimizi gösteriyor.
#peki başka bir threshold yöntemi de bakalım bunlar opencv kılavuzdan bakabilirsiniz.
th2=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
cv2.imshow("PencereminAdi",img)
cv2.imshow("ThresHoldUygulanan",th1)
cv2.imshow("ThresHold2Uygulanan",th2)

cv2.waitKey(0)
cv2.destroyAllWindows() 