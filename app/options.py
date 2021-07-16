from tkinter import *
from webbrowser import open_new_tab as ont

class options_class():
    def __init__(self):
        self.options_menu = Tk()
        self.options_menu.geometry('600x300')
        self.options_menu.resizable(False, False)
        self.options_menu.configure(background = '#52467D')
        self.options_menu.wm_attributes('-topmost', 1)
        self.options_menu.title('Real-file.extnsn   (R-F.E v3)')
        try:
            self.options_menu.wm_iconbitmap('icons/icon.ico')
        except:
            self.options_menu.wm_iconbitmap('@icons/icon.xbm')


    def options_widgets(self):
        Label(self.options_menu,
              text = 'COMING SOON',
              bg = '#52467D',
              fg = '#FFF',
              font = (None, 18)).pack(pady = 30)
        ####### (License informations)
        Label(self.options_menu, text = '    • Real-file.extnsn is a free software under the MIT license and uses filetype module under the ', bg = '#52467D', fg = 'white').pack(side = 'left')
        MIT_link = Label(self.options_menu, text = 'MIT License', fg = 'blue', cursor = 'hand2')
        MIT_link.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
        MIT_link.pack(side = 'left')
        Label(self.options_menu, text = '.', bg = '#52467D', fg = 'white').pack(side = 'left')
        #######

        self.options_menu.mainloop()