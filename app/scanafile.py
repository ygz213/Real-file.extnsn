from tkinter import *

class scanner():
    def __init__(self):
        self.scanning_menu = Tk()
        self.scanning_menu.geometry('450x300')
        self.scanning_menu.resizable(False, False)
        self.scanning_menu.configure(background = '#A01A1C')
        self.scanning_menu.wm_attributes('-topmost', 1)
        self.scanning_menu.title('Real-file.extnsn')
        try:
            self.scanning_menu.wm_iconbitmap('icons/icon.ico')
        except:
            self.scanning_menu.wm_iconbitmap('@icons/icon.xbm')


    def scanning_widgets(self):
        Label(self.scanning_menu,
              text = "Paste the file's path.",   # Information
              bg = '#A01A1C',
              fg = 'white',
              height = 3).pack()

        Entry(self.scanning_menu,
              justify = 'center',   # Input box for the file's path
              width = 50,
              bd = 3,
              bg = '#D4C4B7',
              highlightthickness = 3,
              highlightbackground = '#A01A1C',
              highlightcolor = 'black',
              selectforeground = 'black',
              relief = 'flat').pack(pady = 15)

        Button(self.scanning_menu,
               text = 'SCAN',   # Scanning button
               font = 18,
               height = 2,
               width = 10,
               bg = '#758E87',
               activebackground = '#576863',
               relief = 'flat').pack()

        self.scanning_menu.mainloop()