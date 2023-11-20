print ("Selamat datang di program Mengenal Angkatan!")
print ("============================================")
print ("Masukkan Identitas Mahasiswa : (Nama NPM - Tanggal Bulan Tahun)")
#setup loop
STOP = False
Kumpulan_data = []
Buku_npm = {}
Buku_data = {}
#buat loop untul list
while STOP == False :
    data = input()
    if data == "STOP":
        STOP = True
        continue
    Kumpulan_data.append(data)
#buka loop untuk update dictionary apabila hanya 1 input

if len(Kumpulan_data) == 1 :
    Data_mahasiswa = Kumpulan_data[0].split(" ")
    Nama = Data_mahasiswa [0]
    Bulan = Data_mahasiswa [4]
    npm = Data_mahasiswa [1]
    Buku_data.update({Bulan:Nama})
    Buku_npm.update({Bulan:npm})
#buka loop untuk dictionary lebih dari 1 input
else :
    #ambil nama, npm, bulan
    for i in (0,len(Kumpulan_data)) :
        Data_1 = Kumpulan_data[i-1]
        Data_2 = Data_1.split(" ")
        Nama = Data_2[0]
        npm = Data_2[1]
        Bulan = Data_2[4]
        #apabila ada nama atau npm sama
        if Bulan in Buku_data :
            if Nama in Buku_data:
                continue
            Nama_2 = Buku_data[Bulan]
            Buku_data.update ({Bulan:{Nama,Nama_2}})
        if Bulan in Buku_npm :
            if npm in Buku_npm:
                continue
            npm_2 = Buku_npm[Bulan]
            Buku_npm.update ({Bulan:{npm,npm_2}})
        #update dictionary
        Buku_data.update({Bulan:Nama})
        Buku_npm.update({Bulan:npm})

#print output
bulan = input("Cari mahasiswa berdasarkan bulan:" )
jumlah_1 = 0
jumlah_2 = 0
for bulan in Buku_data :
    jumlah_1 = jumlah_1+1
for npm in Buku_npm :
    jumlah_2 = jumlah_2+1
print ("===================Hasil================")
print (f"Terdapat {jumlah_1} nama yang lahir di bulan {bulan}:")
print (Buku_data[bulan])
print (f"Terdapat {jumlah_2} NPM yang lahir di bulan {bulan}:")
print (Buku_npm[npm])
print ("Terima kasih telah menggunakan program ini, semangat PMB-nya")
