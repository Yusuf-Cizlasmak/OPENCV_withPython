#ilk önce gerekli kütüphaneleri import ediyoruz.
from pickletools import uint8
import numpy as np
import argparse
import cv2

#istediğimiz şekilde resimleri ve kodu cmd çekmem için argparse kullanıcam.
ap=argparse.ArgumentParser() #ap değişkenini argparse.ArgumentParser fonksiyonu eşitliyorum (Argüman Biçimleyici-Kesici demek)
ap.add_argument("-i","--image",help="path to the image") #burada required gerek kalmadan yaptık. İlk parametrem key'im ikinci dosyanın ne işe yaracağını söyleyen help.
args=vars(ap.parse_args())

#şimdi de diskten resmi çekiyoruz.
image=cv2.imread(args["image"]) #burada args içine key'imi yazıcam.
#şimdi de hazır renklerinden mavi değerini bulucam. boundaries==SINIRLAR demek.
boundaries = [
	([17, 15, 100], [50, 56, 200]),
	([86, 31, 4], [220, 88, 50]),
	([25, 146, 190], [62, 174, 250]),
	([103, 86, 65], [145, 133, 128])] 

#mavi sınırlarını bulmak için bir döngüye koymak zorundayım.

for(lower,upper) in boundaries: #lower upper değerleri boundaires(sınırlar) içinde dönecekler.
    lower=np.array(lower,dtype="uint8") #np.array döndürtmek için ya float32 ya da uint8 olması gerekiyor.
    upper=np.array(upper,dtype="uint8") 

    #şimdi de karmaşık sınırları bulmak için mask uygulucam.

    mask=cv2.inRange(image,lower,upper) #cv2.inRange fonksiyonudur, bu foksiyonumuz ise girilen değerler arasındaki renkleri seçmeye yarar.
    output=cv2.bitwise_and(image,image,mask=mask) #bitwise_and ile resmi öbekleştirdim. ilk parametrem işlenecek resim, ikincisi kazınacak resim,3.cüsü de literatür.

    #şimdi Gösteri zamanı..
    cv2.imshow("images",np.hstack([image,output]))
    cv2.waitKey(0)

cv2.destroyAllWindows()

"""
Summary
In this blog post I showed you how to perform color detection using OpenCV and Python.

To detect colors in images, the first thing you need to do is define the upper and lower limits for your pixel values.

Once you have defined your upper and lower limits, you then make a call to the cv2.inRange method which returns a mask, specifying which pixels fall into your specified upper and lower range.

Finally, now that you have the mask, you can apply it to your image using the cv2.bitwise_and function.
"""