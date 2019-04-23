from tkinter import *
from tkinter import messagebox
import fonksiyonlar as fonk
import io
import os
from google.cloud import vision
from google.cloud.vision import types

def goruntu():

    try:

        sec= yazi.get()

        if(sec!=""): #Seçilen dosya adı null değilse
            img=fonk.resimAc(sec)  #Resim Açma İşlemi
            img_gray=fonk.griyecevir(img)  #griye cevirme fonk
            gurultuazalt=fonk.gurultuAzalt(img_gray) #Gurultu azaltma fonksiyonu
            h_esitleme=fonk.histogramEsitleme(gurultuazalt) #Histogram Eşitleme
            morfolojik_resim=fonk.morfolojikIslem(h_esitleme) #Morfolojik islem
            goruntucikarma=fonk.goruntuCikarma(h_esitleme,morfolojik_resim) #Goruntu Çıkarma İşlemi
            goruntuesikleme=fonk.goruntuEsikle(goruntucikarma)  ##Goruntu Eşikleme İşlemi
            cannedge_goruntu=fonk.cannyEdge(goruntuesikleme)     #Canny_Edge İşlemi
            gen_goruntu=fonk.genisletmeIslemi(cannedge_goruntu)  #Dilated (Genişletme İşlemi)
            screenCnt=fonk.konturIslemi(img,gen_goruntu)                   #Kontur İşlemi
            yeni_goruntu=fonk.maskelemeIslemi(img_gray,img,screenCnt)    #Maskeleme İşlemi
            #fonk.plakaIyilestir(yeni_goruntu)   #Maskelenmiş görüntü üzerinde işlemler.
            fonk.plakayaz()
            plakayaz()

            fonk.cv2.waitKey()  # Bir tuşa basarsan pencereyi kapatır.
    except :
        print("Lütfen Resim adını kontrol ediniz...")

def plakayaz():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"
    client = vision.ImageAnnotatorClient()
    #Yeni klasörüne kaydedilen a.jpg resmini işleme sokup plakayı yazdırma
    file_name = os.path.join(os.path.dirname(__file__), "Yeni/a.jpg")

    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)
    response2 = client.text_detection(image=image)
    texts = response2.text_annotations
    sayac=0
    for text in texts:
        sayac=sayac+1
        if(sayac==1):
            etiket["text"] = text.description
            messagebox.showinfo("Resimdeki Plaka", etiket["text"])
            break


pencere = Tk()
pencere.title("Plaka Tanıma Sistemi")
pencere.geometry("450x200+350+40")

yazi = Entry()
yazi.pack()

buton = Button(text="Plaka Oku", command=goruntu)
buton.pack()

yazi2= Label(text="Resimdeki Plaka")
yazi2.pack()

etiket = Label(text="")
etiket.pack()

mainloop()
