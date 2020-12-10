from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

root = Tk()
root.title("The Adventure of Princess Mary")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

ttk.Label(mainframe, text="Bubble").grid(column=2, row=4, sticky=E)

def num():
    num=6
    print(str("6"))
ttk.Button(mainframe, text="num", command=num).grid(column=3, row=3, sticky=W)

image = Image.open('Princess Mary Start and End.png')
image = image.resize((600, 450), Image.ANTIALIAS)
image =  ImageTk.PhotoImage(image)
ttk.Label(mainframe, image = image).grid(column=24, row=6, sticky=N)
root.geometry('1500x600')
windowWidth = root.winfo_reqwidth()
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
print(positionRight)
print(f'+{positionRight}+0')
root.geometry(f'+{positionRight}+0')






