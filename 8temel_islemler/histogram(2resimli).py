import cv2
import numpy as np
from matplotlib import pyplot as plt


img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/unnamed.jpg")
b,g,r=cv2.split(img)
#burada brg'ların tek tek histogramlarını göreceğiz.
cv2.imshow("Ana de Armas",img)

plt.hist(b.ravel(),256,[0,256]) #ilkisi bilmememiz gereken bir fonk. ikincisi max value. 3'cüsü ise değer aralıkları şeklinde düşünebiliriz aslında.
plt.hist(g.ravel(),256,[0,256]) #ilkisi bilmememiz gereken bir fonk. ikincisi max value. 3'cüsü ise değer aralıkları şeklinde düşünebiliriz aslında.
plt.hist(r.ravel(),256,[0,256]) #ilkisi bilmememiz gereken bir fonk. ikincisi max value. 3'cüsü ise değer aralıkları şeklinde düşünebiliriz aslında.
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

#mavi maviyi temsil ederken, turuncu yeşili,yeşil ise kırmızıyı temsil eder histogramda.