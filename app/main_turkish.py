from tkinter import *
import scanafile_turkish as saft

class ana_menü_sınıfı():
    def __init__(self):
        self.ana_menü = Tk()
        self.ana_menü.title('Real-file.extnsn')
        try:
            self.ana_menü.wm_iconbitmap('icons/icon.ico')
        except:
            self.ana_menü.wm_iconbitmap('@icons/icon.xbm')
        try:
            self.ana_menü.state('zoomed')
        except:
            self.ana_menü.attributes('-fullscreen', True)


    def tarayıcıyı_başlat():
        kullanıcı = saft.tarayıcı()
        kullanıcı.tarama_widgetları()


    def ana_widgetlar(self):
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
               command = lambda: ana_menü_sınıfı.tarayıcıyı_başlat()).grid(padx = 37, pady = 14)

        Button(self.ana_menü,
               text = 'Ayarlar',   # "Ayarlar" düğmesi
               font = 11,
               height = 3,
               width = 17,
               bg = '#625FA4',
               fg = '#FFF',
               activebackground = '#52467D',
               activeforeground = '#FFF',
               relief = 'flat').grid(padx = 37, pady = 14)
        
        self.ana_menü.mainloop()


if __name__ == '__main__':
    kullanıcı = ana_menü_sınıfı()
    kullanıcı.ana_widgetlar()