import cv2
from cv2 import VideoCapture
circles= []
cap=VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/10HoughDonusumleri/line.mp4")
def mouse(event,x,y,flags,params):
    if event==cv2.EVENT_LBUTTONDOWN:
        circles.append((x,y))


#şimdi de yaptığım işlemi anlayacak fonk. olması gerekiyor.
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame",mouse)

while 1:
    _,frame= cap.read()
    frame=cv2.resize(frame,(640,480))
    for center in circles:
        cv2.circle(frame,center,20,(0,255,255),-1)

    cv2.imshow("Frame",frame)
    key= cv2.waitKey(15)
    if key==27: #27 makine dilinde "esc" nin karşılığıdır.
        break
    elif key ==ord("h"):
        circles=[]

cap.release()
cv2.destroyAllWindows()