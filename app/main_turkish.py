from tkinter import *

ana_menü = Tk()
ana_menü.title('Real-file.extnsn')
ana_menü.wm_iconbitmap('icon.ico')
try:
    ana_menü.state('zoomed')
except:
    ana_menü.attributes('-fullscreen', True)


class menü():
    Button(text = 'Dosya tarat',   # "Dosya tarat" düğmesi
           font = 11,
           height = 3,
           width = 17,
           bg = '#9B5038',
           fg = '#FFF',
           activebackground = '#A01A1C',
           activeforeground = '#FFF',
           relief = 'flat').grid(padx = 37, pady = 14)

    Button(text = 'Ayarlar',   # "Ayarlar" düğmesi
           font = 11,
           height = 3,
           width = 17,
           bg = '#625FA4',
           fg = '#FFF',
           activebackground = '#52467D',
           activeforeground = '#FFF',
           relief = 'flat').grid(padx = 37, pady = 14)

ana_menü.mainloop()
