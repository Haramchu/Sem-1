#Inisiasi variabel yang dibutuhkan
user_active = False
user_membership = False
total_harga = 0

# Loop selama toko masih buka
store_open = True
while store_open:
    # Menerima permintaan pengguna
    print("Selamat Datang di Toko Buku Place Anak Chill")
    print("============================================")
    print("1. Pinjam buku")
    print("2. Keluar")   
    print("============================================")
    action = input("Apa yang ingin anda lakukan: ").lower()
    # Proses permintaan pinjam buku
    if action == "1":
        # Proses permintaan data pengguna
        user_active = True
        user_name = input("Masukkan nama anda: ")
        user_saldo = int(input("Masukkan saldo anda (Rp): "))
        user_status = input("Apakah anda member? [Y/N]: ").lower()
        
        # Verifikasi user member
        if user_status == "y":
            jumlah_id_salah = 0
            for loop in range(3):
                sum = 0
                user_id = input("Masukkan ID anda: ")
                for num in user_id:
                    sum += int(num)
                if sum == 23: #Membandingkan sum dengan kode unik
                    user_membership = True
                    print("Login member berhasil!")
                    break
                else: # Alur salah memasukkan ID
                    jumlah_id_salah += 1
                    print("ID anda salah!")
            if jumlah_id_salah == 3: # Kesalahan ID melewati batas (3)
                print("Program akan kembali ke menu utama")
                user_active = False
                continue

        else: #Login sebagai non-member
            print("Login non-member berhasil!")
            
            
        # Alur peminjaman buku
        while user_active:
            print("\n============================================")
            print("Katalog Buku Place Anak Chill")
            print("============================================")
            print("X-Man (Rp 7.000/hari)\nDoraemoh (Rp 5.500/hari)\nNartoh (Rp 4.000/hari)")
            print("============================================")
            print("Exit")
            print("============================================")

            user_book = input("Buku yang dipilih: ")

            if user_book.lower() == "exit": #Keluar dari peminjaman buku
                print()
                break
            #Penghitungan harga peminjaman buku
            durasi = int(input("Ingin melakukan peminjaman untuk berapa hari: "))

            if user_book.lower() == "x-man":
                total_harga = (durasi * 7000)
            elif user_book.lower() == "doraemoh":
                total_harga = (durasi * 5500)
            elif user_book.lower() == "nartoh":
                total_harga = (durasi * 4000)
            else:
                print("Komik tidak ditemukan. Masukkan kembali judul komik sesuai katalog!")
                continue

            if user_membership: #Diskon member
                total_harga *= 0.8
            if user_saldo >= total_harga: # Pembelian berhasil saat saldo cukup
                user_saldo -= total_harga
                print(f"Berhasil meminjam buku {user_book} selama {durasi} hari")
                print(f"Saldo anda saat ini Rp{user_saldo}\n")
            else: #Pembelian tidak berhasil
                print(f"Tidak berhasil meminjam! Saldo anda kurang {(total_harga-user_saldo)}\n")

    elif action == "2":  #Keluar dari program
        break
    else:
        print("Perintah tidak diketahui!\n")

print("Terima kasih telah mengunjungi Toko Buku Place Anak Chill!")