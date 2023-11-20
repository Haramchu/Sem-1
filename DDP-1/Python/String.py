#setup input dan variabel
String_1 = input("Masukkan String: ")
String_2 = String_1
String_3 = ""
String_akhir = ""

#setup loop untuk memisahkan tiap huruf dan menggeser 1 ke kanan
for i in range (len(String_1)) :
    String_2 = String_2 [i:i + 1]
    String_3 = ord(String_2) + 1

    #untuk huruf z agar balik ke a
    if String_3 == 91 :
        String_3 = 65
    elif String_3 == 123 :
        String_3 = 97

    #compile kembali semua huruf
    String_3 = chr(String_3)
    String_akhir = String_akhir + String_3 
    String_3 = 0
    String_2 = String_1

print(String_akhir)