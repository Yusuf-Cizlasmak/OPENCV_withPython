#gerekli kütüphaneleri import ediyoruz.

import imutils
import cv2

#dosya çekiyoruz..
image=cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV_SITE/basic_things/jp.jpg")
resized=cv2.resize(image,(200,200))
#şuan görüntünün şekilleri alıyoruz.
(h,w,d)=image.shape
print("width={}","height={}","depth={}".format(w,h,d))

#x'De 100 ve y'de 50 renk değerlerini aldık.
(B, G, R) = image[100, 50]
print("R={}, G={}, B={}".format(R, G, B))

#şimdi de region of image (ilgi alanı)

roi=image[60:160,320:420]


resized=imutils.resize(image,width=300)# burada imutils fonksiyon resize ile width veya height aynı görevi görüyor.

#hadi biraz 45 derece döndürelim..
center=(w//2,h//2)
M=cv2.getRotationMatrix2D(center,-45,1.0)#birinci parametrem nereden çevireceğim,ikinci hangi yöne doğru olduğu, üçüncü parametrem ise ölçek oluyor.
rotated=cv2.warpAffine(image,M,(w,h))

rotated=imutils.rotate_bound(image,45) #rotate bound görüntüyü bozmadan döndürür.

#daha da pürüzleşirtiriz.

blurred=cv2.GaussianBlur(image,(11,11),0) #ve bulanıklaştırdık.
cv2.imshow("Blureed",blurred)


cv2.imshow("OpenCv rotation",rotated)
cv2.imshow("resized",resized)
cv2.imshow("roi",roi)
cv2.imshow("Image",image)
cv2.waitKey(0)
