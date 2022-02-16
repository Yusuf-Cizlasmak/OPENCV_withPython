import cv2

def nothing():
    pass

img1=cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/aircraft.jpg")
img1=cv2.resize(img1,(640,480))
img2=cv2.imread("C:/Users/yusuf/Desktop/YAZEM/YAZEM_goruntuIsleme_/OPENCV/12Alistirmalar_2/balls.jpg")
img2=cv2.resize(img2,(640,480))