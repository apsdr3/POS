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


"""
NEED TO LEARN HOW TO MAKE GRID VIEW OR TABLE LIST ON PYTHON
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
        
        #NEED TO CHECK IF I CAN USE MENU BUTTONS INSTEAD OF MENU!
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

        #First frame inside the current MainPage Window Frame
        frame1 = Frame(self, bg = "red")
        frame1.grid(row = 0, column = 0, sticky = W)
        
        frame1.label = tk.Label(self, text="Main Page", font=SMALL_FONT)
        frame1.label.grid(row = 0, column = 0, sticky = W)

        itemScanNumber = StringVar()    #creates the object itemScanNumber with a string variable type
        frame1.EntryBox = ttk.Entry(self, textvariable = itemScanNumber)   #creates an entry box and allows the entry of a string variable
        frame1.EntryBox.grid(row = 0, column = 1, sticky = W)

        print(itemScanNumber.get())

        def printNumber():
            print("Your Number: " + itemScanNumber.get())
            return

        frame1.button = ttk.Button(self, text = "CLICK ME FOR SCAN NUMBER!", command = printNumber)#command=fileExplorer)
        frame1.button.grid(row = 0, column = 2, sticky = W)

        frame1.button1 = ttk.Button(self, text = "CLICK ME!", command = lambda: controller.show_frame(MasterFilePage))#command=fileExplorer)
        frame1.button1.grid(row = 0, column = 3, sticky = W)
        #need to use .place instead of .pack, for next iteration



        #Second frame inside the current MainPage Window Frame
        frame2 = Frame(self, bg = "blue")
        frame2.grid(row = 1, column = 0, sticky = W)
        
        frame2.label = tk.Label(self, text="Main Page2", font=SMALL_FONT)
        frame2.label.grid(row = 0, column = 0, sticky = W)
        #THIS CREATES THE GRID TO OUTPUT THE DATA QUERIED FROM THE MASTER FILE
        #Description of Box: 'X' amount goind down, i.e. number of items, 6 descriptive columns: Bar Code, Product Description, Amount, Quantity, Additional Discount, Total Amount
        #Created a frame within the MainPage Frame
        #frame2.canvasGrid = Canvas(self, height = 300, width = 300, bg = "white")
        #frame2.canvasGrid.grid(row = 0, column = 0, sticky = W)


"""        
        gridFrame = Frame(self)
        gridFrame.pack()    #need to fix these into a grid later on
        #gridFrame.labelGF = tk.Label(self, text="TEST FRAME", font=SMALL_FONT, relief = SUNKEN) #SUNKENS MAKES IT GO BEHIND
        #gridFrame.labelGF.pack(pady=10, padx=10)
        
        #Created the "Dynamically allocated grid view entry boxes"
        gridFrame.labelGF1 = tk.Label(self, text="Bar Code", font=LARGE_FONT, relief = SUNKEN)
        gridFrame.labelGF1.grid(row = 0, column = 0, sticky = W)

        gridFrame.labelGF2 = tk.Label(self, text="Product Description", font=LARGE_FONT, relief = SUNKEN)
        gridFrame.labelGF2.grid(row = 0, column = 1, sticky = W)

        gridFrame.labelGF3 = tk.Label(self, text="Amount", font=LARGE_FONT, relief = SUNKEN)
        gridFrame.labelGF3.grid(row = 0, column = 2, sticky = W)

        gridFrame.labelGF4 = tk.Label(self, text="Quantity", font=LARGE_FONT, relief = SUNKEN)
        gridFrame.labelGF4.grid(row = 0, column = 3, sticky = W)

        gridFrame.labelGF5 = tk.Label(self, text="Discount", font=LARGE_FONT, relief = SUNKEN)
        gridFrame.labelGF5.grid(row = 0, column = 4, sticky = W)

        gridFrame.labelGF6 = tk.Label(self, text="Total", font=LARGE_FONT, relief = SUNKEN)
        gridFrame.labelGF6.grid(row = 0, column = 5, sticky = W)

"""


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