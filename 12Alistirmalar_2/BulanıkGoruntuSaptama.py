import cv2

img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/starwars.jpg")
#resmi bulanıklıştırma.
blurry_img=cv2.medianBlur(img,7) #(2) 7--> 9 eğer ben  kerneli arttırsam laplacian değerini düşürmüş olurum.

#şuan yeni bir fonksiyon öğrenicez. bu sayede fotoğrafın blur'lu olup olmadığını cv2.Laplacian fonk. öğrenicez.
laplacian =cv2.Laplacian(blurry_img,cv2.CV_64F).var() #şuan burası bana bir değer döndürücek.
#laplacian1 =cv2.Laplacian(img,cv2.CV_64F).var() #şuan burası bana bir değer döndürücek.
print(laplacian) #output: 317.9994595426443
#print(laplacian1) output:900.5680561195056

if laplacian< 500:
    print("bluury image")
""""
cv2.imshow("img",img)
cv2.imshow("Blurlu IMG",blurry_img)

cv2.waitKey(0)
cv2.destroyAllWindows()""" 