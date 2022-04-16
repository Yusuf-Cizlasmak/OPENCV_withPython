from imutils import paths  
import numpy as np
import argparse
import imutils
import cv2

#Söz yapıcam.
def looping_image(video):
    cap= cv2.VideoCapture(video)
    fileName= "C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV_SITE/Detection/image"
    
    while True:
        ret,frame=cap.read()
        frame=cv2.resize(frame,(640,480))
        frame=cv2.flip(frame,1)

        if cv2.waitKey(27) & 0xFF == ord('q'):
            break

        if cv2.waitKey(27) & 0xFF == ord('s'):
            cv2.imwrite(fileName+str(i)+".jpg",frame)
            i+=1

    return frame 



def find_marker(image):
    #şuan bu fonksiyonu gri ekrana ve kenarlarını bulmak için yazdım.
    gray= cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) #griye çevirdim.
    gray=cv2.GaussianBlur(gray,(5,5),0) #blur'u yaptım.
    edged=cv2.Canny(gray,35,125) #kenarları bulmak için canny'ı yaptım.

    #şimde de contour'ları bulalım..
    cnts=cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE) #contour'ları bulmak için contour'larının yerini belirttim.
    cnts=imutils.grab_contours(cnts) #contour'larının yerini belirttim.
    c=max(cnts,key=cv2.contourArea) #contour'larının en büyük alanını bulmak için max fonksiyonu kullandım.

    return cv2.minAreaRect(c) #en büyük alanının döndürdüğü değeri döndürüyorum.

def distance_to_camera(knownWidth, focalLength, perWidth):
    # kameraya ekrana yazdırılacak olan genişliği bulma
    return (knownWidth * focalLength) / perWidth 

KNOWN_DISTANCE = 24.0

KNOWN_WIDTH = 11.0

#kameranızdan 2 fit uzakta olduğu bilinen bir nesneyi içeren ilk görüntüyü yükleyin, ardından görüntüdeki kağıt işaretçisini bulun ve odak uzunluğunu başlatı
image= looping_image(0)
cv2.imshow("s",image)
cv2.waitKey(0)

for imagePath in sorted(paths.list_images("image")):#sorted fonksiyonu ile images klasöründeki resimleri sıraladım.
    marker = find_marker(image) #find_marker fonksiyonunu çağırdım.
    #marker= np.int32(marker) # int32'e çevirdim dataype'ını değiştirdim.
    focalLength = (marker[1][0] * KNOWN_DISTANCE) / KNOWN_WIDTH #focalLength'ı bulma
    image = cv2.imread(imagePath) #imagePath'i okuyup image'e atadım.
    marker = find_marker(image)
    inches = distance_to_camera(KNOWN_WIDTH,focalLength,marker[1][0]) #inches'ı bulma
   
    box=cv2.boxPoints(marker) if imutils.is_cv2() else cv2.boxPoints(marker) #box'ı bulma
   
    box=np.int0(box) #int0'e çevirdim dataype'ını değiştirdim.
    
    cv2.drawContours(image, [marker], -1, (0, 255, 0), 2)
    cv2.putText(image, "%.2fft" % (inches / 12),
        (image.shape[1] - 200, image.shape[0] - 20), cv2.FONT_HERSHEY_SIMPLEX,2.0, (0, 255, 0), 3)
    cv2.imshow("image", image)
    cv2.waitKey(0)