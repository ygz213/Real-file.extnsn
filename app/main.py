from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from webbrowser import open_new_tab as ont
from filetype import guess

class application():
	def __init__(self):
		self.main_menu = Tk()
		self.main_menu.title('Real-file.extnsn   (R-F.E v4)')
		self.main_menu['bg'] = '#DEDEDE'
		try:
			self.main_menu.wm_iconbitmap('icons/icon.ico')
		except:
			self.main_menu.wm_iconbitmap('@icons/icon.xbm')
		try:
			self.main_menu.state('zoomed')
		except:
			self.main_menu.attributes('-fullscreen', True)
		self.extension_information = StringVar()
		self.extension_information.set("Select the file or paste the file's path.")
		self.file_path_frame = Frame()

		self.main_widgets()


	def main_widgets(self):
		Label(textvariable = self.extension_information,   # Changeable string
			  bg = '#DEDEDE',
			  height = 3).pack()

		self.file_path_frame.pack(pady = 13)

		file_path = Entry(self.file_path_frame,
						  justify = 'center',   # Input box for the file's path
						  width = 60,
						  bd = 4,
						  bg = '#D4C4B7',
						  highlightthickness = 2,
						  highlightbackground = '#DEDEDE',
						  highlightcolor = '#DEDEDE',
						  selectforeground = 'black',
						  relief = 'flat')
		file_path.bind("<Return>", lambda x: scanner())
		file_path.pack(side = 'left')

		####### (Select the file and paste to the entry)
		def get_path():
			file = fd.askopenfilename()
			file_path.delete(0, 'end')
			file_path.insert(0, file)
		#######

		select_file = Button(self.file_path_frame,
							 text = 'Select file',
							 bg = '#758E87',
							 activebackground = '#576863',
							 relief = 'flat',
							 command = lambda: get_path()).pack(side = 'right')

		####### (Scanner function)
		def scanner():
			try:
				scanned_file = guess('{}'.format(file_path.get()))
				if scanned_file is None:
					messagebox.showerror('ERROR', "Could not find this file's extension. It may be a text file, you can look at the file after renamed as <filename>.txt")
					return
				self.extension_information.set('This file is a {}.'.format(scanned_file.extension.upper()))
			except FileNotFoundError:
				messagebox.showerror('ERROR', 'File not found.')
			except PermissionError:
				messagebox.showerror('ERROR', 'Permission denied to access file.')
			except OSError:
				messagebox.showerror('ERROR', 'Invalid file path.')
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
		Label(text = '     • Real-file.extnsn is a free software under the MIT License and uses filetype module under the ', bg = '#DEDEDE').pack(side = 'left')
		MIT_link = Label(text = 'MIT License', bg = '#DEDEDE', fg = 'blue', cursor = 'hand2')
		MIT_link.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
		MIT_link.pack(side = 'left')
		Label(text = '.', bg = '#DEDEDE').pack(side = 'left')
		#######
		self.main_menu.mainloop()



if __name__ == '__main__':
	user = application()