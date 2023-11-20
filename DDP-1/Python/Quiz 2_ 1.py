nama = input("Masukkan nama :")
Nama_terpisah = nama.split(" ")

print (f"{Nama_terpisah[len(Nama_terpisah)- 1]}, ", end = "")

for i in range (len(Nama_terpisah) - 1) :
    x = Nama_terpisah[i]
    print (f"{x[0:1]}.", end = " ")
