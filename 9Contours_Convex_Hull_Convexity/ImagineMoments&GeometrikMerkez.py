import cv2

img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/9Contours_Convex_Hull_Convexity/contour.png")
#yapacağımız işlem için ilk önce gray'e çeviricez.

gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#şimdi de bu resmi thres'licez yani sınıflara ayırıcaz(öblendiricez.)

ret,thresh= cv2.threshold(gray,127,255,cv2.THRESH_BINARY)#ilk parametrem yapacağım resmin, ikincisi min üçüncüsü maksimum son olarakta cv2.THRESH_BINARY fonk.'nu kullanıcam.
#binary 0 ve 1'lerden oluşan sistem.. herhangi bir renk geçişi yok demek.


#şimdi de moments diye ilk defa kullanacağımız bir fonk. var aslında.

M=cv2.moments(thresh)
x=int(M["m10"]/M["m00"])  #üçgenin ağırlık merkezi bulunurken X değeri m10/m00 dır
y=int(M["m10"]/M["m00"])#üçgenin ağırlık merkezi bulunurken Y değeri m01/m00 dır


#ağırlık merkezini bulmak için bir circle çizicem.
cv2.circle(img,(x,y),5,(0,255,255),-1)
print(x)

cv2.imshow("PencereIsmi",img)
cv2.waitKey(0)
cv2.destroyAllWindows()