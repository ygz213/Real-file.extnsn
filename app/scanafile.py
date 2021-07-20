from tkinter import *
from tkinter import messagebox
from filetype import guess

class scanner_class():
    def __init__(self):
        self.scanning_menu = Tk()
        self.scanning_menu.geometry('450x300')
        self.scanning_menu.resizable(False, False)
        self.scanning_menu.configure(background = '#A01A1C')
        self.scanning_menu.wm_attributes('-topmost', 1)
        self.scanning_menu.title('Real-file.extnsn   (R-F.E v3.2)')
        try:
            self.scanning_menu.wm_iconbitmap('icons/icon.ico')
        except:
            self.scanning_menu.wm_iconbitmap('@icons/icon.xbm')


    def scanning_widgets(self):
        extension_information = StringVar(self.scanning_menu)
        extension_information.set("Paste the file's path.")
        Label(self.scanning_menu,
              textvariable = extension_information,   # Changeable string
              bg = '#A01A1C',
              fg = 'white',
              height = 3).pack()

        file_path = Entry(self.scanning_menu,
                           justify = 'center',   # Input box for the file's path
                           width = 50,
                           bd = 3,
                           bg = '#D4C4B7',
                           highlightthickness = 3,
                           highlightbackground = '#A01A1C',
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

        Button(self.scanning_menu,
               text = 'SCAN',   # Scanning button
               font = 18,
               height = 2,
               width = 10,
               bg = '#758E87',
               activebackground = '#576863',
               relief = 'flat',
               command = lambda: scanner()).pack()

        self.scanning_menu.mainloop()