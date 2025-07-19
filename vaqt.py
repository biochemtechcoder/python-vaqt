def vaqt():       #O'zgaruvchi yaratish
 """Bu o'zgaruvchi vaqtni hisoblash va Taymer funksiyasiga ega."""
def vaqt():       #Funksiya yaratish
 """Bu funksiya vaqtni hisoblash va Taymer funksiyasiga ega."""
 while True:
    import time
    from datetime import datetime

    print(f"Hozirgi vaqtni bilish uchun [1]ni \nTaymerga o'tish uchun [2]ni yozing \ntugatmoqchi bo'lsanggiz 'exit' deb yozing. ")
    
    tanlov = input('Tanlovni yozish uchun >>> ')        #Tanlovni qabul qilish
    
    if tanlov == 'exit':                 #Tanlov exit ga teng yoki yo'qligini tekshirish
        print("Dastur to'xtadi.")  #Agar exit ga teng bo'lsa dasturni tugatish
        break

    if tanlov == '1':          
        hozir = datetime.now()
        print('Hozirgi vaqt:', hozir.strftime('%H:%M:%S'))  #Hozirgi vaqt ni formatlash
        
    
    elif tanlov == '2':
        sekund = int(input('Necha soniya taymer: '))
        while sekund > 0:
            print('Qolgan:', sekund, 's')
            time.sleep(1)                     #Taymer efekti
            sekund -= 1             #Sekundni bittaga kamaytirish
        print('Taymer tugadi.')
    
    else:
        print('Xato tanlov')       #Tanlov xato kiritilganda
vaqt()     #O'zgaruvchini terminalga chiqarishvaqt()     #Funksiyani terminalga chiqarish