import math
Nama = input("Nama : ")
n = float(input("Panjang persegi nametag (cm) : "))
m = float(input("Panjang trapesium nametag (cm) : "))
banyak_nametag = float(input("Banyak nametag : "))

Setengah_lingkaran = round((math.pi * ((n /2)** 2) / 2), 2)
Persegi = round((n * n), 2)
Segitiga = round(((n * n) / 2), 2)
Trapesium = round(((n + m) * n / 2), 2)

Setengah_lingkaran = float(Setengah_lingkaran)
Persegi = float(Persegi)
Segitiga = float(Segitiga)
Trapesium = float(Trapesium)

Luas_1_nametag = (Setengah_lingkaran + Persegi + Segitiga + Trapesium)
Luas_total_nametag = round((banyak_nametag * Luas_1_nametag), 2)
Uang = Luas_total_nametag * 4 / 10
Uang = math.ceil(Uang/1000) * 1000

print ()
print ("Halo", Nama, "! Berikut informasi terkait nametag kamu :")
print ()
print ("Luas 1 nametag :", Luas_1_nametag, "cm^2")
print ("Luas total nametag :", Luas_total_nametag, "cm^2")
print ("Uang yang diperlukan : Rp", Uang)
