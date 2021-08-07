from tkinter import *
from tkinter import messagebox
from tkinter import filedialog as fd
from webbrowser import open_new_tab as ont
from filetype import guess

class uygulama():
	def __init__(self):
		self.ana_menü = Tk()
		self.ana_menü.title('Real-file.extnsn   (R-F.E v4.2)')
		self.ana_menü['bg'] = '#DEDEDE'
		try:
			self.ana_menü.wm_iconbitmap('icons/icon.ico')
		except:
			self.ana_menü.wm_iconbitmap('@icons/icon.xbm')
		try:
			self.ana_menü.state('zoomed')
		except:
			self.ana_menü.attributes('-fullscreen', True)
		self.uzantı_bilgilendirmesi = StringVar()
		self.uzantı_bilgilendirmesi.set('Taranacak dosyayı seçin veya yolunu yapıştırın.')
		self.dosya_yolu_kabı = Frame()

		self.ana_widgetlar()


	def ana_widgetlar(self):
		Label(textvariable = self.uzantı_bilgilendirmesi,   # Değişken yazı dizisi
			  bg = '#DEDEDE',
			  height = 3).pack()

		self.dosya_yolu_kabı.pack(pady = 13)

		dosya_yolu = Entry(self.dosya_yolu_kabı,
						   justify = 'center',   # Dosya yolu için giri kutusu
						   width = 60,
						   bd = 4,
						   bg = '#D4C4B7',
						   highlightthickness = 2,
						   highlightbackground = '#DEDEDE',
						   highlightcolor = '#DEDEDE',
						   selectforeground = 'black',
						   relief = 'flat')
		dosya_yolu.bind("<Return>", lambda x: tarayıcı())
		dosya_yolu.pack(side = 'left')

		####### (Dosyayı seç ve giriye yapıştır)
		def yol_al():
			dosya = fd.askopenfilename()
			dosya_yolu.delete(0, 'end')
			dosya_yolu.insert(0, dosya)
		#######

		dosyayı_seç = Button(self.dosya_yolu_kabı,
							 cursor = 'hand2',
							 text = 'Dosya seç',
							 bg = '#758E87',
							 activebackground = '#576863',
							 relief = 'flat',
							 command = lambda: yol_al()).pack(side = 'right')

		####### (Tarayıcı fonksiyonu)
		def tarayıcı():
			try:
				taranan_dosya = guess('{}'.format(dosya_yolu.get()))
				if taranan_dosya is None:
					messagebox.showerror('HATA', 'Dosyanın uzantısı bulunamadı. Muhtemelen düz bir metin dosyası (Real-file.extnsn düz metin dosyalarının uzantılarını bulamaz), uzantısını bir .TXT dosyasına çevirerek inceleyebilirsiniz.')
					return
				self.uzantı_bilgilendirmesi.set('Bu dosya bir {}.'.format(taranan_dosya.extension.upper()))
			except FileNotFoundError:
				messagebox.showerror('HATA', 'Dosya bulunamadı.')
			except PermissionError:
				messagebox.showerror('HATA', 'Dosyaya erişim reddedildi.')
			except OSError:
				messagebox.showerror('HATA', 'Geçersiz dosya yolu.')
		#######

		Button(text = 'TARA',   # Tarama düğmesi
			   cursor = 'hand2',
			   font = 18,
			   height = 2,
			   width = 10,
			   bg = '#758E87',
			   activebackground = '#576863',
			   relief = 'flat',
			   command = lambda: tarayıcı()).pack()

		####### (Lisans bilgilendirmeleri)
		Label(text = '    • Real-file.extnsn, MIT Lisansı altında özgür bir yazılımdır ve yine', bg = '#DEDEDE').pack(side = 'left')
		MIT_linki = Label(text = 'MIT Lisansı', bg = '#DEDEDE', fg = 'blue', cursor = 'hand2')
		MIT_linki.bind("<Button-1>", lambda e: ont('https://github.com/h2non/filetype.py/blob/master/LICENSE'))
		MIT_linki.pack(side = 'left')
		Label(text = 'altında olan filetype modülünü kullanır.', bg = '#DEDEDE').pack(side = 'left')
		#######
		self.ana_menü.mainloop()



if __name__ == '__main__':
	kullanıcı = uygulama()