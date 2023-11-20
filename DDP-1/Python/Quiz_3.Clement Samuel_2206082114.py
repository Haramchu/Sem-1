angka = input ("Masukkan angka : ")
def countOnes(angka, total) :
    if len(angka) == 1:
        if angka == "0" :
            print(total)
        elif angka == "1" :
            print(total + 1)
    else :
        if angka[0:1] == "1" :
            total = total + 1
            return countOnes(angka[1:], total)
        else :
            return countOnes(angka[1:], total)

countOnes(angka, 0)