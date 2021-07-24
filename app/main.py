from tkinter import *
from tkinter import messagebox
from filetype import guess

class main_menu_class():
    def __init__(self):
        self.main_menu = Tk()
        self.main_menu.title('Real-file.extnsn   (R-F.E v3.2)')
        try:
            self.main_menu.wm_iconbitmap('icons/icon.ico')
        except:
            self.main_menu.wm_iconbitmap('@icons/icon.xbm')
        try:
            self.main_menu.state('zoomed')
        except:
            self.main_menu.attributes('-fullscreen', True)

    def main_widgets(self):
        extension_information = StringVar()
        extension_information.set("Paste the file's path.")
        Label(textvariable = extension_information,   # Changeable string
              height = 3).pack()

        file_path = Entry(justify = 'center',   # Input box for the file's path
                          width = 50,
                          bd = 3,
                          bg = '#D4C4B7',
                          highlightthickness = 3,
                          highlightcolor = 'black',
                          selectforeground = 'black',
                           relief = 'flat')
        file_path.pack(pady = 13)

        ####### (Scanner function)
        def scanner():
            try:
                scanned_file = guess('{}'.format(file_path.get()))
                extension_information.set('This file is a {}.'.format(scanned_file.extension.upper()))
            except FileNotFoundError:
                messagebox.showerror('ERROR', 'No file found.')
            except PermissionError:
                messagebox.showerror('ERROR', 'Permission denied to access file.')
            except AttributeError:
                messagebox.showerror('ERROR', "Could not find this file's extension. It may be a text file, you can look at the file after renamed as <filename>.txt")
        #######

        Button(text = 'SCAN',   # Scanning button
               font = 18,
               height = 2,
               width = 10,
               bg = '#758E87',
               activebackground = '#576863',
               relief = 'flat',
               command = lambda: scanner()).pack()
        ####### (License informations)
        Label(text = '    • Real-file.extnsn is a free software under the MIT license and uses filetype module under the ').pack(side = 'left')
        MIT_link = Label(text = 'MIT License', fg = 'blue', cursor = 'hand2')
        MIT_link.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
        MIT_link.pack(side = 'left')
        Label(text = '.').pack(side = 'left')
        #######
        self.main_menu.mainloop()


if __name__ == '__main__':
    user = main_menu_class()
    user.main_widgets()