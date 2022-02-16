import cv2
import numpy as np



def nothing(x): #yine bir Trackbar kullanıcam. o yüzden hata almamak adına boş bir fonksiyon oluşturdum.
    pass    

cap= cv2.VideoCapture(0)
cv2.namedWindow("Trackbar")
cv2.createTrackbar("LH","Trackbar",0,179,nothing)
cv2.createTrackbar("LS","Trackbar",0,255,nothing)
cv2.createTrackbar("LV","Trackbar",0,255,nothing)
cv2.createTrackbar("UH","Trackbar",0,179,nothing)
cv2.createTrackbar("US","Trackbar",0,255,nothing)
cv2.createTrackbar("UV","Trackbar",0,255,nothing)

while True:
    ret,frame=cap.read()
    frame=cv2.resize(frame,(640,480))
    frame=cv2.flip(frame,1)
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    lowerH=cv2.getTrackbarPos("LH","Trackbar")
    lowerS=cv2.getTrackbarPos("LS","Trackbar")
    lowerV=cv2.getTrackbarPos("LV","Trackbar")
    upperH=cv2.getTrackbarPos("UH","Trackbar")
    upperS=cv2.getTrackbarPos("US","Trackbar")
    upperV=cv2.getTrackbarPos("UV","Trackbar")

    lowerBlue=np.array([lowerH,lowerS,lowerV])
    upperBlue=np.array([upperH,upperS,upperV])

    mask=cv2.inRange(hsv,lowerBlue,upperBlue) 
    bitwise=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Normal",frame)
    cv2.imshow("bitwise'lı mask",bitwise)
    cv2.imshow("MASK",mask)
    if cv2.waitKey(30) & 0XFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()