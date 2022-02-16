import cv2

cap= cv2.VideoCapture(0) #Görüntüyü cam'den almak için 0 giriyoruz.

#kullanacağımız cascade dosyasını çalışmamıza dahil edelim.
face_cascade = cv2.CascadeClassifier("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/14FaceDetection/frontalface.xml.xml")

#Sonsuz bir döngü ile her frame tek tek inceleyelim.
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1)

    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#Haar-like özellikleri kolay algılayabilmek için her bir kareyi boz(gri) tonlara çevirelim.
    faces=face_cascade.detectMultiScale(gray,1.5,7)

#"faces" değişkeninde tuttuğumuz koordinatları kullanarak yüzleri dikdörtgen içerisine alalım.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(82,0,255),2)

#İşlediğimiz kareleri görelim.
    cv2.imshow("video",frame)
    if cv2.waitKey(15) & 0XFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
