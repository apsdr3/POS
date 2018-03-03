import tkinter as tk
from tkinter import *

class POS(tk.Tk):
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}

        for F in (ErrorPage, MainPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column = 0, sticky = "nsew")
        
        self.show_frame(MainPage)

    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() 


class MainPage(tk.Frame):
    entry = "N/A"

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        global entry

        frame = tk.Frame(self)
        frame.pack(fill = BOTH)

        button = Button(frame, text = "OK", command = self.bindHello)
        button.pack(pady=10, padx=10)

        entry = StringVar()
        e = Entry(frame, textvariable = entry, width = 15)
        e.pack(pady = 10, padx = 10)

        frame.winfo_toplevel().bind('<Return>', self.bindHello)

    def bindHello(self, event=None):
        print("HELLO " + entry.get())

#Yes this doesn't do anything but I need it for the frame container as set before
class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        frame = tk.Frame(self)
        frame.pack(fill = BOTH)

        button = Button(frame, text = "OK", command = self.bindHello)
        button.pack(pady=5, padx=10)

        frame.bind("<Return>", self.bindHello)

    def bindHello(self, event=None):
        print("HELLO2")


app = POS()
app.mainloop()


"""
from tkinter import *
master = Tk()

def callback(event=None):
    print("Hello " + entry.get())

entry = StringVar()
e = Entry(master, textvariable = entry, width = 15)
e.pack()

b = Button(master, text="OK", command = callback)
b.pack()
master.bind("<Return>", callback)

mainloop()"""