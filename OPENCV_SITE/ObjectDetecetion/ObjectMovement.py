#az önce  BallDetection'ı yaptık. Şimdi de bu kısımda BallDetection'ın içinde bulunan fonksiyonları kullanarak ObjectMovement'ı (koordinatlı tabii)yazalım.

from collections import deque
from collections import deque
from cv2 import VideoCapture  #Nesnenin algılandığı ve izlendiği geçmiş N noktayı verimli bir şekilde depolamak için Python'un yerleşik deque veri türüne ihtiyacımız var.
from imutils.video import VideoStream 
import numpy as np
import argparse
import cv2
import imutils 
import time

#şimdi de argparse ile istediğimiz resmi çağırıyoruz.
ap= argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the (optional) video file")
ap.add_argument("-b", "--buffer", type=int, default=64, help="max buffer size")
args=vars(ap.parse_args())

#şimdi de en düşük ve yüksek sınırları (boundaries) yeşil rengi tanımlıyoruz.
greenLower= (29, 86, 6)
greenUpper= (64, 255, 255)
#frame'deki sınırları ve koordinatları list'leyelim.
pts=deque(maxlen=args["buffer"])
counter=0
(dX, dY)= (0, 0)
direction=""

#eğer video tanımlanmamaışsa bize kameradan getirmektir.
if not args.get("video", False):
    cap=cv2.VideoCapture(0)
    time.sleep(2.0)

while True:
    frame= cap.read()
    frame=frame[1] if args.get("video",False) else frame

    if frame is None:
        break

    frame= imutils.resize(frame, width=600)#600 pikseli kare olarak görüntüyü küçültüyoruz.
    