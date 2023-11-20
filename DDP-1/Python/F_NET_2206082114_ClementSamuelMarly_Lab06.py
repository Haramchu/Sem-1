#print awalan
print ("Selamat Datang di Program Pemeriksa Nilai Dek Depe!")
print ("===================================================")
print ()
print ("Masukkan kunci jawaban: (gunakan huruf kapital dan STOP untuk berhenti)")

#bikin list awal dan looping untuk menerima kunci jawaban
list_kunci_jawaban = []
stop = False
while (stop != True) :
    #meminta input kunci jawaban
    kunci_jawaban = input()
    #memasukkan kunci jawaban ke list
    list_kunci_jawaban.append(kunci_jawaban)
    #fungsi stop untuk memberhentikan masukkan dari kunci jawban
    if kunci_jawaban == "STOP":
        stop = True
        #agar stop tidak dimasukkan ke dalam list
        list_kunci_jawaban.remove("STOP")

print ("Masukkan jawaban kamu : (Gunakan Huruf Kapital)")

#setup variabel
benar = 0
#setup loop berdasarkan jumlah kunci jawaban di list yang dimasukkan
for kunci_jawaban in list_kunci_jawaban :
    jawaban = input()
    #apabila jawaban sama dengan kunci jawaban, berarti jawaban benar dan dicatat
    if jawaban == kunci_jawaban :
        benar = benar + 1
#menghitung nilai dengan floor division
nilai = int(benar / len(list_kunci_jawaban) * 100 // 1)

#print kata kata berdasarkan nilai yang diperoleh
if nilai >= 85 :
    print("Selamat :D")
elif nilai >= 55 : 
    print ("Semangat :)")
else :
    print ("nt")

#print akhir jumlah benar dari total soal dan nilainya
print (f"Total jawaban benar adalah {benar} dari {len(list_kunci_jawaban)}")
print (f"Nilai yang kamu peroleh adalah {nilai}")