#setup semua variabel, dictionary, dan list yang dibutuhkan
stop = False
list_meja = [1,2,3,4,5,6,7,8,9,10]
daftar_pesanan_meja = {}
daftar_nama_makanan_ke_harga = {}
daftar_kode_makanan_ke_nama_makanan = {}
inverse_daftar_kode_makanan_ke_nama_makanan = {}
daftar_harga_pesanan = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}
daftar_jumlah_pesanan = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}
daftar_nama_meja = {}
menu = []
list_menu_check_duplicate = []
set_menu_check_duplicate = set()
#open file menu.txt dan membaca
file_open = open("menu.txt")
file_read = file_open.readlines()
#function menu tidak valid
def menu_not_valid () :
    print ("Daftar menu tidak valid, cek kembali menu.txt")
    exit ()
#untuk mendapatkan menu yang berupa list
for file_line in file_read :
    line_checker = file_line
    file_line = file_line.strip().split(";")
    #pengecekan apabila format menu tidak benar (hanya terdapat 3 index setelah ; dislice)
    if len(file_line) == 1 :
        file_line[0] = file_line[0].strip("===")
        file_line[0] = f"{file_line[0]} : \n"
    #strip === dari menu.txt
    if len(file_line) == 2 or len(file_line) >=4 :
        menu_not_valid()
    #mencegah subjudul menu dicoba untuk diambil indexnya, dan terjadi index error
    elif len(file_line) == 3 :
        file_line[0] = file_line[0]
        kode_menu = file_line[0]
        nama_makanan = file_line[1]
        Harga = file_line [2]
        file_line.append ("\n")
        #apabila yang diinput di bagian harga bukan angka
        try :
            int (Harga)
        except ValueError :
            menu_not_valid()
        #apabila nama makanan hanya mengandung angka (dianggap tidak ada nama makanan yang berupa angka)
        try :
            if type(int(nama_makanan)) == int :
                menu_not_valid()
        except ValueError :
            pass
        #memasukkan semua kode menu, nama makanan, dan harga ke list atau dictionary yang diperlukan (nama dictionary sesuai kegunaan)
        daftar_nama_makanan_ke_harga[nama_makanan] = Harga
        daftar_kode_makanan_ke_nama_makanan[kode_menu] = nama_makanan
        list_menu_check_duplicate.append(nama_makanan)
        set_menu_check_duplicate.add(nama_makanan)
        #validasi menu untuk file nama makanan yang ada dua atau lebih
        if len(list_menu_check_duplicate) == len(set_menu_check_duplicate) :
            pass
        else :
            menu_not_valid()
        #untuk bagian receipt dimana diperlukan kembali kode menu
        inverse_daftar_kode_makanan_ke_nama_makanan[nama_makanan] = kode_menu 
    #menggabungkan kembali isi menu menjadi suatu menu
    for char in file_line :
        menu.append(char)
#apabila menu kosong atau dictionary kosong
if menu == [] or daftar_nama_makanan_ke_harga == {} or daftar_kode_makanan_ke_nama_makanan == {}:
    print ("Menu kosong, cek kembali menu.txt")
    exit ()
#buka loop meminta input
while stop == False :
    print ("------------------------------------")
    print ("Selamat datang di Kafe Daun Pacilkom")
    perintah = input("Apa yang ingin Anda lakukan? (BUAT PESANAN, UBAH PESANAN atau SELESAI MENGGUNAKAN MEJA) ")
    #reset total harga tiap customer
    total_harga = 0
    harga = 0
    #apabila customer ingin buat pesanan
    if perintah == "BUAT PESANAN" :
        if list_meja == [] :
            print ("Mohon maaf meja sudah penuh, silakan kembali nanti.")
            continue
        nama = input("Siapa nama Anda? ")
        #mencegah adanya nama yang sama
        if nama in daftar_nama_meja.values() :
            print (f"Nama {nama} telah digunakan, gunakan nama lain.")
            print ()
            continue
        #memasukkan nama ke dictionary untuk mengetahui siapa yang menggunakan meja tersebut
        daftar_nama_meja[list_meja[0]] = nama
        print ()
        print ("Berikut ini adalah menu yang kami sediakan : ")
        #print isi menu yang telah digabungkan
        print (end = " ")
        for isi in menu : 
            print (isi, end = " ")
        print ()
        #meminta pesanan customer
        pesanan = input("Masukkan menu yang ingin anda pesan : ")
        #membuka loop agar customer bisa terus memesan
        while pesanan != "SELESAI" :
            #reset jumlah pesanan atau harga pesanan tiap customer
            jumlah_pesanan = 0
            harga_pesanan = 0
            #mengubah kode makanan ke nama makanan untuk memudahkan customer mengetahui apa yang dipesan dan pemanggilan dictionary lain
            if pesanan in daftar_kode_makanan_ke_nama_makanan :
                pesanan = daftar_kode_makanan_ke_nama_makanan[f"{pesanan}"]
            #apabila pesanan telah ada di daftar pesanan customer, dictionary diupdate dimana jumlah pesanan atas suatu makanan ditambah 1
            if f"{pesanan}" in daftar_jumlah_pesanan[list_meja[0]].keys() :
                jumlah_pesanan = daftar_jumlah_pesanan[list_meja[0]][pesanan] + 1
                daftar_jumlah_pesanan[list_meja[0]].update({pesanan:jumlah_pesanan})
                pesanan = input (f"Berhasil memesan {pesanan}. Masukkan menu yang ingin Anda pesan : ")
            #apabila pesanan belum ada di daftar pesanan customer, tetapi ada di menu
            elif pesanan in menu :
                jumlah_pesanan = 1
                #input dictionary jumlah pesanan dan harganya dalam dictionary meja customer
                daftar_jumlah_pesanan[list_meja[0]][pesanan] = jumlah_pesanan
                daftar_harga_pesanan[list_meja[0]][pesanan] = daftar_nama_makanan_ke_harga[f"{pesanan}"]
                pesanan = input (f"Berhasil memesan {pesanan}. Masukkan menu yang ingin Anda pesan : ")
            #apabila pesanan tidak ada di menu
            else :
                pesanan = input (f"Menu {pesanan} tidak ditemukan. Masukkan menu yang ingin Anda pesan : ")
        print ()
        #apabila customer tidak memesan apapun atau dictionary jumlah pesanan kosong
        if daftar_jumlah_pesanan[list_meja[0]] == {} :
            #mengosongkan kembali nama customer pada suatu meja
            del daftar_nama_meja[list_meja[0]]
            print ("Anda tidak memesan apa - apa")
        #menghasilkan output pesanan customer beserta total harga
        else :
            print ("Berikut adalah pesanan Anda:")
            for key in daftar_jumlah_pesanan[list_meja[0]] :
                harga = daftar_jumlah_pesanan[list_meja[0]][key] * int(daftar_harga_pesanan[list_meja[0]][key])
                print (f"{key} {daftar_jumlah_pesanan[list_meja[0]][key]} buah, total Rp{harga}") 
                total_harga = harga + total_harga
            print ()
            print (f"Total pesanan : Rp{total_harga}")
            #mengambil meja pertama yang belum digunakan dalam list meja yang tersedia
            print (f"Pesanan akan kami proses, Anda bisa menggunakan meja nomor {list_meja.pop(0)}. Terima kasih.")
    #apabila perintah ubah pesanan
    elif perintah == "UBAH PESANAN" :
        #meminta nomor meja dan memvalidasi nomor meja (1-10, meja belum digunakan, dan berupa int)
        try :
            nomor_meja = int(input("Nomor meja berapa? "))
        except ValueError :
            print ("Nomor meja kosong atau tidak sesuai (1-10), silahkan ulang kembali")
            continue
        if nomor_meja <= 0 or nomor_meja > 10 :
            print ("Nomor meja kosong atau tidak sesuai (1-10), silahkan ulang kembali")
            continue
        if nomor_meja in list_meja :
            print ("Anda belum memesan, silahkan pesan terlebih dahulu")
            continue
        print ("Berikut ini adalah menu yang kami sediakan :")
        #print isi menu
        print (end = " ")
        for isi in menu : 
            print (isi, end = " ")
        print ()
        #mengambil data pesananan customer dari dictionary meja customer
        print ("Berikut adalah pesanan Anda :")
        for key in daftar_jumlah_pesanan[nomor_meja] :
            harga = daftar_jumlah_pesanan[nomor_meja][key] * int(daftar_harga_pesanan[nomor_meja][key])
            print (f"{key} {daftar_jumlah_pesanan[nomor_meja][key]} buah, total Rp{harga}") 
        print ()
        #meminta perintah dari customer dan membuka loop sampai ditulis selesai
        perintah_2 = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
        while perintah_2 != "SELESAI" :
            #reset jumlah pesanan dan harga
            jumlah_pesanan = 0
            harga_pesanan = 0
            #apabila customer ingin ganti jumlah
            if perintah_2 == "GANTI JUMLAH" :
                makanan_yang_diganti = input("Menu apa yang ingin Anda ganti jumlahnya : ")
                #mengubah kode menu menjadi nama makanan untuk mempermudah customer dan memanggil dictionary lain
                if makanan_yang_diganti in daftar_kode_makanan_ke_nama_makanan :
                    makanan_yang_diganti = daftar_kode_makanan_ke_nama_makanan[f"{makanan_yang_diganti}"]
                #apabila makanan yang ingin diganti tidak ada di menu
                if makanan_yang_diganti not in menu :
                    perintah_2 = input(f"Menu {makanan_yang_diganti} tidak ditemukan. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                #apabila makanan yang ingin diganti belum dipesan
                elif makanan_yang_diganti not in daftar_jumlah_pesanan[nomor_meja].keys() :
                    perintah_2 = input(f"Menu {makanan_yang_diganti} tidak anda pesan sebelumnya. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                #mengganti jumlah makanan telah dipesan sesuai dengan keinginan pengguna
                elif makanan_yang_diganti in daftar_jumlah_pesanan[nomor_meja].keys() :
                    jumlah_makanan_baru = int(input("Masukkan jumlah pesanan yang baru : "))
                    #validasi agar jumlah makanan yang diinput tidak lebih kecil dari 0
                    if jumlah_makanan_baru <= 0 :
                        perintah_2 = input("Jumlah harus bilangan positif! Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                    daftar_jumlah_pesanan[nomor_meja].update ({makanan_yang_diganti:jumlah_makanan_baru})
                    perintah_2 = input (f"Berhasil mengubah pesanan {makanan_yang_diganti} {jumlah_makanan_baru} buah. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            #apabila customer ingin menghapus suatu pesanan
            elif perintah_2 == "HAPUS" :
                makanan_yang_dihapus = input("Menu apa yang ingin Anda hapus dari pesanan : ")
                #mengubah kode menu menjadi nama makanan untuk mempermudah customer dan memanggil dictionary lain
                if makanan_yang_dihapus in daftar_kode_makanan_ke_nama_makanan :
                    makanan_yang_dihapus = daftar_kode_makanan_ke_nama_makanan[f"{makanan_yang_dihapus}"]
                #apabila makanan yang ingin diganti tidak ada di menu
                if makanan_yang_dihapus not in menu :
                    perintah_2 = input(f"Menu {makanan_yang_dihapus} tidak ditemukan. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                #apabila makanan yang ingin diganti belum dipesan
                elif makanan_yang_dihapus not in daftar_jumlah_pesanan[nomor_meja].keys() :
                    perintah_2 = input(f"Menu {makanan_yang_diganti} tidak anda pesan sebelumnya. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                #menghapus pesanan yang diminta customer
                elif makanan_yang_dihapus in daftar_jumlah_pesanan[nomor_meja].keys() :
                    jumlah_makanan_awal = daftar_jumlah_pesanan[nomor_meja][makanan_yang_dihapus]
                    #menghapus dictionary yang berisi pesanan yang ingin dihapus customer
                    del daftar_jumlah_pesanan[nomor_meja][makanan_yang_dihapus]
                    perintah_2 = input(f"{jumlah_makanan_awal} buah {makanan_yang_dihapus} dihapus dari pesanan. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            #apabila customer ingin menambah pesanan
            elif perintah_2 == "TAMBAH PESANAN" :
                makanan_yang_ditambah = input("Menu apa yang ingin dipesan : ")
                #mengubah kode menu menjadi nama makanan untuk mempermudah customer dan memanggil dictionary lain
                if makanan_yang_ditambah in daftar_kode_makanan_ke_nama_makanan :
                    makanan_yang_ditambah = daftar_kode_makanan_ke_nama_makanan[f"{makanan_yang_ditambah}"]
                #apabila makanan yang ingin ditambah tidak ada di menu
                if makanan_yang_ditambah not in menu :
                    perintah_2 = input(f"Menu {makanan_yang_ditambah} tidak ditemukan. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                #apabila makanan yang sebelumnya telah dipesan, makan dictionary diupdate agar jumlah pesanan tersebut ditambah 1
                elif makanan_yang_ditambah in daftar_jumlah_pesanan[nomor_meja].keys() :
                    jumlah_makanan_ditambah = daftar_jumlah_pesanan[nomor_meja][makanan_yang_ditambah] + 1
                    daftar_jumlah_pesanan[nomor_meja].update ({makanan_yang_ditambah:jumlah_makanan_ditambah})
                    perintah_2 = input(f"Berhasil memesan {makanan_yang_ditambah}. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
                #apabila makanan belum dipesan, membuat pesanan baru atas makanan tersebut, dan dictionary ditambahkan jumlah pesanan dan harga makanan
                elif makanan_yang_ditambah in menu :
                    jumlah_pesanan = 1
                    daftar_jumlah_pesanan[nomor_meja][makanan_yang_ditambah] = jumlah_pesanan
                    daftar_harga_pesanan[nomor_meja][makanan_yang_ditambah] = daftar_nama_makanan_ke_harga[f"{makanan_yang_ditambah}"]
                    perintah_2 = input (f"Berhasil memesan {makanan_yang_ditambah}. Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
            #apabila perintah tidak benar, ulang loop
            else : 
                print ("Perintah tidak benar, mohon diulang kembali")
                perintah_2 = input("Apakah Anda ingin GANTI JUMLAH, HAPUS, atau TAMBAH PESANAN? ")
        #apabila dihapus atau diubah menjadi kosong
        if daftar_jumlah_pesanan[nomor_meja] == {} :
            #mengosongkan kembali nama customer pada suatu meja
            del daftar_nama_meja[nomor_meja]
            list_meja.append(nomor_meja)
            list_meja.sort()
            print ()
            print ("Anda tidak memesan apa - apa")
        #menghasilkan output pesanan customer beserta total harga
        else :
            print ("Berikut adalah pesanan terbaru Anda : ")
            for key in daftar_jumlah_pesanan[nomor_meja] :
                harga = daftar_jumlah_pesanan[nomor_meja][key] * int(daftar_harga_pesanan[nomor_meja][key])
                print (f"{key} {daftar_jumlah_pesanan[nomor_meja][key]} buah, total Rp{harga}") 
                total_harga = harga + total_harga
            print ()
            print (f"Total pesanan : Rp{total_harga}")
    #apabila customer selesai menggunakan meja
    elif perintah == "SELESAI MENGGUNAKAN MEJA" :
        #validasi nomor meja
        try :
            nomor_meja = int(input("Nomor meja berapa? "))
        except ValueError :
            print ("Nomor meja kosong atau tidak sesuai (1-10), silahkan ulang kembali")
            continue
        if nomor_meja <= 0 or nomor_meja > 10 :
            print ("Nomor meja kosong atau tidak sesuai (1-10), silahkan ulang kembali")
            continue
        if nomor_meja in list_meja :
            print ("Anda belum memesan, silahkan pesan terlebih dahulu")
            continue
        #meja dikosongkan
        print (f"Pelanggan atas nama {daftar_nama_meja[nomor_meja]} selesai menggunakan meja {nomor_meja}.")
        receipt = open(f"receipt_{daftar_nama_meja[nomor_meja]}.txt", "w")
        del daftar_nama_meja[nomor_meja]
        #meja dikembalikan ke dalam list meja yang tersedia dan disortir agar yang diambil yang paling rendah
        list_meja.append(nomor_meja)
        list_meja.sort()
        #membuka loop untuk membuat file receipt beserta isinya
        for key in daftar_jumlah_pesanan[nomor_meja] :
            harga = daftar_jumlah_pesanan[nomor_meja][key] * int(daftar_harga_pesanan[nomor_meja][key])
            total_harga = harga + total_harga
            receipt.write (f"{inverse_daftar_kode_makanan_ke_nama_makanan[key]};{key};{daftar_jumlah_pesanan[nomor_meja][key]};{daftar_harga_pesanan[nomor_meja][key]};{harga}")
            receipt.write ("\n")
        receipt.write ("\n")
        receipt.write (f"Total {total_harga}")
        receipt.close ()
        #mereset pesanan meja customer yang selesai menggunakan
        daftar_jumlah_pesanan[nomor_meja].clear()
        daftar_harga_pesanan[nomor_meja].clear()
    #apabila program ingin ditutup
    elif perintah == "SELESAI" :
        #apabila ada customer yang belum selesai menggunakan meja 
        for keys,values in daftar_nama_meja.items() :
            print (f"Meja {keys} atau {values} belum selesai menggunakan meja")
        print ("Terima kasih telah datang ke Kafe Daun Pacilkom")
        stop = True
    #apabila perintah tidak valid, loop diulang
    else :
        print ("Perintah tidak valid, silahkan ulang kembali")
        continue




        