a = input("Lütfen Kelime veya Cümle Giriniz.").lower()
liste = list()
for i in a:
        liste.append("{} harfi {} defa geçiyor".format(i,a.count(i)))

liste = list(dict.fromkeys(liste))
print(liste)
