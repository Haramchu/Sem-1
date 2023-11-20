x = int(input("Masukkan lebar bahu :"))
y = int(input("Masukkan panjang lingkar perut :"))

if x <=15 and y <=60:
    print ("Ukuran : S")
elif 15< x <=18 and 60< y <=70:
    print ("Ukuran : M")
elif 18< x <=22 and 70< y <=80:
    print ("Ukuran : L")
elif 22< x <=25 and 80< y <=90:
    print ("Ukuran : XL")
else:
    print ("Ukuran melebihi XL")

