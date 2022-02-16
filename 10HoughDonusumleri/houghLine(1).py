import cv2
import numpy as np


img= cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/10HoughDonusumleri/h_line.png")

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #daha kolay işlem yapılması için gray'e 

edges =cv2.Canny(gray,75,150) #canny kenar bulma algoritmasını kullanıyor.

cv2.imshow("gray",gray)
cv2.imshow("Koseli Resim",edges)
#artık line'ları tespit etmek.
#cv2.HoughLines() normalde bu fonksiyonu kullanırız ama bu bilgisayarın Ram'ini öldürdüğünden dolayı aşağıdakini tercih edicez.
lines= cv2.HoughLinesP(edges,1,np.pi/180,50) #buraya en son parametre olarak maxLineGap'ı de ekleyip çizgileri kalınlaştırabilirsiniz.
for line in lines:
    x1,y1,x2,y2 =line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)                        #şimdi biz print(lines dediğimizde altta 4 tane değer çıktı bunları x1,y1,x2,y2 şeklinde düşünebiliriz aslında da x1,x2'ler başlangıc veya bitiş olarak düşünebiliriz)

cv2.imshow("Orijinal",img)
cv2.imshow("gray",gray)
cv2.imshow("Koseli Resim",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()