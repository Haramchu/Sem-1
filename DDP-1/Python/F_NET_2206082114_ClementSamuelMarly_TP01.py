#import library turtle dan random
import turtle
import random

#set screen
turtle.getscreen()
turtle.speed("fastest")
turtle.screensize(1920,1080)
turtle.pensize(2)
turtle.bgcolor("#8AFF8A")
turtle.pencolor("#000000")
turtle.penup()

#setup inputbox untuk variabel yang dibutuhkan
Balok_bawah = int(turtle.numinput("Input", "Jumlah batu bata pada lapisan paling bawah :", minval=1, maxval=25))
Balok_atas = int(turtle.numinput(f"Input", "Jumlah batu bata pada lapisan paling atas :", minval=1, maxval=Balok_bawah))
Panjang = int(turtle.numinput("Input", "Panjang satu buah batu bata (pixel) :", minval=1, maxval=35))
Lebar = int(turtle.numinput("Input", "Lebar satu buah batu bata (pixel) :", minval=1, maxval=25)) 

#setup variabel yang dibutuhkan
x = Balok_bawah
y = 1 + Balok_bawah - Balok_atas
balok = Balok_bawah
total_balok = 0

#mulai menggambar
#setup pemindahan posisi setiap naik balok
for j in range (y) :
    turtle.penup
    turtle.setposition((-(Panjang * (Balok_bawah - j) / 2)),(-(Lebar * ((Balok_bawah - Balok_atas) /2 - j))))
    turtle.pendown()

    #setup layer balok bawah
    if (Balok_bawah - j == Balok_bawah) :
        for i in range (x) :
            turtle.fillcolor("#BC4A3C")
            turtle.begin_fill()
            turtle.forward(Panjang)
            turtle.left(90)
            turtle.forward(Lebar)
            turtle.left(90)
            turtle.forward(Panjang)
            turtle.left(90)
            turtle.forward(Lebar)
            turtle.left(90)
            turtle.forward(Panjang)
            turtle.end_fill()

    #setup layer balok atas
    elif (Balok_bawah - j == Balok_atas) :
        for i in range (x) :
            turtle.fillcolor("#BC4A3C")
            turtle.begin_fill()
            turtle.forward(Panjang)
            turtle.left(90)
            turtle.forward(Lebar)
            turtle.left(90)
            turtle.forward(Panjang)
            turtle.left(90)
            turtle.forward(Lebar)
            turtle.left(90)
            turtle.forward(Panjang)
            turtle.end_fill()

    #setup layer balok tengah dan warna warni
    elif (Balok_bawah - j != Balok_bawah) :
        turtle.fillcolor("#BC4A3C")
        turtle.begin_fill()
        turtle.forward(Panjang)
        turtle.left(90)
        turtle.forward(Lebar)
        turtle.left(90)
        turtle.forward(Panjang)
        turtle.left(90)
        turtle.forward(Lebar)
        turtle.left(90)
        turtle.forward(Panjang)
        turtle.end_fill()

        for j in range (x-2) :
             #random angka untuk color code
            r = round(random.random() * 255)
            g = round(random.random() * 255)
            b = round(random.random() * 255)
            
            #angka diubah ke heksadesimal dengan if sebagai penjaga agar angka 0 dibelakang tetap ada
            r = hex(r)
            if (len(r)) == 3:
                r = r + "0"
            g = hex(g)
            if (len(g)) == 3:
                g = g + "0"
            b = hex(b)
            if (len(b)) == 3:
                b = b + "0"

            #penghilangan 0x di depan heksadesimal
            r = r[2:]
            g = g[2:]
            b = b[2:]

            #menggabungkan heksadesimal sehingga membentuk kode warna
            color = (r) + (g) + (b)
            color = "#" + color

            turtle.fillcolor(color)
            turtle.begin_fill()
            turtle.forward(Panjang)
            turtle.left(90)
            turtle.forward(Lebar)
            turtle.left(90)
            turtle.forward(Panjang)
            turtle.left(90)
            turtle.forward(Lebar)
            turtle.left(90)
            turtle.forward(Panjang)
            turtle.end_fill()

        turtle.fillcolor("#BC4A3C")
        turtle.begin_fill()
        turtle.forward(Panjang)
        turtle.left(90)
        turtle.forward(Lebar)
        turtle.left(90)
        turtle.forward(Panjang)
        turtle.left(90)
        turtle.forward(Lebar)
        turtle.left(90)
        turtle.forward(Panjang)
        turtle.end_fill()

    x = x - 1
    turtle.penup()

#menghitung total balok
for k in range (y) :
    total_balok = total_balok + balok
    balok = balok - 1

#menulis jumlah balok
turtle.setposition (0,(-(Lebar * ((Balok_bawah - Balok_atas) /2 + 3)) - 20))
Kalimat1 = "Candi dengan "
Kalimat2 = " total batu bata"
Kalimat_full = Kalimat1 + str(total_balok) + Kalimat2
turtle.write(Kalimat_full, align="center", font="bold")

turtle.hideturtle()
turtle.done()