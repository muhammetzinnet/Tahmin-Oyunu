
from random import choice

degerler = ["taş","kağıt","makas"]


while True:
    
    kullanici = str(input("Tercihin ne ? Taş mı?, Kağıt mı?, Makas mı? "))
    kullanici = kullanici.lower()
    bilgisayar = choice(degerler)
    
    if kullanici == "taş":
        if bilgisayar == "taş":
            print("Berabere bitti")
        elif bilgisayar == "kağıt":
            print("Kağıt taşı sarar kaybettiniz")
        elif bilgisayar == "makas":
            print("Taş makası ezer kazandınız")
    elif kullanici == "kağıt":
        if bilgisayar == "taş":
            print("Kağıt taşı sarar kazandınız")
        elif bilgisayar == "kağıt":
            print("Berabere bitti")
        elif bilgisayar == "makas":
            print("Makas kağıdı keser kaybettiniz")
    elif kullanici == "makas":
        if bilgisayar == "taş":
            print("Taş makası ezer kaybettiniz")
        elif bilgisayar == "kağıt":
            print("Makas kağıdı keser kazandınız")
        elif bilgisayar == "makas":
            print("Berabere bitti")
    else:
        print("Yanlış secim yaptınız...")
        
    
    karar = input("Oyuna devap etmek istiyormusunuz ? evet =>1, hayır=>2 : ")
    if karar == "1":
        print("Oyuna devam ediyorsunuz")
    elif karar == "2":
        print("Oyun sonlandırılıyor görüşmek üzere")
        break
    else:
        print("Yanlış seçim yaptınız lütfen kontrol ederek tekrar seçim yapınız.")
    

