import tkinter as tk
import tkinter.messagebox as showinfo

#Window awal
class MainWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master.title("Karung Ajaib")
        self.pack()
        self.create_widgets()
#Sesuaikan command tiap button dengan functionnya
    def create_widgets(self):
        self.label = tk.Label(self, \
                              text = 'Selamat datang Dek Depe di Karung Ajaib. Silahkan pilih Menu yang tersedia')

        self.btn_lihat_daftar_karung = tk.Button(self, \
                                                text = "LIHAT DAFTAR KARUNG", \
                                                command = self.popup_lihat_karung)
        self.btn_masukkan_item = tk.Button(self, \
                                            text = "MASUKKAN ITEM", \
                                            command = self.popup_add_item)
        self.btn_keluarkan_item = tk.Button(self, \
                                        text = "KELUARKAN ITEM", \
                                        command = self.popup_keluarkan_item)
        self.btn_exit = tk.Button(self, \
                                  text = "EXIT", \
                                  command = self.master.destroy)

        self.label.pack()
        self.btn_lihat_daftar_karung.pack()
        self.btn_masukkan_item.pack()
        self.btn_keluarkan_item.pack()
        self.btn_exit.pack()

    # semua item dalam karung
    def popup_lihat_karung(self):
        PopupLihatKarung(self.master)

    # menu masukkan item
    def popup_add_item(self):
        PopupAddItem(self.master)

    # menu keluarkan item
    def popup_keluarkan_item(self):
        PopupKeluarkanItem(self.master)
#class untuk lihat karung
class PopupLihatKarung(object):
  def __init__(self,master):
    self.main_window = tk.Toplevel()
    self.main_window.geometry("280x100")
    self.main_window.wm_title("Lihat Karung")
    self.title = tk.Label(self.main_window, text='Daftar Karung Ajaib')
    self.nama = tk.Label(self.main_window, text='Nama Item')
    self.title.pack()
    self.nama.pack()
    #untuk print daftar item
    jumlah_list = len(PopupAddItem.list_item)
    #apabila terjadi index error dan program tidak berjalan dengan baik atau exit button tidak muncul
    try :
        for i in range (jumlah_list+1) :
            self.nama = tk.Label(self.main_window, text = f"{i+1}.{PopupAddItem.list_item[i]}")
            self.nama.pack()
    except IndexError:
        pass
    self.exit_button = tk.Button(self.main_window, text="EXIT", command = self.main_window.destroy)
    self.exit_button.pack()

# Class Masukkan Item 
class PopupAddItem(object):
    list_item = []
    def __init__(self,master):
        self.main_window = tk.Toplevel()
        self.main_window.wm_title("Masukkan Item")
        self.main_window.geometry("280x100")
        #print label dan entry
        self.label1 = tk.Label(self.main_window, text="Input Masukkan Item")
        self.label1.pack()
        self.label2 = tk.Label(self.main_window, text = "Nama Item")
        self.label2.pack()
        self.nama = tk.StringVar()
        self.input = tk.Entry(self.main_window, textvariable=self.nama, width=40)
        self.input.pack()
        self.button = tk.Button(self.main_window, text="Masukkan", command=self.masukkan_item)
        self.button.pack()
        self.submit_button = tk.Button(self.main_window, text = 'Masukkan', command = self.masukkan_item)

    def masukkan_item(self):
        item = self.input.get()
        #apabila item ada di list atau tidak, print error atau info
        if item in PopupAddItem.list_item :
            showinfo.showwarning (title = "ItemNotFound", message ="Item dengan {} nama sudah ada di dalam KarungAjaib. Item {} tidak bisa dimasukkan lagi.".format(item,item))
        else :
            showinfo.showinfo (title = "Berhasil", message ="Berhasil memasukkan item {}".format(item,item))
            PopupAddItem.list_item.append(item)
        self.main_window.destroy

# Class Keluarkan Item
class PopupKeluarkanItem(object):
  def __init__(self, master):
    self.main_window = tk.Toplevel()
    self.main_window.wm_title("Keluarkan item")
    self.main_window.geometry("280x100")
    #print label dan entry
    self.label1 = tk.Label(self.main_window, text="Input Keluarkan Item")
    self.label1.pack()
    self.label2 = tk.Label(self.main_window, text = "Nama Item")
    self.label2.pack()
    self.nama = tk.StringVar()
    self.input = tk.Entry(self.main_window, textvariable=self.nama, width=40)
    self.input.pack()
    self.submit_button = tk.Button(self.main_window, text = 'Ambil', command = self.keluarkan_item)
    self.submit_button.pack()
  def keluarkan_item(self):
    item = self.input.get()
    #apabila item ada di list atau tidak, print error atau info
    if item in PopupAddItem.list_item :
        showinfo.showinfo (title = "Berhasil", message ="Berhasil mengeluarkan item {}".format(item))
        PopupAddItem.list_item.remove(item)
    else :
        showinfo.showwarning (title = "ItemNotFound", message ="Item dengan {} nama tidak ada di dalam KarungAjaib. Item {} tidak bisa dikeluarkan.".format(item,item))
    self.main_window.destroy
#eksekusi program    
if __name__ == "__main__":
    root = tk.Tk()
    m=MainWindow(root)
    root.mainloop()