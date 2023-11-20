#untuk import math.pi
import math
#print awalan
print ("Selamat datang di Depot Minuman Dek Depe!")
print ("==========================================")

#definition hitungan harga balok dan volume
def harga_balok () : 
    #agar variabel dapat digunakan diluar def
    global Harga
    global Volume
    Harga = 0
    Volume = 0
    Volume = Panjang * Lebar * Tinggi
    Harga = Volume * 700
    Harga = round (Harga, 2)
    Volume = round (Volume, 2)

#definition hitungan harga kerucut dan volume
def harga_kerucut () :
    #agar variabel dapat digunakan diluar def
    global Harga
    global Volume
    Harga = 0
    Volume = 0
    Volume = 1/3 * math.pi * Jari**2 * Tinggi
    Harga = Volume * 700
    Harga = round (Harga, 2)
    Volume = round (Volume, 2)

#setup variabel
Bentuk = ""
Harga_total = 0
Volume_total = 0

#apabila bentuk tidak sama dengan stop, jalan terus
while Bentuk != "STOP" :
    Bentuk = input("Masukkan bentuk galon yang diinginkan antara BALOK atau KERUCUT (STOP untuk berhenti):")
    #apabila stop, print hasil akhir atau tidak ada input
    if Bentuk == "STOP" :
        if Volume_total == 0 :
            print ("====================================================")
            print ("Anda tidak memasukkan input satupun :(")
            print ("Terima kasih telah datang di Depot Minuman Pak Depe.")
            print ("====================================================")
            exit ()
        print ("====================================================")
        Volume_total = round (Volume_total, 2)
        print (f"Total volume air yang dikeluarkan adalah : {Volume_total}")
        Harga_total = round (Harga_total, 2)
        Harga_total = "Rp" + str(Harga_total)
        print (f"Total harga yang harus dibayar adalah : {Harga_total}")
        print ("====================================================")
        print ()
        print ("Terima kasih telah datang di Depot Minuman Pak Depe.")
        exit()
    #apabila bentuk balok, minta input dan masukkan ke dalam definisi balok
    elif Bentuk == "BALOK":
        Panjang = float(input("Masukkan panjang balok (angka) :"))
        if Panjang <= 0 or type(Panjang) == str:
            print ("Input tidak valid, coba kembali")
            exit()
        Lebar = float(input("Masukkan lebar balok (angka) :"))
        if Lebar <= 0 or type(Lebar) == str:
            print ("Input tidak valid, coba kembali")
            exit()
        Tinggi = float(input("Masukkan tinggi balok (angka) :"))
        if Tinggi <= 0 or type(Tinggi) == str:
            print ("Input tidak valid, coba kembali")
            exit()
        harga_balok ()
        #simpan total volume dan harga
        Harga_total = Harga_total + Harga
        Volume_total = Volume_total + Volume
        #reset variabel
        Tinggi = 0
        Panjang = 0
        Lebar = 0
        print ()
    #apabila bentuk kerucut minta input dan masukkan ke dalam definisi kerucut
    elif Bentuk == "KERUCUT" :
        Jari = float(input("Masukkan jari-jari kerucut (angka) :"))
        if Jari <= 0 and type(Jari) == str:
            print ("Input tidak valid, coba kembali")
            exit()
        Tinggi = float(input("Masukkan tinggi kerucut (angka) :"))
        if Tinggi <= 0 and type(Tinggi) == str:
            print ("Input tidak valid, coba kembali")
            exit()
        print ()
        harga_kerucut ()
        #simpan total volume dan harga
        Harga_total = Harga_total + Harga
        Volume_total = Volume_total + Volume
        #reset variabel
        Tinggi = 0
        Jari = 0
        print ()
    #apabila bentuk bukan balok atau kerucut
    elif Bentuk != "BALOK" and Bentuk != "KERUCUT" :
        print ("Bentuk yang dimasukkan tidak valid")

    
        

    

