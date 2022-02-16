import cv2
import numpy as np

#1.YOL amacımız frame'leri karşılaştırıp aynı olan kısımlarda, beyaza kalmasını istiyip olmayan kısımların ise siyaha boyanması.

cap= cv2.VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/11Alistirmalar_1/car.mp4")
#yaptığımız çoğu işlemde olduğu gibi blur'lıcaz sonra daha temiz bir görüntü için cv2.GaussianBlur() fonksiyonunu kullanıcaz ilk frame için sonra diğerleri içinde aynı şeyi uygulıcaz.

_,firstFrame=cap.read()
firstFrame=cv2.resize(firstFrame,(640,480))
firstGray=cv2.cvtColor(firstFrame,cv2.COLOR_BGR2GRAY)
firstGray=cv2.GaussianBlur(firstGray,(5,5),0)

#ilk frame için yaptıklarımızı bu sefer tüm framelere uygulıcaz.

while True:
    _,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(5,5),0)
    #şimdi yeni bir fonksiyon öğrenicez. ilk frame'le diğer frameleri karşılaştırıcaz.

    diff=cv2.absdiff(firstGray,gray) #ilk parametrem karşılaştıracağım ilk değişken, ikincisi second one,
    #şimdi ben bir sonuç aldım yani en sona gittim. ancak gri noktaları görmek istemiyorum o yüzden threshold uygulicam.
    _,diff=cv2.threshold(diff,25,255,cv2.THRESH_BINARY)
    cv2.imshow("NormaL Frame",frame)
    cv2.imshow("First Frame",firstFrame)
    cv2.imshow("Different Frame",diff)

    if cv2.waitKey(20) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()