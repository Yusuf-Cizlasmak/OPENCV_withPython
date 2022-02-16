from pickletools import uint8
import cv2
import numpy as np

vid= cv2.VideoCapture("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/10HoughDonusumleri/line.mp4")

while True: 
    ret,frame=vid.read() # cap.read() sağlıklı bi şekilde görüntü okuduğunda true değerleri göndererek ret hafızasında saklanır
    #video biraz büyük oldu hadi bunu biraz küçültelim.
    frame=cv2.resize(frame,(640,480)) #ilk parametrem değiştireceğim pencere ikinci de ölçüleri
    #amacım hsv'ye çevirip sarı renkleri videodan ayırıcam.
    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    #Opencv temel işlemler bölümünde yaptığın TRACKBAR HSV uygulaması ile aralıkları bulabilirsin. 
    yellow1=np.array([18,109,140],np.uint8)
    yellow2=np.array([48,255,255],np.uint8)

    mask=cv2.inRange(hsv,yellow1,yellow2)
    
    #şimdi ise edge uygulucam yani o sarı köşeleri bulucam ve işaretlicem.

    edges=cv2.Canny(mask,75,250)

    lines=cv2.HoughLinesP(edges,1,np.pi/180,50,maxLineGap=50)

    for line in lines:
        (x1,y1,x2,y2)= line[0] #burada başlangıç bitiş noktalarını girdik 
        cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),5) #burada çizgilerle belirttik.
    
    if cv2.waitKey(30) & 0xFF==ord('q'):
        break
    cv2.imshow("Son Hali",frame)
vid.release()
cv2.destroyAllWindows()