class Ogr_system():
    
    def __init__(self,ogrNo,sifre,ad,soyad,dersler,bölüm,devamsızlık,girisyılı,vize,final):
        self.ogrNo= ogrNo
        self.sifre= sifre
        self.ad = ad
        self.soyad = soyad
        self.dersler = dersler
        self.bölüm= bölüm
        self.devamsızlık= devamsızlık
        self.girisyılı= girisyılı
        self.vize = vize
        self.final = final
        
    def bilgi_göster(self):
        print("""
             Öğrenci No: {} 
             Şifre : {}
             Ad : {}
             Soyad : {}
             Dersler : {}
             Bölüm : {}
             Devamsızlık : {}
             Giriş Yılı : {}
             Vize Notu : {}
             Final Notu : {}
              """.format(self.ogrNo,self.sifre,self.ad,self.soyad,self.dersler,self.bölüm,self.devamsızlık,self.girisyılı,self.vize,self.final))
    
    def ders_ekle(self,ders):
        self.ders = ders
        print("Ders Eklendi")
        self.dersler.append(ders)
    
    def sifre_degis(self):
        a = input("Lütfen Eski Şifrenizi Giriniz: ")
        if(a == self.sifre):
            yeni_sifre= input("Lütfen Yeni Şifrenizi Giriniz")
            self.sifre= yeni_sifre
        else:
            print("Hatalı şifre, şifrenizi değiştirmek için tekrar deneyiniz")
    
    def ders_sil(self,ders):
        self.ders = ders
        print("Ders Silindi")
        self.dersler.remove(ders)
    
    def harf_notu(self):
        ort = (self.vize*0.4) + (self.final*0.6) 
        print("Ortalamanız = ", ort)
        if(90<ort<101):
            print("Harf Notunuz: AA")
        elif(80<ort<90):
            print("Harf Notunuz: BA")
        elif(70<ort<80):
            print("Harf Notunuz: BB")
        elif(60<ort<70):
            print("Harf Notunuz: BC")
        elif(50<ort<60):
            print("Harf Notunuz: CC")
        elif(0<ort<50):
            print("Harf Notunuz: FF")
        else:
            print("Ortalamanız hesaplanamadı değerlerinizi kontrol ediniz.")
