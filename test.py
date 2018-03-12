import win32com.client
import time

filePath = r"C:\Users\hedce\OneDrive\Desktop\POS\qwem,date=12-03-2018,time=14;27.docx"
msword = win32com.client.Dispatch("Word.Application") 
msword.Documents.Open(filePath)
msword.visible= True
msword.ActiveDocument.PrintOut()
time.sleep(4)
msword.Documents.Close()
msword.Quit()



"""
from win32com import client
from tkinter import *
import time
import os

def printWordDocument(filename,NumPage1):
    word = client.Dispatch("Word.Application")

    path=str(os.path.realpath(__file__))
    path = path[:-16]
    filename=path+filename

    word.Documents.Open(filename)
    word.ActiveDocument.PrintOut(Copies=2,Collate=True)
    root.focus()
    time.sleep(10)
    word.ActiveDocument.Close()

    word.Quit()

root=Tk()
root.attributes("-fullscreen",True)
Button(root,text='Print',command=lambda:printWordDocument('PrintThis.docx',2)).pack()

root.mainloop()
"""