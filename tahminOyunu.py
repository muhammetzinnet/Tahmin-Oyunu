
from random import choice
import pandas as pd

data = pd.read_csv("TR_ŞEHİRLER.csv",encoding="UTF-8")

sehir_isimleri = data["BASLIK"]

rasgele_sehir = choice(sehir_isimleri)

harf_sayisi = len(rasgele_sehir)

print("Tahmin Oyunumuza Hoşgeldiniz...")
print("{} harflidir".format(harf_sayisi))
print("Şehrimizin ilk harfi => {}".format(rasgele_sehir[0]))

deneme_sayisi = 3

while True:

    cevap = input("Şehriniz nedir : ")
    
    if cevap.lower() == rasgele_sehir.lower():
        print("Harika başardın...")
        tekrar = input("Oyuna devam itmek istermisin...Evet ise 1... Hayır ise 0 basın")
        if tekrar == "0":
            print("Tekrar görüşürüz By By")
            break
        elif tekrar == "1":
            print("Bu sefer yapabilirsin hadi başlayalım...")
            rasgele_sehir = choice(sehir_isimleri)
            harf_sayisi = len(rasgele_sehir)
            print("{} harflidir".format(harf_sayisi))
            print("Şehrimizin ilk harfi => {}".format(rasgele_sehir[0]))
            continue
        else:
            print("Yanlış tercih... 1 veya 0 basın")
    else:
        print("Ah!!! Nerdeyse oluyordu...")
        deneme_sayisi-=1
        print("Bir hakkın kayboldu biraz daha düşünerek cevap ver :( {} hakkın kaldı..".format(deneme_sayisi))
        
        if deneme_sayisi < 1:
            print("Maalesef başaramadın. Tekrar denemek istermisin?")        
            tekrar = input("...Evet ise 1... Hayır ise 0 basın\n")
            if tekrar == "0":
                print("Tekrar görüşürüz By By")
                break
            elif tekrar == "1":
                print("Bu sefer yapabilirsin hadi başlayalım...")
                rasgele_sehir = choice(sehir_isimleri)
                harf_sayisi = len(rasgele_sehir)
                print("{} harflidir".format(harf_sayisi))
                print("Şehrimizin ilk harfi => {}".format(rasgele_sehir[0]))
                continue
            else:
                print("Yanlış tercih... 1 veya 0 basın")
        
        
        
        
        
        
        
        
        
        