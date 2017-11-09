import tkinter as tk
import pyexcel as pe
from tkinter import filedialog
from tkinter import *


LARGE_FONT=("Verdana", 12)



class POS(tk.Tk):
	#initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)	#initializes tk module
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)	#"packs" or pushes the container to the top

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}	#creates an object to hold multiple frames i.e. more windows/tabs

        frame = StartPage(container, self)
        self.frames[StartPage] = frame	#adds frame into frames object
        frame.grid(row=0, column = 0, sticky="nsew")	#sets frame structure, nsew = north south east west
        self.show_frame(StartPage)


    #shows the frame when called
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() 

#once button is clicked, it prompts user to find file then it outputs the contents of the file
def qf():
    #intializes another instance of tkinter
    filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
    sheet = pe.get_sheet(file_name=filename)
    print(sheet)
    #need to have a check for whether or not there is an existing file name to open.
    return


#Start Page frame
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text = "CLICK ME!", command=qf)
        
        #opens file explorer to get file name
        #still need research on how to do        

        button1.pack()



#runs program
app = POS()
app.mainloop()