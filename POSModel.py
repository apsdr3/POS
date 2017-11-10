import re
import tkinter as tk
import pyexcel as pe


from tkinter import filedialog
from tkinter import *

#class POSsheet():
	


#once button is clicked, it prompts user to find file then it outputs the contents of the file
def fileExplorer():
    #intializes another instance of tkinter
    try:	
        filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("XLS files","*.xls"),("XLSX files","*.xlsx")))
        
        if re.match("[A-Za-z0-9]",filename):
        	sheet = pe.get_sheet(file_name=filename)

        	return

        else:
        	print("Error") #need to make error frame
    
    except ValueError:
        print("Error2") #need to make error frame
        return
    
    return

