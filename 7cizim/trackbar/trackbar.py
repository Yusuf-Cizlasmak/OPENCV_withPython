import cv2
import numpy as np


def nothing(x):        #Burda boş bir küme tanımladım.. ileride sebebi hikmetini anlatacakmış hoca.
    pass

#pencere oluşturmam lazım trackbar için..
#kanal 3 tane arka arkaya 512'lik portre çizmişim gibi düşün.  sırf renkli renkler elde edebilmek için gibi düşün.
img=np.zeros((512,512,3),np.uint8)
cv2.namedWindow("image") #isim vermemizin nedeni ;trackbar arayüzünü rengini değiştireceğimiz pencereye uyarlamaktır.#RGB diye bir 3 kızak oluşturucaz ve bir anahtar oluşturucaz buna göre renkleri değiştiricez. 

cv2.createTrackbar("R","image",0,255,nothing)                                                   
#girdiğimiz ilk parametre kızagın adı olacak,ikinci parametrem kızagin yerleşecegi "Pencerenin adı",3 ve 4 parametrenin başlangıcı ve son degerleri olacak.. 0-255 mevzusu.
cv2.createTrackbar("G","image",0,255,nothing)     
cv2.createTrackbar("B","image",0,255,nothing)     
#son olarak anahtarı yani value oluşturmam gerekiyor.
switch= "0:OFF \n1:ON" 
cv2.createTrackbar(switch,"image",0,1,nothing)     #ben burada sürekli dinamik bir yapı oluşturuyorum. bu yüzden sürekli değişiklik yapmam lazım. while döngüsü yapmam lazım.
while True:
    cv2.imshow("image",img)
    if cv2.waitKey(1) & 0XFF==ord('q'):   #q bastıgımızda cıkmak icin böyle yaptık. tıpkı oncekilerde yaptıgımız gibi.
        break

    r = cv2.getTrackbarPos("R","image") #burada adından da anlaşacalıgı üzere trackbar'ın konumunu ögreniyoruz.
    g = cv2.getTrackbarPos("G","image") #burada adından da anlaşacalıgı üzere trackbar'ın konumunu ögreniyoruz.
    b = cv2.getTrackbarPos("B","image") #buradaki ilk parametre trackbar ismi ve ikincisi kızacagın bulunacagı pencere.
    s=  cv2.getTrackbarPos(switch,"image")


    if s==0:
        img[:]=[0,0,0]
    else:
        img[:]=[b, g, r] #burada rgb ile tüm renklere ulaşmayı sağlamaya çalışıyorum.

cv2.destroyAllWindows()




#burada yaptıgın en büyük hata while'in içine yapılanları yapmamamış olman.