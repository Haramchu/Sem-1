
angka = int(input("Masukkan bilangan asli positif :"))

def faktorisasi_angka_prima(angka):
    total_pangkat_1 = 0

    i = 1
    while (i <= angka):
        k = 0
        if (angka % i==0):
            j = 1
            while (j <= i):
                if (i % j == 0):
                    k = k + 1
                    total_pangkat_1 = total_pangkat_1 + j
                j = j + 1 
            if (k == 2):
                print (str(i) + "^" + str(total_pangkat_1))
                total_pangkat_1 = 0
        i = i + 1



faktorisasi_angka_prima (angka)

