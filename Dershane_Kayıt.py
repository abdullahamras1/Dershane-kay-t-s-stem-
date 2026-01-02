for i in range(20):
    print(f"\n{i+1}. Öğrenci Kaydı")
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    yas = int(input("Yaş: "))
    ilce = input("İlçe: ")

    ogrenci = {
        "isim": isim,
        "soyisim": soyisim,
        "yas": yas,
        "ilce": ilce
    }

ogrenciler.append(ogrenci)