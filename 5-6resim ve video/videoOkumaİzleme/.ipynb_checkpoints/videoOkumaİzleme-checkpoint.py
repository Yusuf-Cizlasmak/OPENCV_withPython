{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e376c63a",
   "metadata": {},
   "outputs": [],
   "source": [
    "import cv2\n",
    "\n",
    "cap= cv2.VideoCapture(\"vizontele.mp4\") #cap 'yakalama anlamından dolayı' kullanılan bir değişken.\n",
    "#videoCapture' fonksiyonunu kullanıp 0 girersek webcam kullanırız anlamına geliyor.\n",
    "while True:    # sonsuz bir döngüyü ifade eder. ret 0 eşitlersek bu döngüyü kırmış oluruz.\n",
    "    ret, frame = cap.read()\n",
    "    if ret==0:\n",
    "        break\n",
    "    frame =cv2.flip(frame,1) # gördüğün her görüntüyü istediğin eksene göre yansıtır.\n",
    "    cv2.imshow(\"Vizontele\",frame) \n",
    "    if cv2.waitKey(50) & 0xFF == ord(\"q\"): #frame'leri atamak. \n",
    "        break\n",
    "        \n",
    "  \n",
    "        #burda tuş atayarak bu döngüyü kırarak pencereden çık demek.\n",
    "    \n",
    "\n",
    "    \n",
    "cap.release() #yukarıdaki işlemlerin kapatıp başka işlemlere için yol açar.\n",
    "cv2.destroyAllWindows()\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4e1a51d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bb25703e",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b3883856",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
