from tkinter import *
import scanafile as saf
import options as opo

class main_menu_class():
    def __init__(self):
        self.main_menu = Tk()
        self.main_menu.title('Real-file.extnsn   (R-F.E v3)')
        try:
            self.main_menu.wm_iconbitmap('icons/icon.ico')
        except:
            self.main_menu.wm_iconbitmap('@icons/icon.xbm')
        try:
            self.main_menu.state('zoomed')
        except:
            self.main_menu.attributes('-fullscreen', True)
        try:
            options_file = open('options.txt')
            if options_file.readlines(0)[0] == 'theme: True':
                self.main_menu['bg'] = '#1B1E23'
        except FileNotFoundError:
            pass


    def main_widgets(self):
        def run_scanner():
            scanner_user = saf.scanner_class()
            scanner_user.scanning_widgets()
        def run_settings():
            settings_user = opo.options_class()
            settings_user.options_widgets()

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
               command = lambda: run_scanner()).grid(padx = 37, pady = 14)

        Button(self.main_menu,
               text = 'Options',   # "Options" button
               font = 11,
               height = 3,
               width = 17,
               bg = '#625FA4',
               fg = '#FFF',
               activebackground = '#52467D',
               activeforeground = '#FFF',
               relief = 'flat',
               command = lambda: run_settings()).grid(padx = 37, pady = 14)
        
        self.main_menu.mainloop()


if __name__ == '__main__':
    user = main_menu_class()
    user.main_widgets()