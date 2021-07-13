from tkinter import *

class tarayıcı():
    def __init__(self):
        self.tarama_menüsü = Tk()
        self.tarama_menüsü.geometry('450x300')
        self.tarama_menüsü.resizable(False, False)
        self.tarama_menüsü.configure(background = '#A01A1C')
        self.tarama_menüsü.wm_attributes('-topmost', 1)
        self.tarama_menüsü.title('Real-file.extnsn')
        try:
            self.tarama_menüsü.wm_iconbitmap('icons/icon.ico')
        except:
            self.tarama_menüsü.wm_iconbitmap('@icons/icon.xbm')


    def tarama_widgetları(self):
        Label(self.tarama_menüsü,
              text = 'Taranacak dosyanın yolunu yapıştırın.',   # Bilgilendirme
              bg = '#A01A1C',
              fg = 'white',
              height = 3).pack()

        Entry(self.tarama_menüsü,
              justify = 'center',   # Dosya yolu için giri kutusu
              width = 50,
              bd = 3,
              bg = '#D4C4B7',
              highlightthickness = 3,
              highlightbackground = '#A01A1C',
              highlightcolor = 'black',
              selectforeground = 'black',
              relief = 'flat').pack(pady = 15)

        Button(self.tarama_menüsü,
               text = 'TARA',   # Tarama düğmesi
               font = 18,
               height = 2,
               width = 10,
               bg = '#758E87',
               activebackground = '#576863',
               relief = 'flat').pack()

        self.tarama_menüsü.mainloop()