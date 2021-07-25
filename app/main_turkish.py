from tkinter import *
from tkinter import messagebox
from filetype import guess

class ana_menü_sınıfı():
    def __init__(self):
        self.ana_menü = Tk()
        self.ana_menü.title('Real-file.extnsn   (R-F.E v3.4)')
        self.ana_menü['bg'] = '#DEDEDE'
        try:
            self.ana_menü.wm_iconbitmap('icons/icon.ico')
        except:
            self.ana_menü.wm_iconbitmap('@icons/icon.xbm')
        try:
            self.ana_menü.state('zoomed')
        except:
            self.ana_menü.attributes('-fullscreen', True)


    def ana_widgetlar(self):
        uzantı_bilgilendirmesi = StringVar()
        uzantı_bilgilendirmesi.set('Taranacak dosyanın yolunu yapıştırın.')
        Label(textvariable = uzantı_bilgilendirmesi,   # Değişken yazı dizisi
              bg = '#DEDEDE',
              height = 3).pack()

        dosya_yolu = Entry(justify = 'center',   # Dosya yolu için giri kutusu
                           width = 50,
                           bd = 3,
                           bg = '#D4C4B7',
                           highlightthickness = 3,
                           highlightbackground = '#DEDEDE',
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
            except OSError:
                messagebox.showerror('HATA', 'Geçersiz dosya yolu.')
            except PermissionError:
                messagebox.showerror('HATA', 'Dosyaya erişim reddedildi.')
            except AttributeError:
                messagebox.showerror('HATA', 'Dosyanın uzantısı bulunamadı. Muhtemelen düz bir metin dosyası (Real-file.extnsn düz metin dosyalarının uzantılarını bulamaz), uzantısını bir .TXT dosyasına çevirerek inceleyebilirsiniz.')
        #######

        Button(text = 'TARA',   # Tarama düğmesi
               font = 18,
               height = 2,
               width = 10,
               bg = '#758E87',
               activebackground = '#576863',
               relief = 'flat',
               command = lambda: tarayıcı()).pack()

        ####### (Lisans bilgilendirmeleri)
        Label(text = '    • Real-file.extnsn, MIT Lisansı altında özgür bir yazılımdır ve yine', bg = '#DEDEDE').pack(side = 'left')
        MIT_linki = Label(text = 'MIT Lisansı', bg = '#DEDEDE', fg = 'blue', cursor = 'hand2')
        MIT_linki.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
        MIT_linki.pack(side = 'left')
        Label(text = 'altında olan filetype modülünü kullanır.', bg = '#DEDEDE').pack(side = 'left')
        #######
        self.ana_menü.mainloop()



if __name__ == '__main__':
    kullanıcı = ana_menü_sınıfı()
    kullanıcı.ana_widgetlar()