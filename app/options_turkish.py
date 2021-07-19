from tkinter import *
from webbrowser import open_new_tab as ont

class ayarlar_sınıfı():
    def __init__(self):
        self.ayarlar_menüsü = Tk()
        self.ayarlar_menüsü.geometry('650x300')
        self.ayarlar_menüsü.resizable(False, False)
        self.ayarlar_menüsü.configure(background = '#52467D')
        self.ayarlar_menüsü.wm_attributes('-topmost', 1)
        self.ayarlar_menüsü.title('Real-file.extnsn   (R-F.E v3)')
        try:
            self.ayarlar_menüsü.wm_iconbitmap('icons/icon.ico')
        except:
            self.ayarlar_menüsü.wm_iconbitmap('@icons/icon.xbm')


    def ayarların_widgetları(self):
        tema = IntVar()
        tema.set(0)

        def ayarları_kaydet():
            ayarlar_dosyası = open('options.txt', 'w')
            if tema.get() == 1:
                tema.set(0)
                ayarlar_dosyası.write('theme: False')
            elif tema.get() == 0:
                tema.set(1)
                ayarlar_dosyası.write('theme: True')
            ayarlar_dosyası.close()

        tema_kabı = Frame(self.ayarlar_menüsü, bg = '#52467D', height = 3, pady = 50)
        tema_kabı.pack(side = 'top')

        Checkbutton(tema_kabı,
                    state = 'active',
                    bg = '#52467D',
                    activebackground = '#52467D',
                    variable = tema,
                    onvalue = 1,
                    offvalue = 0,
                    command = lambda: ayarları_kaydet()).pack(side = 'left')
        Label(tema_kabı, text = 'Koyu tema', bg = '#52467D', fg = 'white').pack(side = 'right')

        Label(self.ayarlar_menüsü, text = '• Ayarları değiştirdikten sonra uygulamayı yeniden başlatın.', bg = '#52467D', fg = 'white').pack()

        ####### (Lisans bilgilendirmeleri)
        Label(self.ayarlar_menüsü, text = '    • Real-file.extnsn, MIT Lisansı altında özgür bir yazılımdır ve yine', bg = '#52467D', fg = 'white').pack(side = 'left')
        MIT_linki = Label(self.ayarlar_menüsü, text = 'MIT Lisansı', fg = 'blue', cursor = 'hand2')
        MIT_linki.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
        MIT_linki.pack(side = 'left')
        Label(self.ayarlar_menüsü, text = 'altında olan filetype modülünü kullanır.', bg = '#52467D', fg = 'white').pack(side = 'left')
        #######

        self.ayarlar_menüsü.mainloop()