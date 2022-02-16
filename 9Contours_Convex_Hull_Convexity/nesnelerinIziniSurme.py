
#bunu bir video üzerinden yapıcaz.
import cv2
import numpy as np


cap=cv2.VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/9Contours_Convex_Hull_Convexity.py/dog.mp4")

while(cap.isOpened()): #eğer cap.read fonksiyonu çalışmaz ise VideoCapture=cap eşitle sonra da while içine cap.isOpened yaz. illa olacaktır.
    ret,frame=cap.read() #burada frameleri çekicez işte ama bu ret ile bi işimiz yok sadece true false alalım diye yani bildiğin ayıp olmasın diye orada kerata:)

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #burada nesne takibini iyi yapmak için bgr'dan hsv'ye çeviriyorum görüntüyü..
    #direkt beyazları bulmak için internet üzerin lower_white ve upper_white şeklinde.
    sensitivity=15
    lower_white=np.array([0,0,255-sensitivity])
    upper_white=np.array([255,sensitivity,255])

    #şimdi de mask uygulicaz.

    mask=cv2.inRange(hsv,lower_white,upper_white,)
    #şimdide maskın doğru uygulanabilmesi için bitwise uygulicam.
    res=cv2.bitwise_and(frame,frame,mask=mask) #neden iki frame var diyebilirsin. burda ilki orijinali olup diğeri de kazıma işlemi yaptığımı düşünebilirsin aslında.
    #bitwise ile yazmak istiyorsan bak bu bir özel kullanımdır. unutma bak.

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("sonuc",res)


    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()