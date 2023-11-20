print("Selamat datang ke Dek Depe Holiday Tracker!")
print()
jumlah_wisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
#meminta input jumlah wisata dan apabila tidak valid
while (jumlah_wisata < 1):
    print ("Input tidak valid. Silahkan masukkan input kembali!")
    jumlah_wisata = int(input("Masukkan banyak tempat wisata yang kamu kunjungi: "))
print()
#set variable rating awal untuk summary
Rating_total = int(0)
Rating_max = int(0)
#meminta tempat perjalanan dan ratingnya
for i in range (1, jumlah_wisata + 1):
    Perjalanan = input(f"Perjalanan {i}: ")
    Rating = int(input(f"Rating perjalanan kamu ke {Perjalanan} (indeks 1-10) : "))
    print()
    #Total rating untuk mendapatkan rata - rata rating
    Rating_total = Rating + Rating_total
    #Mendapatkan tempat dengan rating paling tinggi untuk summary
    if (Rating >= Rating_max) :
        Rating_max = Rating
        perjalanan_paling_menyenangkan = Perjalanan
#Rata - rata rating
Rating_akhir = Rating_total / jumlah_wisata
#Print akhir
print("---Summary---")
print(f"Perjalanan paling mengesankan adalah ketika pergi ke {perjalanan_paling_menyenangkan}")
print("Skala kebahagiaan Dek Depe adalah %.2f"% Rating_akhir)

if (8<= Rating_akhir <= 10) :
    print("Dek Depe bahagia karena pengalamannya menyenangkan.")
elif (5<= Rating_akhir < 8) :
    print("Dek Depe senang karena pengalamannya cukup baik.")
else :
    print("Dek Depe sedih karena pengalamannya buruk.")

print()
print("Terimakasih telah menggunakan Dek Depe Holiday Tracker!")





    

