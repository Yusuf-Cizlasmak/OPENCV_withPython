import cv2
import numpy as np


cap= cv2.VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/11Alistirmalar_1/car.mp4")
#şimdi yeni bir fonksiyon öğrenicez subtractor fonksiyonu.
subtractor=cv2.createBackgroundSubtractorMOG2(history=100,varThreshold=122,detectShadows=True)
#history 100 yazmamızın sebebi istediğim frame sayısı o kadar olması.
#detectShadows adında anlaşılacağı üzere gölgeleri de gösteriyim mi gibisinden düşünülebilir.

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    mask= subtractor.apply(frame)


    cv2.imshow("Normal",frame)
    cv2.imshow("2YOLARKAPLAN",mask)

    if cv2.waitKey(30) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()