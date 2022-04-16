#Gerekli kütüphaneleri import edelim

import numpy as np
import argparse
import imutils
import cv2

def order_points(pts): 
    rect=np.zeros((4,2),dtype="float32") # 4 tane siyah nokta belirledik ve float 32 tipinde
    s=pts.sum(axis=1)
    rect[0]=pts[np.argmin(s)]
    rect[2]=pts[np.argmax(s)]
    
    diff=np.diff(pts,axis=1)                                             #4 noktayı işaretlemek yazdık.. ve 
    rect[1]=pts[np.argmin(diff)]
    rect[3]=pts[np.argmax(diff)]                # sol üst nokta en küçük toplam olacaktır, oysa
                                                # sağ alt nokta en büyük miktara sahip olacak

    return rect 

def four_point_transform(image,pts):
    rect=order_points(pts) #noktaların tutarlı bir sırasını elde edin ve bunları tek tek açın
    (t1,tr,br,b1)=rect

    #şimdi de en alttaki sağ ve sol ve en üstteki sağ ve solları belirlemek olacak. sonra maximum- minumum x eksenindeki noktaları bulucam.

    widthtA=np.sqrt(((br[0]-b1[0])**2)+((br[1]-b1[1])**2))
    widthB=np.sqrt(((tr[0]-t1[0])**2)+((tr[1]-t1[1])**2)) 
    maxWidth=max(int(widthtA),int(widthB)) #Genişlikte sadece heightA'nın tam sayılarını alıyoruz. 

    #Aynısını Uzunluk içinde yapıcaz.
    #şimdi de en alttaki sağ ve sol ve en üstteki sağ ve solları belirlemek olacak. sonra maximum- minumum y eksenindeki noktaları bulucam.
    heightA=np.sqrt(((br[0]-b1[0])**2)+((br[1]-b1[1])**2))
    heightB=np.sqrt(((tr[0]-t1[0])**2)+((tr[1]-t1[1])**2)) 
    maxHeight=max(int(heightA),int(heightB))

    #şimdi de kuş bakışı görmek için uzunluklarını hesaplıcaz.çünkü görüntünün boyutlarına sahip olduğumuza göre.
    dst = np.array([
		[0, 0],
		[maxWidth - 1, 0],
		[maxWidth - 1, maxHeight - 1],
		[0, maxHeight - 1]], dtype = "float32")

# compute the perspective transform matrix and then apply it
    M=cv2.getPerspectiveTransform(rect,dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

        #şimdi de return'layız.
    return warped

#argparse mentörü ile resimleri ve kodu cmd çekmem için argparse kullanıcam.
ap=argparse.ArgumentParser() #ap değişkenini argparse.ArgumentParser fonksiyonu eşitliyorum (Argüman Biçimleyici-Kesici demek)
ap.add_argument("-i","--image",help="path to the image") #burada required gerek kalmadan yaptık. İlk parametrem key'im ikinci dosyanın ne işe yaracağını söyleyen help.
args=vars(ap.parse_args()) 


#şimdi de diskten resmi çekiyoruz.
image=cv2.imread(args["image"]) #burada args içine key'imi yazıcam.
#şimdi de resmi daha çok işlenebilmek için gri çeviricem

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

#x ve y düzleminde Scharr magnitude ile işlem yapıyoruz.

ddepth=cv2.CV_32F if imutils.is_cv2() else cv2.CV_32F 
gradX=cv2.Sobel(gray,ddepth=ddepth,dx=1,dy=0,ksize=-1) #x düzleminde
gradY=cv2.Sobel(gray,ddepth=ddepth,dx=0,dy=1,ksize=-1) #y düzleminde

gradient=cv2.subtract(gradX,gradY) 
gradient=cv2.convertScaleAbs(gradient) #magnitude değerini küçültüyoruz.

#Şimdi de blur'layalıp ve threshold'layalım.

blurred=cv2.blur(gradient,(9,9)) #blur'layalım.
(_,thresh)=cv2.threshold(blurred,225,255,cv2.THRESH_BINARY) #threshold'layalım. #ilk paratmetremiz ilk resmimiz, , ikincisi threshold değerimiz, üçüncüsü threshold tipimiz,    #burada threshold tipimiz binary olacak.

#kapalı bir kernel matrisi yapıp resmi threshold'layalım.

kernel= cv2.getStructuringElement(cv2.MORPH_RECT,(21,7)) #burada kernel matrisi yapıyoruz.
closed=cv2.morphologyEx(thresh,cv2.MORPH_CLOSE,kernel) #burada kapalı bir kernel matrisi yapıyoruz. #birinci parametremiz threshold, ikincisi kernel matrisi, üçüncüsü kapalı bir kernel matrisi.

#şimdi de morfolojik işlemleri yapalım.
closed=cv2.erode(closed,None,iterations=4) #burada erode işlemi yapıyoruz.
closed=cv2.dilate(closed,None,iterations=4) #burada dilate işlemi yapıyoruz. #tekrarlama sayısını 4 yapıyoruz.

#şimdi de threshold contour'ları bulalım. ve contours'ların sıralayalım.. ve en büyük olanını saklayalım.
cnts=cv2.findContours(closed.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE) #burada contours buluyoruz.ayrıca son iki parametrem contour'ın sağlayabilmesi..
cnts=imutils.grab_contours(cnts) 

c=sorted(cnts,key=cv2.contourArea,reverse=True)[0] #burada contours'ların sıralanmasını sağlıyoruz. ama en büyük değerini alıyoruz.
c1=sorted(cnts,key=cv2.contourArea,reverse=True)[1] #burada contours'ların sıralanmasını sağlıyoruz. ama en büyük değerini alıyoruz.

#en büyük konturun döndürülmüş sınırlayıcı kutusunu hesaplalayım..
rect=cv2.minAreaRect(c) #burada en büyük konturun döndürülmüş sınırlayıcı kutusunu hesaplalıyoruz.
rect1=cv2.minAreaRect(c1) #burada en büyük konturun döndürülmüş sınırlayıcı kutusunu hesaplalıyoruz.

box=cv2.boxPoints(rect) 
box=np.int0(box) #burada box'ı int0 ile dönüştürelim.


box1=cv2.boxPoints(rect1)
box1=np.int0(box1) #burada box'ı int0 ile dönüştürelim.


#tespit edilen barkodun etrafına bir sınırlayıcı kutu çizin ve görüntüyü görüntüleyin
p1=four_point_transform(image,box) #burada four_point_transform fonksiyonunu kullanıyoruz.
p2=four_point_transform(image,box1) #burada four_point_transform fonksiyonunu kullanıyoruz.

cv2.drawContours(image,[box],-1,(0,255,0),3) #burada box'ının çizdirilmesini sağlıyoruz.  #-1 yazılırsa tüm konturları çizdiriyor. #3 yazılırsa kalınlığı 3 olarak ayarlıyoruz. 
cv2.drawContours(image,[box1],-1,(0,255,0),3) #burada box'ının çizdirilmesini sağlıyoruz.  #-1 yazılırsa tüm konturları çizdiriyor. #3 yazılırsa kalınlığı 3 olarak ayarlıyoruz. 


cv2.imshow("Image",p1) #burada görüntüyü görüntüleyelim.
#cv2.imshow("Image",p2) #burada görüntüyü görüntüleyelim.


cv2.imshow("Graident",gradient) #burada görüntüyü görüntüleyelim.
cv2.imshow("Threshold",thresh) #burada görüntüyü görüntüleyelim.
cv2.imshow("ROI",closed) #burada görüntüyü görüntüleyelim.

cv2.waitKey(0)

#Mission direk barkodu net görüntü olarak eklet..