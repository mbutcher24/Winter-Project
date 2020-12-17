import tkinter as tk
from PIL import ImageTk, Image
import json
import functools

root = tk.Tk()
root.title("The Adventure of Princess Mary")
#Creates and titles new window for the game

class TkApp(tk.Frame):
        def __init__(self, master=None):
                super().__init__(master)
                self.master = master
                self.pack()
                self.perry = []
                self.create_widgets()
                self.dictionary = json.loads(open('The Adventures of Princess Mary.json', 'r', encoding="utf-8").read())
               # self.story_part("Intro")
                #Gives access to json file containing story routes


        def create_widgets(self):
                self.dufenshmerts = tk.Label(self)
                self.incorporated = tk.Frame(self.dufenshmerts, height = 110, width = 850)
                self.incorporated.pack_propagate(0)
                self.incorporated.place(x=80, y=440)
                self.evil = tk.Label(self.incorporated, wraplength=800, bg = "#E5C2D7")
                #Creates text and images, controlling sizing and color


'''
        def story_part(self, name):
                if name == 'Quit':
                        root.destroy()
                #Stops the game
                else:
                        image = Image.open(self.dictionary[name]['image'])
                        image = image.resize((1000, 600), Image.ANTIALIAS)
                        image =  ImageTk.PhotoImage(image, master=self.master)
                        self.dufenshmerts.image = image
                        self.dufenshmerts.configure(image = image)
                        self.dufenshmerts.pack(side="top")
                        self.evil.configure(text = (self.dictionary[name]['text']))
                        self.evil.pack(side="top", fill = tk.BOTH, expand = 1)
                        
                        for egg in self.perry:
                                egg.pack_forget()
                        self.perry = []
                        for path in self.dictionary[name]['choices']:
                                platypus = tk.Button(self, text = path['text'], command = functools.partial(self.story_part, path['direction']))
                                platypus.pack(side="top")
                                self.perry.append(platypus)
                
                '''

app = TkApp(root)
app.mainloop()







