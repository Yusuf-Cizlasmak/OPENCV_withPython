from collections import deque #farklı bir tür liste -- çift yönlü liste.. Liste 32. elemanının önüne ekleme yapar.
from imutils.video import VideoStream
import numpy as np
import argparse
import cv2
import imutils
import time

from pyrsistent import v

ap= argparse.ArgumentParser() 
ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")  # burada argparse ile istediğim resmi çağırabilirim . Sadece terminala 
args = vars(ap.parse_args())

#şimde de topun en alt sınırı ve üst sınırını belirlicem (yeşil renk!) (boundaries)ını belirleyelim, HSV ile bu işlemi gerçekleşiricem. 

greenLower= (29, 86, 6)
greenUpper= (64, 255, 255)
pts= deque(maxlen=args["buffer"]) #deque ile bir liste oluşturduk.

#video dosyasının yolunu alıyoruz.görüntüyü kameradan mı yoksa video dosyasından mı alıyoruz onu sorguluyor.
if not args.get("video", False):
    cap= VideoStream(src=0).start() 
    time.sleep(1.0) #bu da 2 saniye beklemeyi sağlıyor.

else:
    cap= cv2.VideoCapture(args["video"])
    time.sleep(1.0) #bu da 3 saniye beklemeyi sağlıyor.

while True:
    frame= cap.read() #_ yerine frame yazarsak görüntüyü alıyoruz.
    
    frame= frame[1] if args.get("video", False) else frame #bu da video dosyasından görüntü alıyor.

    if frame is None:
        break

    frame= imutils.resize(frame, width=600) #bu kısımda görüntüyü 600 pikseli küçültüyoruz.
    blurred= cv2.GaussianBlur(frame, (11,11), 0) #bu kısımda görüntüyü blur yapıyoruz.
    hsv= cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV) #bu kısımda görüntüyü HSV ye çeviriyoruz.     

    #şimde de morfolojik işlemleri ve inRange fonksiyonu ile seçtiğimiz değerler arasında bir mask uygulucaz.
    mask=cv2.inRange(hsv, greenLower, greenUpper)
    mask= cv2.erode(mask, None, iterations=2) #bu kısımda mask uyguluyoruz.
    mask=cv2.dilate(mask, None, iterations=2) 

    #şimdi mask uygulanmış görüntüyü kullanarak contourları buluyoruz.
    cnts= cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts= imutils.grab_contours(cnts)
    center= None

    if len(cnts) > 0:
        #en büyük contouru buluyoruz.
        c= max(cnts, key=cv2.contourArea) #contourların büyüklüğünün en büyük olanını buluyoruz.
        ((x,y), radius)= cv2.minEnclosingCircle(c) #bu kısımda contourun çizebileceği en küçük çemberi buluyoruz.
        M= cv2.moments(c) #
        center= (int(M["m10"]/M["m00"]), int(M["m01"]/M["m00"])) #bu kısımda contourun merkezini buluyoruz.

        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2) #bu kısımda en büyük contouru çevirip çevrilen contouru çevrilen contourun içinde çember çiziyoruz.
            cv2.circle(frame, center, 5, (0, 0, 255), -1) #burada ise köşeleri çiziyoruz.
            cv2.rectangle(frame, (int(x-radius), int(y-radius)), (int(x+radius), int(y+radius)), (0, 255, 0), 2) #bu kısımda çemberin içinde dikdörtgen çiziyoruz.

            pts.appendleft(center) #bu kısımda contourun merkezini değişkene atıyoruz.
    i= 0

    for i in range(1, len(pts)):
                if pts[i-1] is None or pts[i] is None: 
                    continue

    thickness= int(np.sqrt(args["buffer"]/float(i+1))*2.5) #bu kısımda contourun kalınlığını belirliyoruz.
    cv2.line(frame, pts[i-1], pts[i], (0, 0, 255), thickness) #bu kısımda contourun kalınlığını belirliyoruz.
    cv2.imshow("Frame", frame) #bu kısımda görüntüyü ekrana yazdırıyoruz.

    if cv2.waitKey(27) & 0xFF == ord('q'):
                break
if not args.get("video", False):
                cap.stop()

else:
            cap.release()

cv2.destroyAllWindows()