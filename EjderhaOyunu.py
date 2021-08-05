import random
import time

def baslangic():    

    print("Çok uzak diyarlarda yüksek surların ardında bulunan bir şehir varmış...")
    time.sleep(2)
    print("Bu şehrin mutlu olan ve huzur içinde yaşayıp giden bir halkı varmış. Fakat bir gün...")
    time.sleep(2)
    print("Şehre giriş yapılan iki kapısınında önüne iki ejderha yerleşmiş. Bu ejderhaların biri iyi biri kötü imiş...")
    time.sleep(2)
    print("Şimdi sen bu kapılardan birini seçmen gerek...")
    time.sleep(2)
    print("Seçimin nedir ?")
    
def secim_yap():
    secim=int(input("Seçim senin: 1'inci kapımı ?: 2'inci kapımı ?:"))
    return secim

def ilerle(x):
    print("Yola çıktın bakalım ")
    time.sleep(2)
    print("Seçim senin...")
    time.sleep(2)
    
    if x==random.randint(1,2):
        print("Doğru seçim tebrikler")
        print("Şehre girmeyi başardın...")
    else:
        print("Yanlış tercih yaptın bu seçim senin için iyi olmadı dostum üzgünüm...")
        print("Oyunu kaybettin birdahaki sefere... Hadi bakalım...")
        
while True:
    baslangic()
    x_name = secim_yap()
    ilerle(x_name)
    cevap = input("Oyundan çıkmak istermisin ? hayır=>1 : , evet=>2 : ")
    if cevap=="1":
        print("Oyun devam ediyor...")
    else:
        print("Oyun bitti")
        break
        
        
