#kütüphaneyi import ettik.

import numpy as np
import cv2
import argparse
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

#dosyayı python transform_example.py --image images/example_01.png --coords "[(73, 239), (356, 117), (475, 265), (187, 443)]" şeklinde çalıştırıcaz. 
ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",help="path to the image file")
ap.add_argument("-c","--coords",help="comma seperated of source points")
args=vars(ap.parse_args())

#şimdi resmi çekicez.

image=cv2.imread(args["image"])                 #burada resmi çektik ve koordinatları belirledik.
pts=np.array(eval(args["coords"]),dtype="float32")

 #şimdi de kuş bakışı için yukarıda konumlandırdığımız fonksiyonu kullanıcaz.

warped=four_point_transform(image,pts)

#şimdi de imshow'luyoruz.

cv2.imshow("Original",image)
cv2.imshow("Warped",warped)
cv2.waitKey(0)




