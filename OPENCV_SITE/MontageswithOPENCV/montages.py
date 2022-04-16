from imutils import build_montages
from imutils import paths
import argparse
import cv2
import random

#yine argparse kullanıcaz o yüzden gerekli tanımlamaları yapmamaız gerekiyor.

ap=argparse.ArgumentParser()
ap.add_argument("-i","--images",required=True,help="path to input images")
ap.add_argument("-s","--sample",type=int,default=21,help="# of images to sample") #sample göstermelik demek.

args=vars(ap.parse_args())
#birden fazla resmi istemiş. Klasör istemiş olmuş.
#şimdi de dosya yolunu belirlemek için imagePath değişkeni tanımlıcam.
imagePaths=list(paths.list_images(args["images"])) #rastgele çağrımamızın nedeni montaj, kendi uygularımızı rastgele çağırmak için,
random.shuffle(imagePaths) #· Bu fonksiyon, bir listede yada tupleda yer alan öğeleri rastgele getirir

#şimdi çağırdığımız görüntüyü değerleri boş list'e alıcaz.

images= []

#loop over the list of image paths (resimleri)
for imagePath in imagePaths:
    image=cv2.imread(imagePath)
    images.append(image)

# görüntüler için montajları oluşturun.
    montages=build_montages(images,(640,480),(7,3)) #2 parametrelerim boyut değerleridir

for montage in montages:
    cv2.imshow("Montage",montage)
    cv2.waitKey(0)

