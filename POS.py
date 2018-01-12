#NEED TO PIP INSTALL PYEXCEL
#NEED TO PIP INSTALL PYEXCEL-XLS

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
customerList = []#[36218745, 'KER ELIX ULTI CH FINS 100ML US V315', 350, 0, 3474636218745, 1], [36382682, 'NUT BAIN SATIN 2 250ML', 400, 0, 3474636382682, 1], [36397983, 'RES THERAPISTE MASQ 200ML', 550, 0, 3474636397983, 1], [36398850, 'REF CHROMACAPTIVE MASQ 200ML', 550, 0, 3474636398850, 2], [36382668, 'NUT OLEO RELAX MASQ 200ML', 550, 0, 3474636382668, 1], [36397952, 'RES FORCE ARCH MASQ 200ML', 550, 0, 3474636397952, 2], [30458222, 'REF FONDANT CHROMACAPTIVE 1000ML', 800, 0, 3474630458222, 2], [30458062, 'REF CHROMACAPTIVE MASQ 500ML', 950, 0, 3474630458062, 1], [36356003, 'DENSIFIQUE FEMME 30X6ML', 1500, 0, 3474636356003, 3], [30525658, 'SE PRO KERATIN REFILL SHMP 250ML        ', 55, 0, 3474630525658, 2], [26404810, 'HAIR SPA OIL 100ML                      ', 70, 0, 8901526404810, 1], [30641044, 'SE ABS REPAIR LIPIDIUM THER CRM 125ML   ', 85, 0, 3474630641044, 1], [30525870, 'SE PRO KERATIN REFILL COND 150ML        ', 85, 0, 3474630525870, 1], [30640702, 'SE ABS REPAIR LIPIDIUM MASQ 200ML       ', 90, 0, 3474630640702, 2], [30640504, 'SE ABS REPAIR LIPIDIUM SHMP 250ML       ', 90, 0, 3474630640504, 1], [30714946, 'SE VITAMINO COLOR AOX SULFAT FREE 150ML ', 110, 0, 3474630714946, 4], [36202430, 'SE VITAMINO COLOR AOX FRESH MASQ 150ML  ', 115, 0, 3474636202430, 2], [30632196, 'TNA PLAYBALL DEVIATION PASTE 100ML      ', 125, 0, 3474630632196, 1], [36501960, 'MYTHIC OIL HUILE ORIGINAL 100ML         ', 150, 0, 3474636501960, 1], [30643659, 'SERIOXYL THICKER HAIR 90ML              ', 170, 0, 3474630643659, 1], [30633629, 'MYTHIC OIL SERUM DE FORCE 50ML          ', 180, 0, 3474630633629, 2], [36494859, 'REF CHROMACAPTIVE MASQ CX FINS 200ML', 550, 0, 3474636494859, 1], [18251615, 'HAIR SPA NOURISHING MASQ 1000ML         ', 350, 0, 6955818251615, 2], [86130594, 'FIBERSTRONG BRILT MASQ 150ML            ', 90, 0, 884486130594, 1]]
errorCode = 0
container = 0
"""
Error Code Legend:
0 = No error
1 = Master File Error
"""



class POS(tk.Tk):
    #initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)   #initializes tk module

        #tk.Tk.iconbitmap(self, default="<image-file-name.ico>") #gives an icon for the program, top left corner, has to be an ICON
        tk.Tk.wm_title(self, "FONZY")   #Gives name to program client application
        
        global container
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

        for F in (ErrorPage, MainPage): #Adds frames onto list, to add more frames, just add it to the list
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
        
        #Second frame inside the current MainPage Window Frame
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

        frame3 = Frame(self, bg = "white", width = 690, height = 400, borderwidth = 1)
        frame3.pack(expand = True, fill = Y)

        #Creates a canvas-frame scrollable widget
        frame3Canvas = tk.Canvas(frame3, width = 690, height = 400, borderwidth = 0, bg="white")
        frame3Frame = tk.Frame(frame3Canvas, bg = "white")
        frame3ScrollBar = tk.Scrollbar(frame3, orient = "vertical", command = frame3Canvas.yview)
        frame3Canvas.configure(yscrollcommand = frame3ScrollBar.set)

        frame3ScrollBar.pack(side = "right", fill = "y")
        frame3Canvas.pack(side = "left", fill = "both", expand = True)
        frame3Canvas.create_window((4,4), window = frame3Frame, anchor = "nw")

        frame3Frame.bind("<Configure>", lambda event, canvas = frame3Canvas: frame3Canvas.configure(scrollregion = frame3Canvas.bbox("all")))


        #THIS CREATES THE GRID TO OUTPUT THE DATA QUERIED FROM THE MASTER FILE
        #Description of Box: 'X' amount goind down, i.e. number of items, 6 descriptive columns: Bar Code, Product Description, Amount, Quantity, Additional Discount, Total Amount
        #This is the header GRID VIEW Labels
        frame3Label1 = tk.Label(frame3Frame, text = "Bar Code", font = NORMAL_FONT, relief = SUNKEN, width = 15)
        frame3Label1.grid(row = 0, column = 0)

        frame3Label2 = tk.Label(frame3Frame, text = "Product Description", font = NORMAL_FONT, relief = SUNKEN, width = 30)
        frame3Label2.grid(row = 0, column = 1)

        frame3Label3 = tk.Label(frame3Frame, text = "Price", font = NORMAL_FONT, relief = SUNKEN, width = 9)
        frame3Label3.grid(row = 0, column = 2)

        frame3Label4 = tk.Label(frame3Frame, text = "Quantity", font = NORMAL_FONT, relief = SUNKEN, width = 8)
        frame3Label4.grid(row = 0, column = 3)

        frame3Label5 = tk.Label(frame3Frame, text = "Discount", font = NORMAL_FONT, relief = SUNKEN, width = 8)
        frame3Label5.grid(row = 0, column = 4)

        frame3Label6 = tk.Label(frame3Frame, text = "Cost", font = NORMAL_FONT, relief = SUNKEN, width = 10)
        frame3Label6.grid(row = 0, column = 5)

        
        #Need to create a "Dynamically allocated grid view entry boxes" for next boxes with scroll wheel
        rowNum = 1
        totalCost = 0
        totalQuantity = 0
        for i in range(len(customerList)):

            barCodeString = str(customerList[i][4])
            frame3BarCode = tk.Label(frame3Frame, text = barCodeString, font = NORMAL_FONT, relief = SUNKEN, width = 15)
            frame3BarCode.grid(row = rowNum, column = 0)

            prodDesc = customerList[i][1]
            frame3ProdDesc = tk.Label(frame3Frame, text = prodDesc, font = NORMAL_FONT, relief = SUNKEN, width = 30)
            frame3ProdDesc.grid(row = rowNum, column = 1)

            frame3Price = tk.Label(frame3Frame, text = "{:,}".format(customerList[i][2]), font = NORMAL_FONT, relief = SUNKEN, width = 9)
            frame3Price.grid(row = rowNum, column = 2)

            totalQuantity += customerList[i][5]
            frame3Quantity = ttk.Label(frame3Frame, text = "{:,}".format(customerList[i][5]), font = NORMAL_FONT, relief = SUNKEN, width = 8)   #creates an entry box and allows the entry of a string variable
            frame3Quantity.grid(row = rowNum, column = 3)

            discountString = str(customerList[i][3])
            frame3Discount = tk.Label(frame3Frame, text = discountString+"%", font = NORMAL_FONT, relief = SUNKEN, width = 8)
            frame3Discount.grid(row = rowNum, column = 4)

            cost = (customerList[i][5]*customerList[i][2])-((customerList[i][3]/100)*(customerList[i][5]*customerList[i][2]))   #gets cost estimate with given mathematical values
            totalCost += cost
            frame3Cost = tk.Label(frame3Frame, text = "{:,}".format(cost), font = NORMAL_FONT, relief = SUNKEN, width = 10)
            frame3Cost.grid(row = rowNum, column = 5)

            rowNum += 1        
#--------------------------------------------------------------------------------------#


# FRAME4 -------------------------- TOTAL QUANTITY AND AMOUNT ------------------------------------#
        #Fourth frame inside the current MainPage Window Frame
        frame4 = Frame(self, bg = "blue")
        frame4.pack(fill = BOTH)

        frame4Label1 = tk.Label(frame4, text="Total Quantity", font = NORMAL_FONT)
        frame4Label1.grid(row = 0, column = 0, padx = 5, pady = 5)


        frame4Label2 = tk.Label(frame4, text = "{:,}".format(totalQuantity), font = NORMAL_FONT, relief = SUNKEN, width = 16)  #NEED TO GET SUM OF TOTAL QUANTITY
        frame4Label2.grid(row = 0, column = 1)


        #Frame block to separate the first set of labels above from the second set of labels below
        frame4LabelBlock = tk.Label(frame4, width = 16, bg = "blue")
        frame4LabelBlock.grid(row = 0, column = 2, padx = 45, pady = 5)


        frame4Label3 = tk.Label(frame4, text = "Total Cost", font=NORMAL_FONT)
        frame4Label3.grid(row = 0, column = 3, padx = 5, pady = 5)

        frame4Label4 = tk.Label(frame4, text = "{:,}".format(totalCost), font = NORMAL_FONT, relief = SUNKEN, width = 16)  #NEED TO GET SUM OF TOTAL COST
        frame4Label4.grid(row = 0, column = 4)
#-------------------------------------------------------------------------------------------------#


# FRAME5 -------------------------- BAR CODE AND ADD ITEM ------------------------------------#
        #Fifth frame inside the current MainPage Window Frame
        frame5 = Frame(self, bg = "pink")
        frame5.pack(fill = BOTH)

        frame5Label1 = tk.Label(frame5, text = "Product Bar Code", font = NORMAL_FONT)
        frame5Label1.grid(row = 0, column = 0, padx=5, pady=5, sticky = W)

        barCode = tk.StringVar()    #creates the object barCode with a string variable type
        frame5EntryBox = ttk.Entry(frame5, textvariable = barCode, width = 22)   #creates an entry box and allows the entry of a string variable
        frame5EntryBox.grid(row = 0, column = 1, padx = 5, pady = 5)

        frame5Spacer = tk.Label(frame5, text = "", font = NORMAL_FONT, bg = "pink")
        frame5Spacer.grid(row = 0, column = 2, padx=20, pady=5, sticky = W)

        frame5Label2 = tk.Label(frame5, text = "Quantity", font = NORMAL_FONT)
        frame5Label2.grid(row = 0, column = 3, padx=5, pady=5, sticky = W)

        quantity = tk.IntVar()    #creates the object barCode with a string variable type
        quantity.set(1)
        frame5EntryBox2 = ttk.Entry(frame5, textvariable = quantity, width = 8)   #creates an entry box and allows the entry of a string variable
        frame5EntryBox2.grid(row = 0, column = 4, padx = 5, pady = 5)

        frame5Button = ttk.Button(frame5, text = "Add Item", command = lambda: updateCustomerList(barCode, quantity)) #NEED TO CHECK IF BAR CODE WORKS FIRST!!! MAY NEED TO GO SOMEWHERE OTHER THAN MAIN PAGE
        frame5Button.grid(row = 0, column = 5, padx = 90, pady = 10)
#---------------------------------------------------------------------------------------------#


# FRAME6 -------------------------- PROCESS AND REFRESH ------------------------------------#
        #Sixth frame inside the current MainPage Window Frame
        frame6 = Frame(self, bg = "yellow")
        frame6.pack(fill = BOTH)

        frame6Button = ttk.Button(frame6, text = "Refresh", command=refreshMainFrame)
        frame6Button.grid(row = 0, column = 0, padx = 125, pady = 10)

        frame6Button = ttk.Button(frame6, text = "Process", command=ProcessPage)   #DOESN'T WORKS           #STILL NEED TO MAKE PROCESS FRAME
        frame6Button.grid(row = 0, column = 1, padx = 125, pady = 10)
#--------------------------------------------------------------------------------------------#   




#error page for when there is a possible error
class ErrorPage(tk.Frame):          #NEED TO CHANGE THIS INTO A POP UP WINDOW INSTEAD OF A FRAME
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        
        frame = Frame(self, bg = "green")
        frame.pack(fill = BOTH)

        if errorCode == 1:
            label = tk.Label(frame, text="Error! Please input a correct Master File Document", font=SMALL_FONT)
            label.pack(pady=10, padx=10)

        button1 = ttk.Button(frame, text = "OK", command = MasterFilePopUp) #One can also do command=quit to quit out of the program
        button1.pack(pady=5, padx=10)




#process purchase page for when a purchase is to be made
def ProcessPage():
    processPopup = tk.Toplevel()

    #NEED TO FIGURE OUT SIZE
    processPopup.geometry("400x150")

    processPopup.wm_title("FONZY")

    label = ttk.Label(processPopup, text="PAYMENT HERE!", font=SMALL_FONT)
    label.pack(pady=10, padx=10)

    #to get exact time, used for invoicing
    time = datetime.datetime.now() #time.time()
    print(time.time())
    #once button is clicked, it prompts user to find file then it outputs the contents of the file




def fileExplorer():
    #intializes another instance of tkinter
    global masterList   #allows user to add item to masterList global variable
    try:    
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XLS files","*.xls"),("XLSX files","*.xlsx")))
        
        if re.match("[A-Za-z0-9]",filename):
            sheet = pe.get_array(file_name=filename) #puts data into array
            masterList = sheet
            errorCode = 0 #resets errorCode

        else:
            errorCode = 1
    
    except ValueError:
        errorCode = 1




def MasterFilePopUp():
    masterPopup = tk.Toplevel()

    masterPopup.wm_title("FONZY")
    label = ttk.Label(masterPopup, text = "Please specify the product master file", font = NORMAL_FONT)
    label.pack(side = "top", fill = "x", padx = 5)

    button1 = ttk.Button(masterPopup, text = "Okay", command = lambda: fileExplorer() or masterPopup.destroy())
    button1.pack(pady = 10)

    if errorCode == 0:
        return 1
    else:
        popupmsg("Please input the correct Master File")
        MasterFilePopUp()




#Creates popup message bars
def popupmsg(msg):
    popup = tk.Toplevel()

    popup.wm_title("FONZY")
    label = ttk.Label(popup, text = msg, font = NORMAL_FONT)
    label.pack(side = "top", fill = "x", pady = 10)

    button1 = ttk.Button(popup, text = "Okay", command = popup.destroy)
    button1.pack()




def updateCustomerList(barCode, quantity):
    global customerList   #global variable to allow user to update updateCustomerList
    if not barCode.get():   #checks if barCode is empty
        return  
    else:   #finds barCode inside masterList
        #print(masterList)
        for i in range(len(masterList)):    #searches through master list to see if barCode is inside masterList
           
            if int(barCode.get()) == masterList[i][4]:   #if bar code is inside the masterList

                if len(customerList) == 0:   #if customerList is empty
                    customerList.append(masterList[i][:])  #adds a masterList object inside customerList
                    customerList[0].append(quantity.get())   #gives a quantifiable value to number of products the customer wants to purchase
                    
                    if customerList[0][5] <= 0: #deletes element if item quantity value is 0 or less than 0
                        del customerList[0]
                    refreshMainFrame()  #sends back to MainPage Frame

                else:   #if customerList is not empty
                    for j in range(len(customerList)):    #searches through customerList to see if item is already inside; checks for repeats
                        
                        if int(barCode.get()) == customerList[j][4]:   #if is a repeated barCode
                            customerList[j][5] += quantity.get()
                            
                            if customerList[j][5] <= 0: #deletes element if item quantity value is 0 or less than 0
                                del customerList[j]
                            refreshMainFrame()  #sends back to MainPage Frame
                            return

                    #if quantity.get() > 0:    #checks if quantity to be added is at least greater than 0
                        #print("Quantity is more than :" + str(quantity.get()))

                    customerList.append(masterList[i][:])  #adds a masterList object inside customerList
                    customerList[len(customerList)-1].append(quantity.get())   #gives a quantifiable value to number of products the customer wants to purchase
                    
                    if customerList[len(customerList)-1][5] <= 0: #deletes element if item quantity value is 0 or less than 0
                        del customerList[len(customerList)-1]
                    refreshMainFrame()  #sends back to MainPage Frame
                    

                #masterList
                #prints: [20297939, 'AC EDT 75ML SPRAY TEST', 250, 0, 3605520297939]
                #print("BAR CODE: " + barCode.get())
                #print("CUSTOMER LIST CODE: ")
                #print(customerList)
    refreshMainFrame()
    return            




def refreshMainFrame():
    global app
    app.frames[MainPage].destroy()
    app.frames[MainPage] = MainPage(container, app)
    app.frames[MainPage].grid(row=0, column = 0, sticky = "nsew")
    app.frames[MainPage].tkraise()





#-------------------------------- START OF PROGRAM ----------------------------------------#

#runs tkinter program
app = POS()
#"width x height"
app.geometry("700x700") #makes app into a 700x700p screen, can change size to liking
app.resizable(False, False) #window isn't resizable. Makes it easier for the owner to manage

#finds Master File first
# run after `POS` will be created and `app.mainloop()` will start
app.after(100, MasterFilePopUp)
app.mainloop()