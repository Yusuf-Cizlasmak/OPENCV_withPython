import cv2
import numpy as np


cap= cv2.VideoCapture(0)

while 1:
    ret,frame= cap.read() #bu arada direkt frame'leri çekiyorum videodan.
    frame=cv2.flip(frame,1) #bir defa takla ettirmem gerekiyor. AYNA MODU.


#edge kenar demek
    edges= cv2.Canny(frame,100,200)

    cv2.imshow("Frame",frame)
    cv2.imshow("Kenarları bulunmus goruntu",edges)

    if cv2.waitKey(5) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()