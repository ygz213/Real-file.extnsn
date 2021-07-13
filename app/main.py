from tkinter import *
import scanafile as saf

class main_menu_class():
    def __init__(self):
        self.main_menu = Tk()
        self.main_menu.title('Real-file.extnsn')
        try:
            self.main_menu.wm_iconbitmap('icons/icon.ico')
        except:
            self.main_menu.wm_iconbitmap('@icons/icon.xbm')
        try:
            self.main_menu.state('zoomed')
        except:
            self.main_menu.attributes('-fullscreen', True)


    def run_scanner():
        user = saf.scanner()
        user.scanning_widgets()


    def main_widgets(self):
        Button(self.main_menu,
               text = 'Scan a file',   # "Scan a file" button
               font = 11,
               height = 3,
               width = 17,
               bg = '#9B5038',
               fg = '#FFF',
               activebackground = '#A01A1C',
               activeforeground = '#FFF',
               relief = 'flat',
               command = lambda: main_menu_class.run_scanner()).grid(padx = 37, pady = 14)

        Button(self.main_menu,
               text = 'Options',   # "Options" button
               font = 11,
               height = 3,
               width = 17,
               bg = '#625FA4',
               fg = '#FFF',
               activebackground = '#52467D',
               activeforeground = '#FFF',
               relief = 'flat').grid(padx = 37, pady = 14)
        
        self.main_menu.mainloop()


if __name__ == '__main__':
    user = main_menu_class()
    user.main_widgets()