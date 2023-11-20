9#Kolaborator : Yosef Nuraga Wicaksana 2206082751 dan Alexander Audric Johansyah 2206815466
#import library
import sys
import os
#function error
def error() :
    print("Argumen program tidak valid")
    exit()
#function untuk mendapatkan location file
def File_location_finder() :
    return os.path.join(folder,file)
#analisa input dari user
wildcard = False
input = sys.argv
#apabila -w dan -i ada di input, panggil function error
if "-w" in input and "-i" in input:
    error()
#apabila -w atau -i ada di input, input masuk
elif "-w" in input or "-i" in input:
    #apabila jumlah input lebih dari yang ditentukan, panggil function error
    if len(input) != 4 :
        error()
    command = input[1]
    word = input[2]
    location = input[3]
    wildcard_found = word.find("*")
    #apabila ada tanda wildcard, ubah wildcard menjadi True
    if wildcard_found >= 0 :
        wildcard = True
        word_split = word.split("*")
        #apabila ada dua simbol wildcard atau hanya simbol wildcard, panggil function error
        if len(word_split) >= 3 or len(word_split) <= 0:
            error()
#apabila tidak ada -w atau -i ada di input, input tetap masuk
elif "-w" not in input and "-i" not in input:
    #apabila jumlah input lebih dari yang ditentukan, panggil function error
    if len(input) != 3 : 
        error()
    command = "Empty"
    word = input[1]
    location = input[2]
    wildcard_found = word.find("*")
    #apabila ada tanda wildcard, ubah wildcard menjadi True
    if wildcard_found >= 0 :
        wildcard = True
        word_split = word.split("*")
        #apabila ada dua simbol wildcard atau hanya simbol wildcard, panggil function error
        if len(word_split) >= 3 or len(word_split) <= 0:
            error()
#function print hasil untuk pemanggilan folder
def print_hasil_scan () :
    print(f"{File_location_finder()[:40]:<40}  line  {(line_number + 1):<3}  {line_word[:40]:<40}")
#function print hasil untuk pemanggilan file langsung
def print_direct_location () :
    print(f"{location[:40]:<40}    line  {(line_number + 1):<3}   {line_word[:40]:<40}")
#function scan folder yang diminta
def scan_folder () :
    global folder, directory, file
    global line_number, line_word  
    for folder, directory, files in os.walk(location) :
        for file in files :
            #membuka file dan membaca
            file_open = open(File_location_finder())
            file_read = file_open.readlines()
            #buka for untuk mendapatkan line number dan membaca tiap line
            for line_number in range (0, len(file_read)) :
                line_word = file_read[line_number].split()
                line_word = " ".join(line_word)
                line = line_word.split()
                #apabila tidak ada wildcard
                if wildcard == False :
                    #apabila tidak ada -w atau -i, print hasil scan
                    if command == "Empty":
                        if word in line_word :
                            print_hasil_scan()
                    #apabila commandnya -w, word yang dicari tidak diturunkan, langsung dicari
                    elif command == "-w":
                        for word_file in line :
                            if word == word_file :
                                print_hasil_scan()
                    #apabila commandnya -i, word yang dicari diturunkan beserta barisan yang dibaca agar bisa menghiraukan uppercase lowercase
                    elif command == "-i":
                        if word.lower() in line_word.lower() :
                            print_hasil_scan()
                #apabila ada wildcard
                elif wildcard == True :
                    #split kata menjadi dua berdasarkan letak wildcard
                    word_split = word.split("*")
                    word_1 = word_split[0]
                    word_2 = word_split[1]
                    #mengulang command namun apabila ada wildcard
                    #operasi tiap command disesuaikan dengan adanya dua string akibat wildcard
                    if command == "Empty":
                        if word_1 in line_word and word_2 in line_word :
                            print_hasil_scan()
                    elif command == "-w":
                        for word_file in line :
                            word_file_1 = word_file[:len(word_1)]
                            word_file_2 = word_file[len(word_file) - len(word_2):]
                            #print(word_file_1, word_file_2)
                            if word_1 == word_file_1 and word_2 == word_file_2 :
                                print_hasil_scan()
                    elif command == "-i":
                        line_word = line_word.lower()
                        #find digunakan untuk mencari berdasarkan index hingga mencegah tetap ditemukannya barisan word walaupun wildcard terbalik
                        found_1 = line_word.find(word_1.lower())
                        found_2 = line_word.find(word_2.lower(),found_1)
                        if found_1 >= 0 and found_2 >= 0 :
                            print_hasil_scan()
#function untuk scan file langsung kurang lebih sama dengan scan folder, hanya tidak perlu os.walk dan hasil printnya tidak perlu memanggil function file finder
def scan_file ():
    global folder, directory, file
    global line_number, line_word
    file_open = open(location)
    file_read = file_open.readlines()
    for line_number in range (0, len(file_read)) :
        line_word = file_read[line_number].split()
        line_word = " ".join(line_word)
        line = line_word.split()
        if wildcard == False :
            if command == "Empty":
                if word in line_word :
                    print_direct_location()
            elif command == "-w":
                for word_file in line :
                    if word == word_file :
                        print_direct_location()
            elif command == "-i":
                if word.lower() in line_word.lower() :
                    print_direct_location()
        elif wildcard == True :
            word_split = word.split("*")
            word_1 = word_split[0]
            word_2 = word_split[1]
            if command == "Empty":
                if word_1 in line_word and word_2 in line_word :
                    print_direct_location()
            elif command == "-w":
                for word_file in line :
                    word_file_1 = word_file[:len(word_1)]
                    word_file_2 = word_file[len(word_file) - len(word_2):]
                    #print(word_file_1, word_file_2)
                    if word_1 == word_file_1 and word_2 == word_file_2 :
                        print_direct_location()
            elif command == "-i":
                line_word = line_word.lower()
                found_1 = line_word.find(word_1.lower())
                found_2 = line_word.find(word_2.lower(),found_1)
                if found_1 >= 0 and found_2 >= 0 :
                    print_direct_location()
#eksekusi function dengan try untuk menuliskan file tidak ditemukan apabila terdapat error file not found
try :                 
    if os.path.isdir(location) :
        scan_folder ()
    else :
        scan_file ()
except FileNotFoundError :
    print (f"Path {location} tidak ditemukan")
