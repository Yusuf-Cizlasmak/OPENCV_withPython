import cv2
from cv2 import threshold


cap=cv2.VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/11Alistirmalar_1/eye_motion.mp4.mp4")

while True:
    ret,frame= cap.read()
    if ret ==0:
        break

#şimdi roi alanımı belirliyorum. region of interest.
    roi = frame[80:210,230:450] #bunu videonun özelliklerinden bulabilriiz.
#frame[y1:y2,x1:x2]  roi
    gray=cv2.cvtColor(roi,cv2.COLOR_BGR2GRAY) # çeviriyoruz.
    _,threshold = cv2.threshold(gray,2,255,cv2.THRESH_BINARY_INV)
    cv2.imshow("ROI",roi)
    cv2.imshow("threshold",threshold)

    contours,_= cv2.findContours(threshold,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #ben şuan contours değerlerini sıralıcam.
    contours= sorted(contours,key=lambda x: cv2.contourArea(x),reverse=True)
    #contourArea değerlerim bu fonksiyona göre sıralanacak demek bu. reverse de tersten sıralama demek zaten.
    #şimdi bir dikdörtgen çizmek için bir for döngüsü yapıcam

    for cnt in contours:
        (x,y,w,h)
    if cv2.waitKey(40) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()