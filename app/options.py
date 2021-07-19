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
        theme = IntVar()
        theme.set(0)

        def save_options():
            options_file = open('options.txt', 'w')
            if theme.get() == 1:
                theme.set(0)
                options_file.write('theme: False')
            elif theme.get() == 0:
                theme.set(1)
                options_file.write('theme: True')
            options_file.close()

        theme_frame = Frame(self.options_menu, bg = '#52467D', height = 3, pady = 50)
        theme_frame.pack(side = 'top')

        Checkbutton(theme_frame,
                    state = 'active',
                    bg = '#52467D',
                    activebackground = '#52467D',
                    variable = theme,
                    onvalue = 1,
                    offvalue = 0,
                    command = lambda: save_options()).pack(side = 'left')
        Label(theme_frame, text = 'Dark theme', bg = '#52467D', fg = 'white').pack(side = 'right')

        Label(self.options_menu, text = '• Restart the app after changing the options.', bg = '#52467D', fg = 'white').pack()

        ####### (License informations)
        Label(self.options_menu, text = '    • Real-file.extnsn is a free software under the MIT license and uses filetype module under the ', bg = '#52467D', fg = 'white').pack(side = 'left')
        MIT_link = Label(self.options_menu, text = 'MIT License', fg = 'blue', cursor = 'hand2')
        MIT_link.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
        MIT_link.pack(side = 'left')
        Label(self.options_menu, text = '.', bg = '#52467D', fg = 'white').pack(side = 'left')
        #######

        self.options_menu.mainloop()