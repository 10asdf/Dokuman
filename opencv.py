import cv2 #opencv modülü dahil edilir
 
resim= cv2.imread("foto.jpg") #İstenilen resim dahil edilir
casc=cv2.CascadeClassifier('haarcascade_frontalface_default.xml') #İstenilen sınıf dahil edilir

gray = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY) #Daha iyi bir sonuç için görüntümüzü dahil ediyoruz
faces=casc.detectMultiScale(gray, 1.9, 3) #Görüntü nümerik değerler ile ayarlanır.

for (x, y, w, h) in faces: #Dikdörtgen çizmek için köşe ayarları yapılır
    cv2.rectangle(resim, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("BASLIK",resim) #Görüntüyü gösterir
cv2.waitKey(0)
