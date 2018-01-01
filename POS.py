import tkinter as tk
import pyexcel as pe


from tkinter import filedialog
from tkinter import *

LARGE_FONT=("Verdana", 12)
SMALL_FONT=("Verdana", 10)

masterList = []

class POS(tk.Tk):
	#initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)	#initializes tk module
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)	#"packs" or pushes the container to the top

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}	#creates an object to hold multiple frames i.e. more windows/tabs

        frame = MainPage(container, self)
        self.frames[MainPage] = frame	#adds frame into frames object
        frame.grid(row=0, column = 0, sticky="nsew")	#sets frame structure, nsew = north south east west
        self.show_frame(MainPage)


    #shows the frame when called
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() 



#Start frame: Prompts user to find master key file
class StartFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="", font=SMALL_FONT)
        label.pack(pady=50, padx=50)

        button1 = tk.Button(self, text = "Please specify the product master file", command=fileExplorer)
        button1.pack()


#Main Landing Page frame
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        label = tk.Label(self, text="Main Page", font=SMALL_FONT)
        label.pack(pady=50, padx=50)

        button1 = tk.Button(self, text = "CLICK ME!", command=fileExplorer)
        button1.pack(pady=10, padx=50)


#once button is clicked, it prompts user to find file then it outputs the contents of the file
def fileExplorer():
    #intializes another instance of tkinter
    try:    
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XLS files","*.xls"),("XLSX files","*.xlsx")))
        
        if re.match("[A-Za-z0-9]",filename):
            #sheet = pe.get_sheet(file_name=filename) #puts data into readable sheet, array is more useful
            sheet = pe.get_array(file_name=filename) #puts data into array

            masterList = sheet
            #print(sheet[4]) #prints: everything
            #print(sheet[4]) #prints: [20297939, 'AC EDT 75ML SPRAY TEST', 250, 0, 3605520297939]
            #print(sheet[4][0]) #prints: 20297939
            return

        else:
            print("Error") #need to make error frame
    
    except ValueError:
        print("Error2") #need to make error frame
        return
    
    return



#runs program
app = POS()
app.mainloop()