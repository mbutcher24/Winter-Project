import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("The Adventure of Princess Mary")
'''
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
'''
class TkApp(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master = master
		self.pack()
		self.create_widgets()
		
	def create_widgets(self):
		self.imgLableImg = Image.open("Princess Mary Start and End.png")
		self.imgLableImg = ImageTk.PhotoImage(self.imgLableImg)
		self.imgLable = tk.Label(root, compound="top", image=self.imgLableImg, text="AHHH")
		self.imgLable.pack(side="top")
		


root = tk.Tk()
app = TkApp(root)
app.mainloop()

ttk.Label(mainframe, text="Bubble").grid(column=2, row=4, sticky=E)

def num():
    num=6
    print(str("6"))
ttk.Button(mainframe, text="num", command=num).grid(column=3, row=3, sticky=W)

image = Image.open('Princess Mary Start and End.png')
image = image.resize((600, 450), Image.ANTIALIAS)
image =  ImageTk.PhotoImage(image)
ttk.Label(mainframe, image = image).grid(column=24, row=6, sticky=N)

json.loads(open('The Adventures of Princess Mary.json', 'r', encoding="utf-8").read())







