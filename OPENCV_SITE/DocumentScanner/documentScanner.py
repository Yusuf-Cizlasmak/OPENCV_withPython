#bunun için algoritmamız şu olacak.

#sınırları belirle.
#sınırları contourler ile belirt.
#bir transform perseptifini uygula.

#gerekli kütüphaneleri import et.


import numpy as np
import argparse
import cv2
import imutils

#şimdi de argparse aktif ediyoruz.argparse çalışma mantığı python dosya.py key value şeklindedir.

def order_points(pts):
	# initialzie a list of coordinates that will be ordered
	# such that the first entry in the list is the top-left,
	# the second entry is the top-right, the third is the
	# bottom-right, and the fourth is the bottom-left
	rect = np.zeros((4, 2), dtype = "float32")
	# the top-left point will have the smallest sum, whereas
	# the bottom-right point will have the largest sum
	s = pts.sum(axis = 1)
	rect[0] = pts[np.argmin(s)]
	rect[2] = pts[np.argmax(s)]
	# now, compute the difference between the points, the
	# top-right point will have the smallest difference,
	# whereas the bottom-left will have the largest difference
	diff = np.diff(pts, axis = 1)
	rect[1] = pts[np.argmin(diff)]
	rect[3] = pts[np.argmax(diff)]
	# return the ordered coordinates
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




ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path to the image to be scanned")
args=vars(ap.parse_args())

#resmi yükle ve resmin uzunluğuna yeni bir değer ata.
image=cv2.imread(args["image"])
ratio=image.shape[0]/500.0
orig=image.copy()
image=imutils.resize(image,height=500)
image=cv2.resize(image,(640,480))

#grayscale çevir ve, blurla, sonra da resmin kenarlarını tespit et.

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray=cv2.GaussianBlur(gray,(5,5),0)#burada ilk parametrem işleneceğim resim sonra kernel matrisim, sonra da sigma değerim.
edged=cv2.Canny(gray,75,200)#burada görüntüyü resmen sınıflandırmış ve kenarlarını çizmiş bir şekilde etki yapıyoruz.Canny ingilizce de açıkgöz demek.


#orijinal ve kenarlanmış görüntüyü gösteriyoruz.
print("STEP 1 : Edge Detection")
cv2.imshow("Image",image)
cv2.imshow("Edged",edged)
cv2.waitKey(0)
cv2.destroyAllWindows()

#contourleri bulup resmi sınırlarını çizeceğiz. en büyüğünü..

cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #burada contourleri buluyoruz.
cnts=imutils.grab_contours(cnts) #burada contourleri listeye çeviriyoruz.
cnts=sorted(cnts,key=cv2.contourArea,reverse=True)[:5] #burada contourleri sınırlarını çizmek için sıralıyoruz.


#sınırları çizmek için bir for döngüsü oluştur.
for c in cnts:
    #contourleri kenarlarını çizmek için bir kutu oluştur.
    peri=cv2.arcLength(c,True)
    approx=cv2.approxPolyDP(c,0.02*peri,True) 


    if len(approx)== 4:
        screenCnt=approx
        break #burada sınırlarını çizdikten sonra döngüyü kırıyoruz.4 tane en yakın contour bulunmuş olacak.



print("STEP 2 : Find contours of paper") #sayfanın contour'leri bulmuş oluyoruz.
cv2.drawContours(image,[screenCnt],-1,(255,0,0),2)
cv2.imshow("Dısarısı",image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Şimdi de Threshold ve Perspective Transform uygulayacağız.

warped=four_point_transform(orig,screenCnt.reshape(4,2)*ratio) #burada 4 tane nokta bulunan contour'u 4 tane nokta ile transform ediyoruz.


warped=cv2.cvtColor(warped,cv2.COLOR_BGR2GRAY) #warped'i griye çeviriyoruz.
#T=threshold_local(warped,11,offset=10,method="gaussian") #burada threshold uyguluyoruz.
#warped= (warped>T).astype("uint8")*255 #burada threshold uygulanmış görüntüyü 255 yapıyoruz.

print("STEP 3 : Apply perspective transform")
cv2.imshow("Original",imutils.resize(orig,height=640))
cv2.imshow("Scanned",imutils.resize(warped,height=640))
cv2.waitKey(0)