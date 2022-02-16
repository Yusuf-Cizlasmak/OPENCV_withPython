import cv2
import numpy as np
from matplotlib import pyplot as plt
#histogram bize görüntü hakkında aydınlık veya karanlık hakkında bilgi veriyor.
img=np.zeros((500,500),np.uint8) #zeros demek zaten 500'e 500 sıfırlardan (karanlıktan) oluşuyor demek.
#burda iki yeni fonk. öğrenicez.plt.hist() -- plt.show() histte yapıp. show'da göstericez adında anlaşılacağı üzere.
cv2.rectangle(img,(0,60),(150,200),(255,250,240),-1)
#plt.hist(img.ravel(),256,[0,256]) #ilkisi bilmememiz gereken bir fonk. ikincisi max value. 3'cüsü ise değer aralıkları şeklinde düşünebiliriz aslında.
#plt.show()
cv2.imshow("Foto",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#peki histogram neden 250000 gösterdi. çünkü benim 500 500 piksel değerlerim var.

#şimdi ben bunu bir dikdörtgende denicem.