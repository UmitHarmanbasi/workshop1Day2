vize = int(input("Vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
ortalama = (vize * 0.4) + (final * 0.6) 

# eğer final 40'dan küçükse kullanıcı kaldı
# eğer ortalama 50'den küçükse kullanıcı kaldı
# eğer vize finalin 2 katı ise kullanıcı kaldı
# bunun dışındaki tüm durumlarda kullanıcı geçti yazdırmak istiyoruz.

if vize < 40:
    print("Kaldınız")
elif (vize*0.4+final*0.6) <50:
    print ("Kaldınız")
elif (vize/final) ==2:
    print("Kaldınız")
else:
    print("Kullanıcı Geçti")