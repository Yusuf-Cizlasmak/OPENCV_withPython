import cv2 
import numpy as np

img1= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/bitwise_1.png")
img2= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/bitwise_2.png")

bitAnd= cv2.bitwise_and(img2,img1) #siyah ile beyazı karşılaştırıyoruz şuan ve bağlacı ile
bitOr= cv2.bitwise_or(img2,img1)#siyah ile beyazı karşılaştırıyoruz şuan veya bağlacı ile
bitNot= cv2.bitwise_not(img2)
cv2.imshow("BitAnd",bitAnd)
cv2.imshow("BitOr",bitOr)
bitNot= cv2.bitwise_not(img2)
cv2.imshow("imgnot",bitNot)
cv2.waitKey(0)
cv2.destroyAllWindows()

#burada ogrenmen gereken 1'in = beyaz
#0 ise siyah olduğudur. eğer ben bitwise ile resimleri 've' bağlacı ile birleştiğimde 0 olacaktır bazı yerler yukarıda da onları bulduk.

#peki ya böyle bir resmin tersini nasıl alabiliriz. ?
#tabii ki de bitwise.not komutuyla.

