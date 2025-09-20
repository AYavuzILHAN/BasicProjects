import cv2
import numpy as np

kamera = cv2.VideoCapture(0) # Bilgisayar kamerasını başlatır diğer sayısal değerler harici kameraları temsil eder.

width = int(kamera.get(cv2.CAP_PROP_FRAME_WIDTH))  # Kameranın genişliğini alır.
height = int(kamera.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Kameranın yüksekliğini alır.

print(f"Video çözünürlüğü: {width}x{height}")

video_writer = cv2.VideoWriter('Video Kaydı.mp4', cv2.VideoWriter_fourcc(*'MP4V'), 20.0, (width, height)) # width ve height'ı elle de yazabiliriz. Video kaydetmek için VideoWriter nesnesi oluşturur. 'XVID' codec'i kullanılır, 20 FPS hızında ve 640x480 çözünürlükte.

while True:   # mantık olarak resimleri sürekli alır ve gösterir bu zaten bir video akışıdır.

    ret, frame = kamera.read() # ret kameranın çalışıp çalışmadığını kontrol eder, frame ise kameradan alınan görüntüyü temsil eder.
    
    video_writer.write(frame)  # Alınan her kareyi video dosyasına yazar.

    if not ret:
        break


    cv2.imshow("Video", frame) # kameradan alınan görüntüyü ekranda gösterir.

    if cv2.waitKey(250) & 0xFF == ord('q'):
        break


kamera.release()
video_writer.release()
cv2.destroyAllWindows()
