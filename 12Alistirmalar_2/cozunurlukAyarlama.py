import cv2

windowName="Live Video"
cv2.namedWindow(windowName)

cap=cv2.VideoCapture(0)
print("Width:"+ str(cap.get(3))) #genişlik 3
print("Height:"+ str(cap.get(4))) #yükseklik 4
#ben şuan görüntünün uzunluk ve genişliğini get fonksiyonu ile aldım şimdi aşağıda görüldüğü üzere set'le düzenlicem.
cap.set(3,480) #ilk önce düzeltmek istediğim şeyi yazıyorum sonra istediğim çözünürlüğü ayarlıyorum.
cap.set(4,240)
print("YENİ Width:"+ str(cap.get(3))) #genişlik 3
print(" YENİ Height:"+ str(cap.get(4))) #yükseklik 4
while True:
    ret,frame=cap.read()
    frame=cv2.flip(frame,1) # daha düz bir görüntü için böyle yaptık bi nevi ayna görevi görüyor cv2.flip

    cv2.imshow(windowName,frame)

    if cv2.waitKey(15) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()