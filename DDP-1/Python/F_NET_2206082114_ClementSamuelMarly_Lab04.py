#print perkenalan
print("Selamat datang di Pacil Mart!")
print()
Nama_File_input = input("Masukkan  nama file input :")

#catatan: saya memakai directory tempat menaruh file python agar bisa bekerja atau file ketemu, jadi mungkin directory harus diubah sesuai dengan file tester
#Apabila file tidak ditemukan
try:
    File_input = open(f"C:\\Users\\cleme\\OneDrive\\Documents\\Code\\Python\\{Nama_File_input}.txt","r")
except FileNotFoundError:
    print ("File tidak ditemukan atau salah nama file")
    exit()

#Apabila file kosong
if File_input.read() == "":
    print("File input kosong")
    exit()

#Buka File dan split file berdasarkan enter (dipisahkan setiap line)
File_input = open(f"C:\\Users\\cleme\\OneDrive\\Documents\\Code\\Python\\{Nama_File_input}.txt", "r")
List = File_input.read()

#print tabel
print("Berikut adalah daftar belanjaanmu:")
print()

#set tabel dengan align kanan atau kiri
print(f"{'Nama':<12}|{'Jumlah':>8}|{'Kembalian':>10}")
print("—-------------------------------")

#print harga, barang, dan kembalian sekaligus menghitung
#loop i sampai total line di dalam file
for i in List.split("\n"):
    #split 1 line menjadi tiga bagian, barang, berapa banyak yang dibeli, dan kembalian
    Barang = i.split()[0]
    Pembelian = int(i.split()[1]) // int(i.split()[2])
    Kembalian = int(i.split()[1]) % int(i.split()[2])
    print(f"{Barang:<12}|{Pembelian:>8}|{Kembalian:>10}")
    #reset variabel
    Barang = ""
    Pembelian = 0
    Kembalian = 0

# menutup file
File_input.close()
#print akhiran file
print()
print("Terima kasih sudah belanja di Pacil Mart!")

    
    

