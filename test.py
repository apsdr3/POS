## TEST FILE ##
import pyexcel as pe
from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg")))
print(root.filename)
#sheet = pe.get_sheet(file_name=root.filename)
#print(sheet)