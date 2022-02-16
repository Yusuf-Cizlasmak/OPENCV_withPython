import cv2
from matplotlib.pyplot import contour, hsv
import numpy as np

cap= cv2.VideoCapture(0) #kameradan görüntüleri aldık

while True:
    ret,frame= cap.read() #burada ret hiç bir önemi yok aslında. frameler sonsuz döngüye girmesi için bunu yaptık ret sadece false true kontrol edick.
    frame=cv2.flip(frame,1) #burda da yapılan görüntülerin y eksenine göre aynasını aldık.
    if ret is False:
        break

    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV) #burda da daha rahat takip yapmak amacıyla hsv çevirdim.

    #sarı renk için gerekli değerleri bulmuştum.
    yellow1=np.array([22,109,57])
    yellow2=np.array([97,182,167])
    rows,cols,_ = frame.shape
    mask=cv2.inRange(hsv,yellow1,yellow2)
    contours,ret=cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)#burada masklerin hangi pencereye uygulanacağını ve daha iyi masklaması için yazdık diğer parametreleri.
    bitwise=cv2.bitwise_and(frame,frame,mask=mask) #ilk parametrem bitwise uygulacağım ikincisi kazıdığım alan, üçüncüsü de jargon.

    for cnt in contours:
        area= cv2.contourArea(cnt)
        if area>100:
            (x,y,w,h)=cv2.boundingRect(cnt)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)
            cv2.line(frame,(x+int(w/2),0),(x+int(w/2),rows),(0,255,0),2)
            cv2.line(frame,(0,y+int(h/2)),(cols,y+int(h/2)),(0,255,0),2)

    cv2.imshow("FRAME",frame)
    cv2.imshow("MASK PENCERE",mask)
    cv2.imshow("BITWISE",bitwise)

    if cv2.waitKey(50) == ord('q'):
        break

cap.realese()
cv2.destroyAllWindows()