import tkinter as tk
from tkinter import ttk
import pyexcel as pe
import datetime
import time

from tkinter import filedialog
from tkinter import *

LARGE_FONT = ("Verdana", 12)
NORMAL_FONT = ("Verdana", 10)
SMALL_FONT = ("Verdana", 8)

#GLOBAL VARIABLES
masterList = [] #list of objects from Master File
customerList = [[20297939, 'AC EDT 75ML SPRAY TEST', 250, 0, 3605520297939],[20297123, 'AC EDC 75ML SPRAY TEST', 550, 10, 3605520217939]]   #list for customer pruchases taken from Master File
errorCode = 0

"""
Error Code Legend:
0 = No error
1 = Master File Error
"""

"""
#time = datetime.datetime.now() #time.time()
"""


class POS(tk.Tk):
    #initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   #initializes tk module

        #tk.Tk.iconbitmap(self, default="<image-file-name.ico>") #gives an icon for the program, top left corner, has to be an ICON
        tk.Tk.wm_title(self, "FONZY")   #Gives name to program client application

        container = tk.Frame(self)
        container.pack(side = "top", fill = "both", expand = True)  #"packs" or pushes the container to the top

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

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

        self.frames = {}    #creates an object to hold multiple frames i.e. more windows/tabs

        for F in (MainPage, ErrorPage, PaymentPage): #Adds frames onto list, to add more frames, just add it to the list
            frame = F(container, self)
            self.frames[F] = frame  #adds frame into frames object
            frame.grid(row=0, column = 0, sticky = "nsew")  #sets frame structure, nsew = north south east west
        
        self.show_frame(MainPage)

    #shows the frame when called
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() 




#MAIN FRAME THAT THE USER WILL BE ON! Showcases customer information and purchase details
class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)

# FRAME1 ------------------ CUSTOMER NAME, TELEPHONE NUMBER ----------------------#

        #First frame inside the current MainPage Window Frame
        frame1 = Frame(self, bg = "green")
        frame1.pack(fill = BOTH)
        
#CUSTOMER NAME
        frame1Label = tk.Label(frame1, text = "Customer Name", font = SMALL_FONT)
        frame1Label.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = W)

        customerName = StringVar()    #creates the object customerName with a string variable type
        frame1EntryBox1 = ttk.Entry(frame1, textvariable = customerName, width = 40)   #creates an entry box and allows the entry of a string variable
        frame1EntryBox1.grid(row = 0, column = 1, padx = 5, pady = 5, sticky = W)
        #print(customerName.get())

#PHONE
        frame1Label2 = tk.Label(frame1, text="Phone", font=SMALL_FONT)
        frame1Label2.grid(row = 0, column = 2, padx = 5, pady = 5, sticky = W)
        
        phone = StringVar()    #creates the object phone with a string variable type
        frame1EntryBox2 = ttk.Entry(frame1, textvariable = phone, width = 40)   #creates an entry box and allows the entry of a string variable
        frame1EntryBox2.grid(row = 0, column = 3, padx = 5, pady = 5, sticky = W)
#-----------------------------------------------------------------------------#


# FRAME2 -------------------------- ADDRESS ------------------------------------#
        
        #Secibd frame inside the current MainPage Window Frame
        frame2 = Frame(self, bg = "red")
        frame2.pack(fill = BOTH)

#ADDRESS
        frame2.label = tk.Label(frame2, text="Address", font=SMALL_FONT)
        frame2.label.grid(row = 1, column = 0, padx=5, pady=5, sticky = W)

        address = StringVar()    #creates the object address with a string variable type
        frame2EntryBox = ttk.Entry(frame2, textvariable = address, width = 99)   #creates an entry box and allows the entry of a string variable
        frame2EntryBox.grid(row = 1, column = 1, padx = 5, pady = 5, sticky = W)
#-----------------------------------------------------------------------------------#


# FRAME3 -------------------------- ENTRY BOX GRID ------------------------------------#
        #Third frame inside the current MainPage Window Frame
        frame3 = Frame(self, bg = "grey", width = 690, height = 400, borderwidth = 1)
        frame3.pack(expand = True, fill=BOTH)
            
        frame3ListBox = Listbox(frame3, width = 690, height = 400, borderwidth = 1, bg = "white")
        frame3ListBox.config(state = DISABLED)
        frame3ListBox.pack(expand = True, fill = BOTH)

        #Scrollbar: Still need to fix
        #frame3ScrollBar = Scrollbar(frame3ListBox)
        #frame3ScrollBar.grid(column = 6)
        #frame3ListBox['yscrollcommand'] = frame3ScrollBar.set  #STILL NEED TO CHECK AND VERIFY!!!
        ##frame3ScrollBar.config(yscrollcommand=frame3ScrollBar.set)
        ##frame3ScrollBar.config(command=frame3ListBox.yview)


        #THIS CREATES THE GRID TO OUTPUT THE DATA QUERIED FROM THE MASTER FILE
        #Description of Box: 'X' amount goind down, i.e. number of items, 6 descriptive columns: Bar Code, Product Description, Amount, Quantity, Additional Discount, Total Amount
        #This is the header GRID VIEW Labels
        frame3Label1 = tk.Label(frame3ListBox, text = "Bar Code", font = NORMAL_FONT, relief = SUNKEN, width = 15)
        frame3Label1.grid(row = 0, column = 0)

        frame3Label2 = tk.Label(frame3ListBox, text = "Product Description", font = NORMAL_FONT, relief = SUNKEN, width = 30)
        frame3Label2.grid(row = 0, column = 1)

        frame3Label3 = tk.Label(frame3ListBox, text = "Price", font = NORMAL_FONT, relief = SUNKEN, width = 9)
        frame3Label3.grid(row = 0, column = 2)

        frame3Label4 = tk.Label(frame3ListBox, text = "Quantity", font = NORMAL_FONT, relief = SUNKEN, width = 8)
        frame3Label4.grid(row = 0, column = 3)

        frame3Label5 = tk.Label(frame3ListBox, text = "Discount", font = NORMAL_FONT, relief = SUNKEN, width = 8)
        frame3Label5.grid(row = 0, column = 4)

        frame3Label6 = tk.Label(frame3ListBox, text = "Cost", font = NORMAL_FONT, relief = SUNKEN, width = 10)
        frame3Label6.grid(row = 0, column = 5)

        
        #Need to create a "Dynamically allocated grid view entry boxes" for next boxes with scroll wheel
        rowNum = 1
        for i in range(len(customerList)):

            barCodeString = str(customerList[i][0])
            frame3BarCode = tk.Label(frame3ListBox, text = barCodeString, font = NORMAL_FONT, relief = SUNKEN, width = 15)
            frame3BarCode.grid(row = rowNum, column = 0)

            prodDesc = customerList[i][1]
            frame3ProdDesc = tk.Label(frame3ListBox, text = prodDesc, font = NORMAL_FONT, relief = SUNKEN, width = 30)
            frame3ProdDesc.grid(row = rowNum, column = 1)

            priceString = str(customerList[i][2])
            frame3Price = tk.Label(frame3ListBox, text = priceString, font = NORMAL_FONT, relief = SUNKEN, width = 9)
            frame3Price.grid(row = rowNum, column = 2)

            quantity = IntVar()
            quantity.set(1)
            frame3Quantity = ttk.Entry(frame3ListBox, textvariable = quantity.get(), font = NORMAL_FONT, width = 8)   #creates an entry box and allows the entry of a string variable
            frame3Quantity.grid(row = rowNum, column = 3)

            discountString = str(customerList[i][3])
            frame3Discount = tk.Label(frame3ListBox, text = discountString, font = NORMAL_FONT, relief = SUNKEN, width = 8)
            frame3Discount.grid(row = rowNum, column = 4)

            cost = (quantity.get()*customerList[i][2])-((customerList[i][3]/100)*(quantity.get()*customerList[i][2]))
            costString = str(cost)
            frame3Cost = ttk.Label(frame3ListBox, text = costString, font = NORMAL_FONT, relief = SUNKEN, width = 10)
            frame3Cost.grid(row = rowNum, column = 5)

            rowNum += 1

            #frame3EANCode = tk.Label(frame3ListBox, text = customerList[i][4], font = NORMAL_FONT, relief = SUNKEN, width = 15)
            #frame3EANCode = grid(row = row, column = 4)
        
#--------------------------------------------------------------------------------------#


# FRAME4 -------------------------- TOTAL QUANTITY AND AMOUNT ------------------------------------#
        #Fourth frame inside the current MainPage Window Frame
        frame4 = Frame(self, bg = "blue")
        frame4.pack(fill = BOTH)

        frame4Label1 = tk.Label(frame4, text="Total Quantity", font = NORMAL_FONT)
        frame4Label1.grid(row = 0, column = 0, padx = 5, pady = 5)

        frame4Label2 = tk.Label(frame4, text = "TQ For Now", font = NORMAL_FONT, relief = SUNKEN, width = 16)  #NEED TO GET SUM OF TOTAL QUANTITY
        frame4Label2.grid(row = 0, column = 1)

        #Frame block to separate the first set of labels above from the second set of labels below
        frame4LabelBlock = tk.Label(frame4, width = 16, bg = "blue")
        frame4LabelBlock.grid(row = 0, column = 2, padx = 45, pady = 5)

        frame4Label3 = tk.Label(frame4, text="Total Amount", font=NORMAL_FONT)
        frame4Label3.grid(row = 0, column = 3, padx = 5, pady = 5)

        frame4Label4 = tk.Label(frame4, text="TA For Now", font = NORMAL_FONT, relief = SUNKEN, width = 16)  #NEED TO GET SUM OF TOTAL COST
        frame4Label4.grid(row = 0, column = 4)
#-------------------------------------------------------------------------------------------------#


# FRAME5 -------------------------- BAR CODE AND ADD ITEM ------------------------------------#
        #Fifth frame inside the current MainPage Window Frame
        frame5 = Frame(self, bg = "pink")
        frame5.pack(fill = BOTH)

        frame5Label1 = tk.Label(frame5, text = "Product Bar Code", font = NORMAL_FONT)
        frame5Label1.grid(row = 0, column = 0, padx=5, pady=5, sticky = W)

        barCode = tk.StringVar()    #creates the object barCode with a string variable type
        frame5EntryBox = ttk.Entry(frame5, textvariable = barCode, width = 40)   #creates an entry box and allows the entry of a string variable
        frame5EntryBox.grid(row = 0, column = 1, padx = 5, pady = 5)

        frame5Button = ttk.Button(frame5, text = "Add Item", command = lambda: updateCustomerList(barCode)) #NEED TO CHECK IF BAR CODE WORKS FIRST!!! MAY NEED TO GO SOMEWHERE OTHER THAN MAIN PAGE
        frame5Button.grid(row = 0, column = 2, padx = 130, pady = 10)
#---------------------------------------------------------------------------------------------#


# FRAME6 -------------------------- PROCESS AND REFRESH ------------------------------------#
        #Sixth frame inside the current MainPage Window Frame
        frame6 = Frame(self, bg = "yellow")
        frame6.pack(fill = BOTH)

        frame6Button = ttk.Button(frame6, text = "Refresh", command=MainPage)   #DOESN'T WORK
        frame6Button.grid(row = 0, column = 0, padx = 125, pady = 10)

        frame6Button = ttk.Button(frame6, text = "Process", command=MainPage)   #DOESN'T WORKS           #STILL NEED TO MAKE PROCESS FRAME
        frame6Button.grid(row = 0, column = 1, padx = 125, pady = 10)
#--------------------------------------------------------------------------------------------#   




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

        button1 = ttk.Button(self, text = "OK", command = MasterFilePopUp) #One can also do command=quit to quit out of the program
        button1.pack(pady=5, padx=10)




#once button is clicked, it prompts user to find file then it outputs the contents of the file
def fileExplorer():
    #intializes another instance of tkinter
    global masterList   #allows user to add item to masterList global variable
    try:    
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XLS files","*.xls"),("XLSX files","*.xlsx")))
        
        if re.match("[A-Za-z0-9]",filename):
            #sheet = pe.get_sheet(file_name=filename) #puts data into readable sheet, array is more useful
            sheet = pe.get_array(file_name=filename) #puts data into array
            masterList = sheet
            #print(sheet)   #prints: everything
            #print(sheet[4]) #prints: [20297939, 'AC EDT 75ML SPRAY TEST', 250, 0, 3605520297939]
            #print(type(sheet[4][0]))
            #print(sheet[4][0]) #prints: 20297939
            #print(len(masterList))
            

            errorCode = 0 #resets errorCode
            return

        else:
            errorCode = 1
            return
    
    except ValueError:
        errorCode = 1
        return




def MasterFilePopUp():
    popup = tk.Toplevel() # <-- Toplevel instead of Tk

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




#Creates popup message bars
def popupmsg(msg):
    popup = tk.Toplevel() # <-- Toplevel instead of Tk

    popup.wm_title("FONZY")
    label = ttk.Label(popup, text = msg, font = NORMAL_FONT)
    label.pack(side = "top", fill = "x", pady = 10)

    button1 = ttk.Button(popup, text = "Okay", command = popup.destroy)
    button1.pack()




def updateCustomerList(barCode):
    global updateCustomerList   #global variable to allow user to update updateCustomerList
    
    if not barCode.get():   #checks if barCode is empty
        return  
    else:   #finds barCode inside masterList
        for i in range(len(masterList)):
            if int(barCode.get()) == masterList[i][0]:
                customerList.append(masterList[i])
        
                #print("BAR CODE: " + barCode.get())
                #print("CUSTOMER LIST CODE: ")
                print(customerList)
    return            


#masterList
#prints: [20297939, 'AC EDT 75ML SPRAY TEST', 250, 0, 3605520297939]







#-------------------------------- START OF PROGRAM ----------------------------------------#

#runs tkinter program
app = POS()

app.geometry("700x700") #makes app into a 700x700p screen, can change size to liking
app.resizable(False, False) #window isn't resizable. Makes it easier for the owner to manage

#finds Master File first
# run after `POS` will be created and `app.mainloop()` will start
app.after(100, MasterFilePopUp)
app.mainloop()