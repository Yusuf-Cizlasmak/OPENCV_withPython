import cv2
import numpy as np  

imgFilter= cv2.imread("C:/Users/yusuf/Desktop/filter1.png")
imgMedian= cv2.imread("C:/Users/yusuf/Desktop/median1.png") #daima parantezin içinde yazılacak bu imshow ettiğimiz adres.
imgBilateral= cv2.imread("C:/Users/yusuf/Desktop/bilateral.png")

#bir kernel oluşturmamız gerekiyor. onun içinde blur şeklinde bir değişken oluşturmamız gerekiyor.

blur= cv2.blur(imgFilter,(9,9))#burada kernel pozitif tek sayı olması gerekiyor. #ilk index değişkenim.. ikincisi de kernel büyüklüğü.
blur2= cv2.GaussianBlur(imgFilter,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("blur",blur)
cv2.imshow("original",imgFilter)
cv2.imshow("original",blur2)


#şimdi de median için yapalım.
blurM= cv2.medianBlur(imgMedian,3)
cv2.imshow("median",blurM)
#şimdi o halı için
blurB= cv2.bilateralFilter(imgBilateral,9,95,95)
cv2.imshow("bila",blurB)

cv2.waitKey(0)
cv2.destroyAllWindows()