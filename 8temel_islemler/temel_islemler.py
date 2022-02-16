import cv2
import numpy as np

img=cv2.imread("C:/Users/yusuf/Desktop/1_aGnp-4ENj8fApqZoO8by_Q.jpg") #peki bu resmin herhangi bir pikselindeki degerlere erişelim.
dimension= img.shape #img.shape bana img' değişkenindeki görselin boyutlarını verir.#dimension demek boyut demek.
color= img[9,1000]
print("BGR:",color) #işte suan bu piksellerdeki renk degerlerini ölçmek için print(color) yazıcam.
print(dimension) #allta outputta eni boyu ve kanalları gösterilmiştir.
cv2.imshow("Benimyazdigimpencereadı",img)


#peki benim sadece bir koordinattaki yeri maviye ulaşmam için ne yapmam gerekiyor.?
blue=img[420,500,0]
print("blue:",blue)

#peki yeşili bulmak için mavide 0 yazdıgım yere yeşil yazmak 1 kullanıcam.

green=img[420,900,1]
print("green:", green)

red=img[420,100,2]
print('red',red)

#ben buradaki kırmızı piksel değerini değiştirmek istersem.. aşağıd
img[420,100,2]=100
print('new red:',img[420,100,2])

#bunu daha kolay yapmak için item ve imset komutları daha kolay hale getirecektir.

blue1= img.item(150,200,0) #burada değiştirmek istediğimiz hedefi item ile aldık.
print('blue' ,blue1) # değiştirmeden önceki halini yazdırdık.


img.itemset((150,200,0),172) # sonra değiştirmek istediğimiz imset komutuyla girip 2 değişkene de yeni değerini yazdık.
print('THE NEW blue:',img[150,200,0])
cv2.waitKey(0)
cv2.destroyAllWindows() 

#pikseller içinde üç tane renk saklıydı bizim  diye adlandırdıgımız..