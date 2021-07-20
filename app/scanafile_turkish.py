from tkinter import *
from tkinter import messagebox
from filetype import guess

class tarayıcı_sınıfı():
    def __init__(self):
        self.tarama_menüsü = Tk()
        self.tarama_menüsü.geometry('450x300')
        self.tarama_menüsü.resizable(False, False)
        self.tarama_menüsü.configure(background = '#A01A1C')
        self.tarama_menüsü.wm_attributes('-topmost', 1)
        self.tarama_menüsü.title('Real-file.extnsn   (R-F.E v3.2)')
        try:
            self.tarama_menüsü.wm_iconbitmap('icons/icon.ico')
        except:
            self.tarama_menüsü.wm_iconbitmap('@icons/icon.xbm')


    def tarama_widgetları(self):
        uzantı_bilgilendirmesi = StringVar(self.tarama_menüsü)
        uzantı_bilgilendirmesi.set('Taranacak dosyanın yolunu yapıştırın.')
        Label(self.tarama_menüsü,
              textvariable = uzantı_bilgilendirmesi,   # Değişken yazı dizisi
              bg = '#A01A1C',
              fg = 'white',
              height = 3).pack()

        dosya_yolu = Entry(self.tarama_menüsü,
                           justify = 'center',   # Dosya yolu için giri kutusu
                           width = 50,
                           bd = 3,
                           bg = '#D4C4B7',
                           highlightthickness = 3,
                           highlightbackground = '#A01A1C',
                           highlightcolor = 'black',
                           selectforeground = 'black',
                           relief = 'flat')
        dosya_yolu.pack(pady = 13)

        ####### (Tarayıcı fonksiyonu)
        def tarayıcı():
            try:
                taranan_dosya = guess('{}'.format(dosya_yolu.get()))
                uzantı_bilgilendirmesi.set('Bu dosya bir {}.'.format(taranan_dosya.extension.upper()))
            except FileNotFoundError:
                messagebox.showerror('HATA', 'Dosya bulunamadı.')
            except PermissionError:
                messagebox.showerror('HATA', 'Dosyaya erişim reddedildi.')
            except AttributeError:
                messagebox.showerror('HATA', 'Dosyanın uzantısı bulunamadı. Muhtemelen düz bir metin dosyası (Real-file.extnsn düz metin dosyalarının uzantılarını bulamaz), uzantısını bir .TXT dosyasına çevirerek inceleyebilirsiniz.')
        #######

        Button(self.tarama_menüsü,
               text = 'TARA',   # Tarama düğmesi
               font = 18,
               height = 2,
               width = 10,
               bg = '#758E87',
               activebackground = '#576863',
               relief = 'flat',
               command = lambda: tarayıcı()).pack()

        self.tarama_menüsü.mainloop()