import cv2

cap=cv2.VideoCapture("C:/Users/yusuf/Downloads/CemYılmaz..mp4") #istediğimizi videoCapture fonksiyonu ile çağırıyoruz.

while True:
    ret, frame = cap.read()  #videoların framelerden oluştuğunu biliyoruz bu şekilde döngüye koyarak frameleri video şeklinde izliyoruz.
    #işte şimdi frame'ların renk uzaylarını değiştirmeye geliyor iş.
    frame= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #burada ilk değişkenim kaynağım, ikincisi de BGR'dan GRAY'E dönüştürmek için yaptığım fonks.
    if ret== False: #videomun bittiğinde ret olarak height ve weight olarak hata alıyordum çünkü while false çeviriyordu. ona önlem amacıyla şu koşulu oluşturdum.
        break

    cv2.imshow("Vizontele",frame)
    if cv2.waitKey(6) & 0xFF ==ord ('q'):
        break


cap.release() 
cv2.destroyAllWindows()