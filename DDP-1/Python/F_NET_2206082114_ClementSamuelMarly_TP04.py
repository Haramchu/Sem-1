# import modul 
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as showinfo
import random

#setup list awal
list_meja = [1,2,3,4,5,6,7,8,9,10]
#setup warna meja dan perintah tiap button pada saat ubah ataupun selesai menggunakan meja
dict_warna_meja = {}
dict_perintah_meja = {}
#list meja terisi
list_meja_isi = []
#kode ke harga atau nama atau keunikan
dict_kode_ke_harga = {}
dict_kode_ke_nama = {}
dict_kode_ke_keunikan = {}
#untuk bikin tabel berdasarkan jumlah tiap kategori menu
daftar_kategori = {}
list_kategori = []
#daftar pesanan tiap meja
daftar_harga_pesanan = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}
daftar_jumlah_pesanan = {1:{},2:{},3:{},4:{},5:{},6:{},7:{},8:{},9:{},10:{}}
#daftar nama pemesan tiap meja
daftar_nama_meja = {}
#list apabila pemesan pencet kembali
meja_mau_selesai = []
list_meja_mau_isi = []
#list mengecek menu
list_menu_check_duplicate = []
set_menu_check_duplicate = set()

#setup main window
class Main(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.pack()
        master.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        button1 = tk.Button(self, text="Buat Pesanan", width=30, command=self.buat_pesanan, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=30, command=self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        button1.grid(row=0, column=0, padx=10, pady=40)
        button2.grid(row=1, column=0)  
    #lanjut ke class buat pesanan  
    def buat_pesanan(self):
        #apabila meja penuh
        if list_meja == [] :
            showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Mohon maaf meja sudah penuh. Silahkan tunggu beberapa saat lagi")
        else :
            BuatPesanan(self.master)
    #lanjut ke class selesai menggunakan meja
    def selesai_gunakan_meja(self):
        SelesaiGunakanMeja(self.master)
        
#class buat pesanan
class BuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.master.geometry("400x200")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_nama = tk.Label(self, text="Siapa nama Anda?")
        self.lbl_nama.grid(column=0, row=0, padx=20, pady=50)
        button1 = tk.Button(self, text="Kembali", width=20, command= self.kembali, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Lanjut", width=20, command= self.lanjut, bg="#4472C4", fg="white")
        button1.grid(row=1, column=0, padx=20, pady=20)
        button2.grid(row=1, column=1, padx=20, pady=20)
        self.nama = tk.StringVar()
        self.input = tk.Entry(self, textvariable=self.nama, width=20)
        self.input.grid(column = 1, row = 0, padx=20, pady=50)
        self.mainloop()
    #destroy window buat pesanan
    def kembali(self):
        self.destroy()
    #lanjut ke class menubuatpesanan
    def lanjut(self):
        #destroy window buat pesanan
        self.destroy()
        #ambil meja random
        nomor_meja = random.choice(list_meja)
        #apabila nama kosong
        if self.nama.get() == "" :
            showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Input nama tidak boleh kosong")
        else :
            #simpan data nama dan meja
            daftar_nama_meja[nomor_meja] = self.nama.get()
            list_meja.remove(nomor_meja)
            list_meja_mau_isi.append(nomor_meja)
            MenuBuatPesanan(self.master)

#buat window menu buat pesanan
class MenuBuatPesanan(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("800x500")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        #ambil nama dan nomor meja dari list tempat menyimpan meja random
        self.lbl_nama = tk.Label(self, text=f"Nama pemesan: {daftar_nama_meja[list_meja_mau_isi[0]]}")
        self.lbl_nama.grid(column=0, row=0, padx=30, pady=(3,20))
        self.nama_meja = tk.Label(self, text=f"No meja: {list_meja_mau_isi[0]}")
        self.nama_meja.grid(column=3, row=0, padx=10, pady=(3,20), sticky="e")
        value = []
        #buat loop untuk mendapatkan variabel placeholder combobox
        for val in range (0,1001) :
          value.append(val)
        i=1
        #loop untuk membuat menu
        for kategori in daftar_kategori.keys() :
            self.dish = tk.Label(self, text=kategori)
            self.dish.grid(column=0, row=i)
            i += 1
            self.kode = tk.Label(self, text="Kode", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.kode.grid(column=0, row=i, sticky="e")
            self.Nama = tk.Label(self, text="Nama", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.Nama.grid(column=1, row=i, sticky="ew")
            self.Harga = tk.Label(self, text="Harga", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.Harga.grid(column=2, row=i, sticky="ew")
            #menyesuaikan dengan keunikan yang ada di soal TP 4, selain itu dianggap keunikan
            if kategori == "MEALS" :
                text_label = "Kegurihan"
            elif kategori == "DRINKS" :
                text_label = "Kemanisan"
            elif kategori == "SIDES" :
                text_label = "Keviralan"
            else :
                text_label = "Keunikan"
            self.kegurihan = tk.Label(self, text=text_label, borderwidth=1, relief="sunken", width=20, anchor="w")
            self.kegurihan.grid(column=3, row=i, sticky="ew")
            self.jumlah = tk.Label(self, text="Jumlah", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.jumlah.grid(column=4, row=i, sticky="w")
            i += 1
            #membuat menu memesan setiap menu yang ada tiap kategori
            for kode_menu in daftar_kategori[kategori] :
                self.label_kode = tk.Label(self, text=f"{kode_menu}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_kode.grid(column=0, row=i, sticky="e")
                self.label_nama = tk.Label(self, text=f"{dict_kode_ke_nama[kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_nama.grid(column=1, row=i, sticky="ew")
                self.label_harga = tk.Label(self, text=f"{dict_kode_ke_harga[kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_harga.grid(column=2, row=i, sticky="ew")
                self.label_keunikan = tk.Label(self, text=f"{dict_kode_ke_keunikan[kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_keunikan.grid(column=3, row=i, sticky="ew")
                self.jumlah = tk.IntVar()
                #membuat setiap kali combobox diclick akan menjalankan suatu function
                self.input = ttk.Combobox(self, textvariable=self.jumlah, values=value, width=20)
                self.input.grid(column = 4, row=i, sticky="w")
                self.input.bind("<<ComboboxSelected>>", lambda event, jumlah=kode_menu: self.masukkan_angka(event,jumlah))
                i += 1
        self.total_harga = tk.Label(self, text="Total harga : Rp 0", font=("Segoe UI", 12, "bold"))
        self.total_harga.grid(row=i+1, column= 3, padx=10, pady=10, columnspan=2)
        button1 = tk.Button(self, text="Kembali", width=18, command= self.kembali, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Ok", width=18, command= self.ok, bg="#4472C4", fg="white")
        button3 = tk.Button(self, text="Ubah", width=5, command= self.ubah, bg="#4472C4", fg="white")
        button1.grid(row=i+2, column= 1, padx=10, pady=(40,10),columnspan=2)
        button2.grid(row=i+2, column= 2, padx=10, pady=(40,10),columnspan=2)
        button3.grid(row=0, column= 4, pady=(3,20),sticky="w")
        self.mainloop()
    #function apabila combobox diclick, maka jumlah pesanan akan dicatat dan total harga akan diubah langsung
    def masukkan_angka(self,event,jumlah_pesanan) :
        total_harga = 0
        angka = int(event.widget.get())
        daftar_jumlah_pesanan[list_meja_mau_isi[0]][jumlah_pesanan]= angka
        #cari total harga dari daftar pesanan
        for kode_makanan in daftar_jumlah_pesanan[list_meja_mau_isi[0]].keys():
          harga = daftar_jumlah_pesanan[list_meja_mau_isi[0]][kode_makanan] * int(dict_kode_ke_harga[kode_makanan])
          total_harga = harga + total_harga
        self.total_harga["text"] = f"Total harga : Rp {total_harga}"
    #function kembali ke window awal dan reset list
    def kembali(self):
        nomor_meja = list_meja_mau_isi[0]
        list_meja.append(nomor_meja)
        list_meja_mau_isi.remove(nomor_meja)
        self.destroy()
    #function untuk mencatat jumlah dan harga pesanan berdasarkan nomor meja
    def ok(self):
        total_harga = 0
        #cari total harga dari daftar pesanan
        for kode_makanan in daftar_jumlah_pesanan[list_meja_mau_isi[0]].keys():
          harga = daftar_jumlah_pesanan[list_meja_mau_isi[0]][kode_makanan] * int(dict_kode_ke_harga[kode_makanan])
          total_harga = harga + total_harga
        #apabila tidak ada pesanan, keluar dan reset list serta daftar
        if total_harga == 0 :
            showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Anda belum memesan apapun")
            nomor_meja = list_meja_mau_isi[0]
            daftar_jumlah_pesanan[list_meja_mau_isi[0]] = {}
            list_meja.append(nomor_meja)
            list_meja_mau_isi.remove(nomor_meja)
            self.destroy()
        else :
            #masukkan data ke dalam daftar pesanan
            for kode_makanan in daftar_jumlah_pesanan[list_meja_mau_isi[0]].keys():
              daftar_harga_pesanan[list_meja_mau_isi[0]][kode_makanan] = daftar_jumlah_pesanan[list_meja_mau_isi[0]][kode_makanan] * int(dict_kode_ke_harga[kode_makanan])
            #reset list meja random temporary
            list_meja_isi.append(list_meja_mau_isi[0])
            list_meja_mau_isi.clear()
            self.destroy()
    #function lanjut ke class ubah pesanan
    def ubah(self):
        self.destroy()
        UbahPesanan(self.master)

class UbahPesanan(tk.Toplevel) :
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("430x400")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        #setup command setiap button
        dict_perintah_meja[1] = self.mau_menggunakan_meja_1
        dict_perintah_meja[2] = self.mau_menggunakan_meja_2
        dict_perintah_meja[3] = self.mau_menggunakan_meja_3
        dict_perintah_meja[4] = self.mau_menggunakan_meja_4
        dict_perintah_meja[5] = self.mau_menggunakan_meja_5
        dict_perintah_meja[6] = self.mau_menggunakan_meja_6
        dict_perintah_meja[7] = self.mau_menggunakan_meja_7
        dict_perintah_meja[8] = self.mau_menggunakan_meja_8
        dict_perintah_meja[9] = self.mau_menggunakan_meja_9
        dict_perintah_meja[10] = self.mau_menggunakan_meja_10
        #re-setup command dan warna button apabila meja sudah terisi atau sedang digunakan
        for nomor_meja in list_meja_mau_isi :
            dict_warna_meja[nomor_meja] = "#2E2EFF"
            dict_perintah_meja[nomor_meja] = self.meja_sendiri
        for nomor_meja in list_meja :
            dict_warna_meja[nomor_meja] = "#808080"
        for nomor_meja in list_meja_isi :
            dict_warna_meja[nomor_meja] = "#FF0000"
            dict_perintah_meja[nomor_meja] = self.skip
        self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:", width=40)
        self.lbl_command.grid(column=2, row=0, columnspan=2)
        self.info = tk.Label(self, text="Info", font = ("Segoe UI",12,"bold"), anchor="w")
        self.info.grid (column=1, row = 6, padx=20)
        self.info_1 = tk.Label(self, text="Merah : Terisi")
        self.info_1.grid (column=1, row = 7, padx=20, columnspan=2, sticky="w")
        self.info_2 = tk.Label(self, text="Abu-abu : Kosong")
        self.info_2.grid (column=1, row = 8, padx=20, columnspan=2, sticky="w")
        self.info_3 = tk.Label(self, text="Biru : Meja Anda")
        self.info_3.grid (column=1, row = 9, padx=20, columnspan=2, sticky="w")
        #pasang setiap button
        button1 = tk.Button(self, text="1", width=15, command= dict_perintah_meja[1], bg=dict_warna_meja[1], fg="white")
        button2 = tk.Button(self, text="2", width=15, command= dict_perintah_meja[2], bg=dict_warna_meja[2], fg="white")
        button3 = tk.Button(self, text="3", width=15, command= dict_perintah_meja[3], bg=dict_warna_meja[3], fg="white")
        button4 = tk.Button(self, text="4", width=15, command= dict_perintah_meja[4], bg=dict_warna_meja[4], fg="white")
        button5 = tk.Button(self, text="5", width=15, command= dict_perintah_meja[5], bg=dict_warna_meja[5], fg="white")
        button6 = tk.Button(self, text="6", width=15, command= dict_perintah_meja[6], bg=dict_warna_meja[6], fg="white")
        button7 = tk.Button(self, text="7", width=15, command= dict_perintah_meja[7], bg=dict_warna_meja[7], fg="white")
        button8 = tk.Button(self, text="8", width=15, command= dict_perintah_meja[8], bg=dict_warna_meja[8], fg="white")
        button9 = tk.Button(self, text="9", width=15, command= dict_perintah_meja[9], bg=dict_warna_meja[9], fg="white")
        button10 = tk.Button(self, text="10", width=15, command= dict_perintah_meja[10], bg=dict_warna_meja[10], fg="white")
        button1.grid(row=1, column= 2, pady = 5)
        button2.grid(row=2, column= 2, pady = 5)
        button3.grid(row=3, column= 2, pady = 5)
        button4.grid(row=4, column= 2, pady = 5)
        button5.grid(row=5, column= 2, pady = 5)
        button6.grid(row=1, column= 3, pady = 5)
        button7.grid(row=2, column= 3, pady = 5)
        button8.grid(row=3, column= 3, pady = 5)
        button9.grid(row=4, column= 3, pady = 5)
        button10.grid(row=5, column= 3, pady = 5)
        button_kembali = tk.Button(self, text="Kembali", width=18, command= self.kembali_menu, bg="#4472C4", fg="white")
        button_kembali.grid(row=10, column= 2,pady = 15, columnspan=2)
        self.mainloop()
    #function balik ke menu
    def kembali_menu(self):
        self.destroy()
        MenuBuatPesanan(self.master)
    #function apabila meja sudah terisi, balik ke menu
    def skip(self):
        self.destroy()
        showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Tidak bisa memilih meja orang lain")
        MenuBuatPesanan(self.master)
    #function apabila meja sedang digunakan, balik ke menu
    def meja_sendiri(self):
        self.destroy()
        showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Tidak bisa memilih meja sendiri")
        MenuBuatPesanan(self.master)
    #function setiap button apabila meja kosong dan reset list. Function dibedakan setiap button agar bisa diambil variabel button yang dipencet
    def mau_menggunakan_meja_1(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(1)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(1)
        daftar_nama_meja[1] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_2(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(2)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(2)
        daftar_nama_meja[2] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_3(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(3)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(3)
        daftar_nama_meja[3] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_4(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(4)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(4)
        daftar_nama_meja[4] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_5(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(5)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(5)
        daftar_nama_meja[5] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_6(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(6)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(6)
        daftar_nama_meja[6] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_7(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(7)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(7)
        daftar_nama_meja[7] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_8(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(8)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(8)
        daftar_nama_meja[8] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_9(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(9)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(9)
        daftar_nama_meja[9] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)
    def mau_menggunakan_meja_10(self):
        nama_pemesan = daftar_nama_meja[list_meja_mau_isi[0]]
        list_meja.append(list_meja_mau_isi[0])
        list_meja.remove(10)
        list_meja.sort()
        list_meja_mau_isi.clear()
        list_meja_mau_isi.append(10)
        daftar_nama_meja[10] = nama_pemesan
        self.destroy()
        MenuBuatPesanan(self.master)

#window selesaimenggunakanmeja. Konsep sama seperti class ubah
class SelesaiGunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        #apabila meja masih kosong semua
        if len(list_meja) == 10 :
            showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Belum ada meja yang dipesan")
            self.destroy()
        else :
            self.geometry("430x400")
            self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
            dict_perintah_meja[1] = self.selesai_meja_1
            dict_perintah_meja[2] = self.selesai_meja_2
            dict_perintah_meja[3] = self.selesai_meja_3
            dict_perintah_meja[4] = self.selesai_meja_4
            dict_perintah_meja[5] = self.selesai_meja_5
            dict_perintah_meja[6] = self.selesai_meja_6
            dict_perintah_meja[7] = self.selesai_meja_7
            dict_perintah_meja[8] = self.selesai_meja_8
            dict_perintah_meja[9] = self.selesai_meja_9
            dict_perintah_meja[10] = self.selesai_meja_10
            for nomor_meja in list_meja :
                dict_warna_meja[nomor_meja] = "#808080"
                dict_perintah_meja[nomor_meja] = self.skip
            for nomor_meja in list_meja_isi :
                dict_warna_meja[nomor_meja] = "#FF0000"
            self.lbl_command = tk.Label(self, text="Silakan klik meja yang selesai digunakan:", width=40)
            self.lbl_command.grid(column=2, row=0, columnspan=2)
            self.info = tk.Label(self, text="Info", font = ("Segoe UI",12,"bold"), anchor="w")
            self.info.grid (column=1, row = 6, padx=20)
            self.info_1 = tk.Label(self, text="Merah : Terisi")
            self.info_1.grid (column=1, row = 7, padx=20, columnspan=2, sticky="w")
            self.info_2 = tk.Label(self, text="Abu-abu : Kosong")
            self.info_2.grid (column=1, row = 8, padx=20, columnspan=2, sticky="w")
            button1 = tk.Button(self, text="1", width=15, command= dict_perintah_meja[1], bg=dict_warna_meja[1], fg="white")
            button2 = tk.Button(self, text="2", width=15, command= dict_perintah_meja[2], bg=dict_warna_meja[2], fg="white")
            button3 = tk.Button(self, text="3", width=15, command= dict_perintah_meja[3], bg=dict_warna_meja[3], fg="white")
            button4 = tk.Button(self, text="4", width=15, command= dict_perintah_meja[4], bg=dict_warna_meja[4], fg="white")
            button5 = tk.Button(self, text="5", width=15, command= dict_perintah_meja[5], bg=dict_warna_meja[5], fg="white")
            button6 = tk.Button(self, text="6", width=15, command= dict_perintah_meja[6], bg=dict_warna_meja[6], fg="white")
            button7 = tk.Button(self, text="7", width=15, command= dict_perintah_meja[7], bg=dict_warna_meja[7], fg="white")
            button8 = tk.Button(self, text="8", width=15, command= dict_perintah_meja[8], bg=dict_warna_meja[8], fg="white")
            button9 = tk.Button(self, text="9", width=15, command= dict_perintah_meja[9], bg=dict_warna_meja[9], fg="white")
            button10 = tk.Button(self, text="10", width=15, command= dict_perintah_meja[10], bg=dict_warna_meja[10], fg="white")
            button1.grid(row=1, column= 2, pady = 5)
            button2.grid(row=2, column= 2, pady = 5)
            button3.grid(row=3, column= 2, pady = 5)
            button4.grid(row=4, column= 2, pady = 5)
            button5.grid(row=5, column= 2, pady = 5)
            button6.grid(row=1, column= 3, pady = 5)
            button7.grid(row=2, column= 3, pady = 5)
            button8.grid(row=3, column= 3, pady = 5)
            button9.grid(row=4, column= 3, pady = 5)
            button10.grid(row=5, column= 3, pady = 5)
            button_kembali = tk.Button(self, text="Kembali", width=18, command= self.kembali, bg="#4472C4", fg="white")
            button_kembali.grid(row=9, column= 2,columnspan=2)
            self.mainloop()
    def kembali(self):
        self.destroy()
    def skip(self):
        showinfo.showinfo(title = "Kafe Daun-Daun Pacilkom v2.0 🌿", message ="Meja belum memesan")
        self.destroy()
    def selesai_meja_1(self):
        meja_mau_selesai.append(1)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_2(self):
        meja_mau_selesai.append(2)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_3(self):
        meja_mau_selesai.append(3)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_4(self):
        meja_mau_selesai.append(4)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_5(self):
        meja_mau_selesai.append(5)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_6(self):
        meja_mau_selesai.append(6)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_7(self):
        meja_mau_selesai.append(7)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_8(self):
        meja_mau_selesai.append(8)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_9(self):
        meja_mau_selesai.append(9)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)
    def selesai_meja_10(self):
        meja_mau_selesai.append(10)
        self.destroy()
        MenuSelesaiMenggunakanMeja(self.master)   

#window menu pembayaran. Konsep sama seperti menu awal
class MenuSelesaiMenggunakanMeja(tk.Toplevel):
    def __init__(self, master = None):
        super().__init__(master)
        self.geometry("800x500")
        self.title("Kafe Daun-Daun Pacilkom v2.0 🌿")
        self.lbl_nama = tk.Label(self, text=f"Nama pemesan: {daftar_nama_meja[meja_mau_selesai[0]]}")
        self.lbl_nama.grid(column=0, row=0, padx=30, pady=(3,20))
        self.nama_meja = tk.Label(self, text=f"No meja: {meja_mau_selesai[0]}")
        self.nama_meja.grid(column=3, row=0, padx=10, pady=(3,20), sticky="e")
        i=1
        for kategori in daftar_kategori.keys() :
            self.dish = tk.Label(self, text=kategori)
            self.dish.grid(column=0, row=i)
            i += 1
            self.kode = tk.Label(self, text="Kode", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.kode.grid(column=0, row=i, sticky="e")
            self.Nama = tk.Label(self, text="Nama", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.Nama.grid(column=1, row=i, sticky="ew")
            self.Harga = tk.Label(self, text="Harga", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.Harga.grid(column=2, row=i, sticky="ew")
            if kategori == "MEALS" :
                text_label = "Kegurihan"
            elif kategori == "DRINKS" :
                text_label = "Kemanisan"
            elif kategori == "SIDES" :
                text_label = "Keviralan"
            else :
                text_label = "Keunikan"
            self.kegurihan = tk.Label(self, text=text_label, borderwidth=1, relief="sunken", width=20, anchor="w")
            self.kegurihan.grid(column=3, row=i, sticky="ew")
            self.jumlah = tk.Label(self, text="Jumlah", borderwidth=1, relief="sunken", width=20, anchor="w")
            self.jumlah.grid(column=4, row=i, sticky="w")
            i += 1
            for kode_menu in daftar_kategori[kategori] :
                self.label_kode = tk.Label(self, text=f"{kode_menu}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_kode.grid(column=0, row=i, sticky="e")
                self.label_nama = tk.Label(self, text=f"{dict_kode_ke_nama[kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_nama.grid(column=1, row=i, sticky="ew")
                self.label_harga = tk.Label(self, text=f"{dict_kode_ke_harga[kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_harga.grid(column=2, row=i, sticky="ew")
                self.label_keunikan = tk.Label(self, text=f"{dict_kode_ke_keunikan[kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                self.label_keunikan.grid(column=3, row=i, sticky="ew")
                try :
                    self.jumlah = tk.Label(self, text=f"{daftar_jumlah_pesanan[meja_mau_selesai[0]][kode_menu]}", borderwidth=1, relief="sunken", width=20, anchor="w")
                    self.jumlah.grid(column=4, row=i, sticky="ew")
                except KeyError :
                    self.jumlah = tk.Label(self, text="0", borderwidth=1, relief="sunken", width=20, anchor="w")
                    self.jumlah.grid(column=4, row=i, sticky="ew")
                i += 1
        total_harga = 0
        for kode_makanan in daftar_jumlah_pesanan[meja_mau_selesai[0]].keys():
          harga = daftar_jumlah_pesanan[meja_mau_selesai[0]][kode_makanan] * int(dict_kode_ke_harga[kode_makanan])
          total_harga = harga + total_harga
        self.total_harga = tk.Label(self, text=f"Total harga : Rp {total_harga}", font=("Segoe UI", 12, "bold"))
        self.total_harga.grid(row=i+1, column= 3, padx=10, pady=10, columnspan=2)
        button1 = tk.Button(self, text="Kembali", width=18, command= self.kembali, bg="#4472C4", fg="white")
        button2 = tk.Button(self, text="Selesai Gunakan Meja", width=18, command= self.selesai_gunakan_meja, bg="#4472C4", fg="white")
        button1.grid(row=i+2, column= 1, padx=10, pady=(40,10),columnspan=2)
        button2.grid(row=i+2, column= 2, padx=10, pady=(40,10),columnspan=2)
        self.mainloop()
    def kembali(self):
        meja_mau_selesai.clear()
        self.destroy()
        self.mainloop()
    #reset list dan daftar apabila selesai menggunakan
    def selesai_gunakan_meja(self):
        daftar_harga_pesanan[meja_mau_selesai[0]] = {}
        list_meja_isi.remove(meja_mau_selesai[0])
        list_meja.append(meja_mau_selesai[0])
        list_meja.sort()
        meja_mau_selesai.clear()
        self.destroy()
        SelesaiGunakanMeja(self.master)


def main():
    #baca menu.txt
    file_open = open("menu1.txt")
    file_read = file_open.readlines()
    for file_line in file_read :
        file_line = file_line.strip().split(";")
        #split berdasarkan ;
        if len(file_line) == 1 :
            kategori = file_line[0].strip("===")
            list_kategori = []
            #strip === dari kategori makanan
        if len(file_line) == 3 or len(file_line) >=5 :
            print ("Daftar menu tidak valid, cek kembali menu.txt")
            exit ()
        #mencegah subjudul menu dicoba untuk diambil indexnya, dan terjadi index error
        elif len(file_line) == 4 :
            file_line[0] = file_line[0]
            kode_menu = file_line[0]
            nama_makanan = file_line[1]
            Harga = file_line [2]
            keunikan = file_line [3]
            #apabila yang diinput di bagian harga bukan angka
            try :
                int (Harga)
            except ValueError :
                print ("Daftar menu tidak valid, cek kembali menu.txt")
                exit ()
            #apabila nama makanan hanya mengandung angka (dianggap tidak ada nama makanan yang berupa angka)
            try :
                if type(int(nama_makanan)) == int :
                    print ("Daftar menu tidak valid, cek kembali menu.txt")
                    exit ()
            except ValueError :
                pass
            #memasukkan semua kode menu, nama makanan, dan harga ke kategori list atau dictionary yang diperlukan (nama dictionary sesuai kegunaan)
            list_kategori.append(kode_menu)
            daftar_kategori[kategori] = list_kategori
            dict_kode_ke_harga[kode_menu] = Harga
            dict_kode_ke_nama[kode_menu] = nama_makanan
            dict_kode_ke_keunikan[kode_menu] = keunikan
            list_menu_check_duplicate.append(nama_makanan)
            list_menu_check_duplicate.append(kode_menu)
            set_menu_check_duplicate.add(nama_makanan)
            set_menu_check_duplicate.add(kode_menu)
            #validasi menu untuk file nama makanan yang ada dua atau lebih
            if len(list_menu_check_duplicate) == len(set_menu_check_duplicate) :
                pass
            else :
                print ("Daftar menu tidak valid, cek kembali menu.txt")
                exit ()
    #apabila menu kosong atau dictionary kosong
    if daftar_kategori == {} :
        print ("Menu kosong, cek kembali menu.txt")
        exit ()
    #eksekusi main window
    window = tk.Tk()
    cafe = Main(window)
    window.mainloop()

#eksekusi program
if __name__ == '__main__':
    main()