from tkinter import *
import scanafile_turkish as saft
import options_turkish as opot

class ana_menü_sınıfı():
    def __init__(self):
        self.ana_menü = Tk()
        self.ana_menü.title('Real-file.extnsn   (R-F.E v3.2)')
        try:
            self.ana_menü.wm_iconbitmap('icons/icon.ico')
        except:
            self.ana_menü.wm_iconbitmap('@icons/icon.xbm')
        try:
            self.ana_menü.state('zoomed')
        except:
            self.ana_menü.attributes('-fullscreen', True)
        try:
            ayarlar_dosyası = open('options.txt')
            if ayarlar_dosyası.readlines(0)[0] == 'theme: True':
                self.ana_menü['bg'] = '#1B1E23'
        except FileNotFoundError:
            pass


    def ana_widgetlar(self):
        def tarayıcıyı_başlat():
            tarayıcı_kullanıcısı = saft.tarayıcı_sınıfı()
            tarayıcı_kullanıcısı.tarama_widgetları()
        def ayarları_başlat():
            ayarlar_kullanıcısı = opot.ayarlar_sınıfı()
            ayarlar_kullanıcısı.ayarların_widgetları()

        Button(self.ana_menü,
               text = 'Dosya tarat',   # "Dosya tarat" düğmesi
               font = 11,
               height = 3,
               width = 17,
               bg = '#9B5038',
               fg = '#FFF',
               activebackground = '#A01A1C',
               activeforeground = '#FFF',
               relief = 'flat',
               command = lambda: tarayıcıyı_başlat()).grid(padx = 37, pady = 14)

        Button(self.ana_menü,
               text = 'Ayarlar',   # "Ayarlar" düğmesi
               font = 11,
               height = 3,
               width = 17,
               bg = '#625FA4',
               fg = '#FFF',
               activebackground = '#52467D',
               activeforeground = '#FFF',
               relief = 'flat',
               command = lambda: ayarları_başlat()).grid(padx = 37, pady = 14)

        self.ana_menü.mainloop()



if __name__ == '__main__':
    kullanıcı = ana_menü_sınıfı()
    kullanıcı.ana_widgetlar()