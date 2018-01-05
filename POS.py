import tkinter as tk
from tkinter import ttk
import pyexcel as pe


from tkinter import filedialog
from tkinter import *

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

masterList = [] #list for Master File
errorCode = 0
"""
Error Code Legend:
0 = No error
1 = Master File Error
"""




class POS(tk.Tk):
	#initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)	#initializes tk module

        #tk.Tk.iconbitmap(self, default="<image-file-name.ico>") #gives an icon for the program, top left corner, has to be an ICON
        tk.Tk.wm_title(self, "FONZY POS Program")   #Gives name to program client application

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)	#"packs" or pushes the container to the top

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)    #adds menu
        
        filemenu = tk.Menu(menubar, tearoff = 0)    #creates a menubar on the app
        filemenu.add_command(label = "Main", command = lambda: popupmsg("Not supported just yet!"))    #need to create this to change windows between frames
        filemenu.add_separator()    #adds separator between different file menus
        menubar.add_cascade(label= "Main", menu = filemenu) #adds filemenu bar to the program menubar

        filemenu2 = tk.Menu(menubar, tearoff = 0)
        filemenu2.add_command(label = "Reports", command = lambda: popupmsg("Not supported just yet!!"))    #need to create this to change windows between frames
        filemenu2.add_separator()
        menubar.add_cascade(label= "Reports", menu = filemenu2)

        tk.Tk.config(self, menu = menubar)

        self.frames = {}	#creates an object to hold multiple frames i.e. more windows/tabs

        for F in (MainPage, MasterFilePage, ErrorPage, PaymentPage): #Adds frames onto list, to add more frames, just add it to the list
            frame = F(container, self)
            self.frames[F] = frame	#adds frame into frames object
            frame.grid(row=0, column = 0, sticky="nsew")	#sets frame structure, nsew = north south east west
        
        self.show_frame(MainPage)


    #shows the frame when called
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() 




#Main Landing Page frame
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        itemScanNumber = StringVar()    #creates the object itemScanNumber with a string variable type

        label = tk.Label(self, text="Main Page", font=SMALL_FONT)
        label.pack(pady=10, padx=10)

        EntryBox = ttk.Entry(self, textvariable = itemScanNumber)   #creates an entry box and allows the entry of a string variable
        EntryBox.pack(pady=10, padx=10)
        print(itemScanNumber.get())

        def printNumber():
            print("Your Number: " + itemScanNumber.get())
            return
        
        button = ttk.Button(self, text = "CLICK ME FOR SCAN NUMBER!", command = printNumber)#command=fileExplorer)
        button.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text = "CLICK ME!", command = lambda: controller.show_frame(MasterFilePage))#command=fileExplorer)
        button1.pack(pady=10, padx=10)
        #need to use .place instead of .pack, for next iteration


   


#Start frame: Prompts user to find master key file
class MasterFilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="Please specify the product master file", font=SMALL_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text = "OK", command=fileExplorer)
        button1.pack(pady=5, padx=10)

        if errorCode == 1:
            controller.show_frame(ErrorPage)




#Payment page where user goes to after a sale is to purchased
class PaymentPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

        label = tk.Label(self, text="PAYMENT HERE!", font=SMALL_FONT)
        label.pack(pady=10, padx=10)




#error page for when there is a possible error
class ErrorPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        if errorCode == 1:
            label = tk.Label(self, text="Error! Please input a correct Master File Document", font=SMALL_FONT)
            label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text = "OK", command=lambda: controller.show_frame(MasterFilePage)) #One can also do command=quit to quit out of the program
        button1.pack(pady=5, padx=10)



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

            errorCode = 0 #resets errorCode
            return

        else:
            errorCode = 1
            return
    
    except ValueError:
        errorCode = 1
        return



#Creates popup message bars
def popupmsg(msg):
    popup = tk.Tk()

    popup.wm_title("!")
    label = ttk.Label(popup, text = msg, font = NORMAL_FONT)
    label.pack(side = "top", fill = "x", pady = 10)

    button1 = ttk.Button(popup, text = "Okay", command = popup.destroy)
    button1.pack()
    popup.mainloop()





#runs program
app = POS()
app.geometry("640x500") #makes app into a 1280x720p screen, can change size to liking
app.mainloop()