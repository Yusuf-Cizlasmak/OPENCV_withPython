# import the necessary packages

import argparse
import cv2
from matplotlib import image

#argparse artık nasıl işleyişini biliyoruz.

ap=argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="path to the image file")
args=vars(ap.parse_args())

#load the image form disk
image=cv2.imread(args["image"])
(h,w,d)=image.shape

print("w:{}, h:{},d: {}".format(w,h,d))

#resmi göstermek için
cv2.imshow("image",image)
cv2.waitKey(0)


#NONE TYPE ERROR HATASI ALMAMAK İÇİN DOSYA YOLUNU ÖNEMLİ OLMASI GEREKİR.
