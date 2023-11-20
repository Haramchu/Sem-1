import turtle

def draw_something():
    x = 50
    x = x + i * 50
    turtle.forward(x)
    turtle.left(90)
    return x   

for i in range(10):
    draw_something()
turtle.hideturtle()

def faktorisasi_angka_prima(angka):
    total_pangkat_1 = 0
    total_pangkat_2 = 0

    while (angka % 2 == 0 ):
        total_pangkat_1 = total_pangkat_1 + 1
        angka = angka / 2
    print(str(2) + "^" + str(total_pangkat_1), end = "")
    
    i=1
    while (i<=angka):
        k = 0
        if (angka % i==0):
            j = 1
            while (j <= i):
                if (i % j == 0):
                    k = k + 1
                j = j + 1 
            if (k == 2):
                print (i)
        i = i + 1
    
        while (angka % i == 0):  
            total_pangkat_2 = total_pangkat_2 + 1  
            angka = angka / i  
    print("*" + str(i) + "^" + str(total_pangkat_2), end = "")