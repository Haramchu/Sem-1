#input nama file yang ingin dibuka
Nama_1= input("Masukkan nama file:")
Nama_2= input("Masukkan nama file:")
#buka file untuk baca
File_1 = open(f"C:\\Users\\cleme\\OneDrive\\Documents\\Code\\Python\\{Nama_1}.txt","r")
File_2 = open(f"C:\\Users\\cleme\\OneDrive\\Documents\\Code\\Python\\{Nama_2}.txt","r")
#buat file baru dengan nama merged
File_baru = open(f"C:\\Users\\cleme\\OneDrive\\Documents\\Code\\Python\\{Nama_1}_{Nama_2}_merged.txt","w")
#baca isi file pertama dan kedua
Isi_1 = File_1.readline()
Isi_2 = File_2.readline()
#tulis isi file pertama dan kedua di file baru merged
File_baru.write (f"{Isi_1}\n")
File_baru.write (f"{Isi_2}")
#tutup file
File_1.close()
File_2.close()
File_baru.close()

f.close()

for i in range (total_list) :
    List = File_input.readline()
    print(List)
    List2 = List.split(" ")
    print(f"{List2[0]}       ", end="")
    if List2[2] <= 0 :
        print("Harga satuan barang dijamin lebih besar dari 0")
    elif List[1] <= 0 :
        print("Uang yang dialokasikan harus lebih besar dari 0")
    else :
        Jumlah = int(List2[1]) // int(List2[2])
        Kembalian = int(List2[1]) % int(List2[2])
        print(f"  {Jumlah}|   ")
        print(f"{Kembalian}")
    Jumlah = 0
    Kembalian = 0
    List2 = ""
    List1 = ""
