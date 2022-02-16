import imp
import cv2
import numpy as np

img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/temel_islemler/unnamed.jpg",0)  # neden yanına 0 koydum çünkü bu foto görüntülü ben bunda daha kolay işlem yapmak için gray çevirdim.
kernel=np.ones((5,5),np.uint8) #bunlar sayı şeklinde olacağından np.uint8 kullandık.
erosion=cv2.erode(img,kernel,iterations=5) #erode zaten erosion fiil hali demek.
#burada erode içinde o kernel yazmam zorunlu iterations'ı da kaç defa üstünden geçeceğini söylüyor.

cv2.imshow("ErosionYaptigimizFoto",erosion)

cv2.imshow("Foto",img)
#erosiondan başka dilation var o da kalınlaştırma anlamına geliyor.
dilation= cv2.dilate(img,kernel,iterations=5)
cv2.imshow("DILATIONFoto",dilation)
#opening kullanalım.
opening= cv2.morphologyEx(img,cv2.MORPH_CLOSE,kernel)
cv2.imshow("OPENINGFoto",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()