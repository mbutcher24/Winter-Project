import tkinter as tk
from PIL import Image, ImageTk
import json

class TkApp(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		self.imgLableImg = Image.open("Mary and Rapunzal.png")
		self.imgLableImg = ImageTk.PhotoImage(self.imgLableImg)
		self.imgLable = tk.Label(root, compound="top", image=self.imgLableImg, text="AHHH")
		self.imgLable.pack(side="top")
		


root = tk.Tk()
app = TkApp(root)
app.mainloop()

json.loads(open('The Adventures of Princess Mary.json', 'r', encoding="utf-8").read())
json.loads(open(f.read["Intro"]))
