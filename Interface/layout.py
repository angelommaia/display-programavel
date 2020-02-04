# -*- coding: utf-8 -*-
from tkinter import *
#import subprocess

class Application(Frame):
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.grid()
		file = open("status.txt","r")
		self.master.title(file.read())
		

root = Tk()
root.geometry("400x200+200+200")
root.iconbitmap('bolt.ico')	
app=Application(master=root)
app.mainloop()