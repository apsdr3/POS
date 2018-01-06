import tkinter as tk
from tkinter import ttk
import pyexcel as pe
import datetime

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

"""
#time = datetime.datetime.now() #time.time()
"""


class POS(tk.Tk):
	#initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)	#initializes tk module

        #tk.Tk.iconbitmap(self, default="<image-file-name.ico>") #gives an icon for the program, top left corner, has to be an ICON
        tk.Tk.wm_title(self, "FONZY")   #Gives name to program client application

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

        for F in (MainPage, ErrorPage, PaymentPage): #Adds frames onto list, to add more frames, just add it to the list
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

# FRAME1 ################## CUSTOMER NAME, TELEPHONE NUMBER ######################

        #First frame inside the current MainPage Window Frame
        frame1 = Frame(self, bg = "green")
        frame1.pack()#grid(row = 0, column = 0, sticky = W)
        
#CUSTOMER NAME
        frame1.label = tk.Label(frame1, text="Customer Name", font=SMALL_FONT)
        frame1.label.grid(row = 0, column = 0, padx=5, pady=5, sticky = W)

        customerName = StringVar()    #creates the object customerName with a string variable type
        frame1.EntryBox1 = ttk.Entry(frame1, textvariable = customerName, width = 40)   #creates an entry box and allows the entry of a string variable
        frame1.EntryBox1.grid(row = 0, column = 1, padx=5, pady=5, sticky = W)
        #print(customerName.get())

#PHONE
        frame1.label2 = tk.Label(frame1, text="Phone", font=SMALL_FONT)
        frame1.label2.grid(row = 0, column = 2, padx=5, pady=5, sticky = W)
        
        phone = StringVar()    #creates the object phone with a string variable type
        frame1.EntryBox2 = ttk.Entry(frame1, textvariable = phone, width = 40)   #creates an entry box and allows the entry of a string variable
        frame1.EntryBox2.grid(row = 0, column = 3, padx=5, pady=5, sticky = W)
###################################################################################


# FRAME2 ########################## ADDRESS #####################################
        
        #Secibd frame inside the current MainPage Window Frame
        frame2 = Frame(self, bg = "red")
        frame2.pack()#grid(row = 1, column = 0, sticky = W)

#ADDRESS
        frame2.label = tk.Label(frame2, text="Address", font=SMALL_FONT)
        frame2.label.grid(row = 1, column = 0, padx=5, pady=5, sticky = W)

        address = StringVar()    #creates the object address with a string variable type
        frame2.EntryBox = ttk.Entry(frame2, textvariable = address, width = 99)   #creates an entry box and allows the entry of a string variable
        frame2.EntryBox.grid(row = 1, column = 1, padx=5, pady=5, sticky = W)
###################################################################################


# FRAME3 ########################## ENTRY BOX GRID #####################################
        #Third frame inside the current MainPage Window Frame
        frame3 = Frame(self, bg = "black")
        frame3.pack()#grid(row = 2, column = 0)
        
        #THIS CREATES THE GRID TO OUTPUT THE DATA QUERIED FROM THE MASTER FILE
        #Description of Box: 'X' amount goind down, i.e. number of items, 6 descriptive columns: Bar Code, Product Description, Amount, Quantity, Additional Discount, Total Amount
        #This is the header GRID VIEW Labels
        frame3.labelGF1 = tk.Label(frame3, text="Bar Code", font=NORMAL_FONT, relief = SUNKEN, width = 16)
        frame3.labelGF1.grid(row = 0, column = 0)

        frame3.labelGF2 = tk.Label(frame3, text="Product Description", font=NORMAL_FONT, relief = SUNKEN, width = 30)
        frame3.labelGF2.grid(row = 0, column = 1)

        frame3.labelGF3 = tk.Label(frame3, text="Price", font=NORMAL_FONT, relief = SUNKEN, width = 10)
        frame3.labelGF3.grid(row = 0, column = 2)

        frame3.labelGF4 = tk.Label(frame3, text="Quantity", font=NORMAL_FONT, relief = SUNKEN, width = 8)
        frame3.labelGF4.grid(row = 0, column = 3)

        frame3.labelGF5 = tk.Label(frame3, text="Discount", font=NORMAL_FONT, relief = SUNKEN, width = 8)
        frame3.labelGF5.grid(row = 0, column = 4)

        frame3.labelGF6 = tk.Label(frame3, text="Cost", font=NORMAL_FONT, relief = SUNKEN, width = 10)
        frame3.labelGF6.grid(row = 0, column = 5)

        #Need to create a "Dynamically allocated grid view entry boxes" for next boxes with scroll wheel
###################################################################################


# FRAME4 ########################## TOTAL QUANTITY AND AMOUNT #####################################
        #Third frame inside the current MainPage Window Frame
        frame4 = Frame(self, bg = "blue")
        frame4.pack()#grid(row = 3, column = 0)

        frame4.label1 = tk.Label(frame4, text="Total Quantity", font=NORMAL_FONT)
        frame4.label1.grid(row = 0, column = 0, padx=5, pady=5, sticky = W)

        frame4.label2 = tk.Label(frame4, text="TQ For Now", font=NORMAL_FONT, relief = SUNKEN, width = 16)  #NEED TO GET SUM OF TOTAL QUANTITY
        frame4.label2.grid(row = 0, column = 1)

        frame4.label3 = tk.Label(frame4, text="Total Amount", font=NORMAL_FONT)
        frame4.label3.grid(row = 0, column = 3, padx=5, pady=5, sticky = W)

        frame4.label4 = tk.Label(frame4, text="TA For Now", font=NORMAL_FONT, relief = SUNKEN, width = 16)  #NEED TO GET SUM OF TOTAL COST
        frame4.label4.grid(row = 0, column = 4)
#############################################################################################


# FRAME5 ########################## BAR CODE AND ADD ITEM #####################################

#############################################################################################


# FRAME6 ########################## PROCESS AND REFRESH #####################################

#############################################################################################





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

        button1 = ttk.Button(self, text = "OK", command=MasterFilePopUp) #One can also do command=quit to quit out of the program
        button1.pack(pady=5, padx=10)




def MasterFilePopUp():
    popup = tk.Tk()

    popup.wm_title("FONZY")
    label = ttk.Label(popup, text = "Please specify the product master file", font = NORMAL_FONT)
    label.pack(side = "top", fill = "x", pady = 10)

    button1 = ttk.Button(popup, text = "Okay", command = fileExplorer)
    button1.pack()

    if errorCode == 0:
        return 1
    else:
        popupmsg("Please input the correct Master File")
        MasterFilePopUp()




#once button is clicked, it prompts user to find file then it outputs the contents of the file
def fileExplorer():
    #intializes another instance of tkinter
    try:    
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XLS files","*.xls"),("XLSX files","*.xlsx")))
        
        if re.match("[A-Za-z0-9]",filename):
            #sheet = pe.get_sheet(file_name=filename) #puts data into readable sheet, array is more useful
            sheet = pe.get_array(file_name=filename) #puts data into array

            masterList = sheet
            print(sheet)
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

    popup.wm_title("FONZY")
    label = ttk.Label(popup, text = msg, font = NORMAL_FONT)
    label.pack(side = "top", fill = "x", pady = 10)

    button1 = ttk.Button(popup, text = "Okay", command = popup.destroy)
    button1.pack()
    popup.mainloop()


################################ START OF PROGRAM #########################################

#finds Master File first
MasterFilePopUp()


#runs tkinter program
app = POS()
app.geometry("700x700") #makes app into a 1280x720p screen, can change size to liking
app.mainloop()