import cv2

cap=cv2.VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/14FaceDetection/faces.mp4")

face_cascade=cv2.CascadeClassifier("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/14FaceDetection/frontalface.xml.xml")
#şimdi de cascade dosyasını çalışmamıza dahil edelim. bunu da cv2.CascadeClassifier() hallediyorum.
#şimdi her bir frame'i gray'e çeviricez.

while (True):
    ret,frame= cap.read()  #ret bize bir şey vermicek sadece fonksiyon ikili çıktı veriyor. bize önemli olan frame oluyor.
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_cascade.detectMultiScale(gray,1.3,2)#face_cascade.detecetMultiScale yazmamın nedeni yukarıdaki değişkende tutmamdır.
#2.parametrem ise ölçeklendirme (ne kadar küçültücem ) 3.parametrem belirli bir alanda girilen sayı kadar pencere  bulsun. faces bize tuple olarak değerleri saklıcak şimdi.
#yüzün üstünde bir dikdörtgen çizmek istiyorum. bunun için for döngüsü kurmam lazım.
#Eğer iki yüzden fazla algılarsa 3.parametreyi değiştir.
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,0),2) 

    cv2.imshow("Sonuc",frame)
    if cv2.waitKey(5) & 0xFF==ord('q'):
        break    
cap.release() #while çıktığıma dikkat et. dikkat et. cap.release videoyu serbest bırakıyorlar.

cv2.destroyAllWindows() 