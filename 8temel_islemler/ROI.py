import cv2
import numpy as np

#roi açılımını --> region of interest--> ilgi alanı demektir.

img=cv2.imread("C:/Users/yusuf/Desktop/unnamed.jpg") # çalışacağım resmi dahil ettim.
print(img.shape[:2])

roi=img[50:100,133:316] #x ekseni ile y ekseni arasında taradığım bölgeleri gösteriyor.

cv2.imshow("Ana De Armas",img)#bu da göstereceğim pencerenin adı ve değişkeni
cv2.imshow("Roi ile taradığım alan",roi)#bu da göstereceğim pencerenin adı ve değişkeni
cv2.waitKey(0)
cv2.destroyAllWindows()