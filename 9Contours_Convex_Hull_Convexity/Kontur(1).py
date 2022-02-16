import cv2
from matplotlib.pyplot import contour, gray
import numpy as np

#zor bir şekildeki sınır çizgilerini(contours) bulmaya çalışıcaz.
img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/9Contours_Convex_Hull_Convexity.py/contour1.png")

#daha kolay işlem yapabilmek adına gray'e çeviricem resmi..

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#threshold işlemi yapıcam şimdide. yani resimleri öbeklendiricem yani sınıflara ayırıcam gibi düşün.

_,thres=cv2.threshold(gray,120,255,cv2.THRESH_BINARY)  #_ olan değişken fazla önem li bir mevzu olmadığı için fazla üstünde durmicaz.
#ilk parametrem yapacağım resmin, ikincisi min üçüncüsü maksimum son olarakta cv2.THRESH_BINARY fonk.'nu kullanıcam.
#binary 0 ve 1'lerden oluşan sistem.. herhangi bir renk geçişi yok demek.

contours,_=cv2.findContours(thres,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #üç tane değişkene ihtiyacım var. bu yüzden 1.-3. değişkenlerim _ olacak çünkü işime yaramıyor. 2. değişken ile işim var.
#girdiğim son iki argüman yaptığım threshold işlemini daha anlamlı bi hale getiriyor. 
#print(contours)

#peki bu bulduğumuz yukarıdaki noktalara çizim yapalım.
cv2.drawContours(img,contours,-1,(0,255,0),1) # burda ilk değişkenimiz resim değişkenimiz sonraki yapacağımız noktalar bu da zaten counturs'ların içinde tutuluyor.üçüncü parametremiz ise renkler sonraki de kalınlık.

cv2.imshow("Contour",img)
cv2.waitKey(0)
cv2.destroyAllWindows()