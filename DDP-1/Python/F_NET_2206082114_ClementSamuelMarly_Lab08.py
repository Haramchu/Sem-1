masukkan = True
daftar_hubungan = {}
daftar_jarak = {}
#minta input
print ("Masukkan data hubungan")
while masukkan != False :
    masukkan = input()
    if masukkan == "SELESAI" :
        break
    #masukkan ke dictionary
    masukkan = masukkan.split()
    nama_1 = masukkan[0]
    nama_2 = masukkan[1]
    jarak = masukkan[2]
    daftar_hubungan[nama_1] = nama_2
    daftar_jarak [nama_1] = jarak

nama_awal = input("Masukkan nama awal:")
nama_tujuan = input("Masukkan nama tujuan:")
jarak_awal = 0
#recursion fungsi, nama untuk simpan nama awal dari user, nama awal akan berubah terus sampai nama awal menjadi nama tujuan
def operasi (nama, nama_awal, nama_tujuan, jarak_total) :
    #print hasil akhir
    if nama_awal == nama_tujuan :
        jarak_total = jarak_total * 10
        print (f"Jarak total : {int(jarak_total)}")
        if jarak_total > 1000 :
            print (f"{nama} dan {nama_tujuan} tidak saling kenal.")
        elif 100 < jarak_total <= 1000 :
            print (f"{nama} dan {nama_tujuan} mungkin saling kenal.")
        elif 0 < jarak_total <= 100 :
            print (f"{nama} dan {nama_tujuan} kenal dekat.")
    #apabila nama awal belum sampai tujuan, ulang fungsi
    else : 
        try :
            jarak_total = float(daftar_jarak[nama_awal]) + jarak_total
            operasi (nama, daftar_hubungan[nama_awal], nama_tujuan, jarak_total)
        except KeyError :
            print (f"Hubungan tidak ditemukan antara {nama} dan {nama_tujuan}")
#operasi akhir
operasi (nama_awal, nama_awal, nama_tujuan, jarak_awal)
