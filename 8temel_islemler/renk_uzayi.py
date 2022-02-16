import imp


import cv2

img = cv2.imread("C:/Users/yusuf/Desktop/unnamed.jpg")
#görüntülerin renk uzaylarını değiştirdiğimiz fonksiyon cv2.cvtColor'dır. İlk kaynak resmi,ikincisi neyden neye dönüştürücem.
imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
imgGray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imshow("ana de armas BGR",img)
cv2.imshow("ana de armas RGB",imgRGB)
cv2.imshow("ana de armas HSV",imgHSV)
cv2.imshow("ana de armas GRAY",imgGray)
cv2.waitKey(0)
cv2.destroyAllWindows()

#genellikle gray temalı fotoları kullanıcaz çünkü renkli resimler 3 katmanlıdır veya onları düzenlemek ve işlemek gerçekten zaman alır.
#Gray temalı fotolar tek katmanlı olduğundan işimizi kolaylaştırır.