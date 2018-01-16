import tkinter as tk
from tkinter import ttk
import datetime

def programStart():
    startPopup = tk.Toplevel()

    label = ttk.Label(startPopup, text = "Cashier Name: ")
    label.grid(row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)

    cashierString = tk.StringVar()
    cashierEntryBox = ttk.Entry(startPopup, textvariable = cashierString, width = 25)
    cashierEntryBox.grid(row = 0, column = 1, padx = 5, pady = 5)

    label2 = ttk.Label(startPopup, text = "Event Name:  ")
    label2.grid(row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)

    eventString = tk.StringVar()
    eventEntryBox = ttk.Entry(startPopup, textvariable = eventString, width = 25)
    eventEntryBox.grid(row = 1, column = 1, padx = 5, pady = 5)

    print(cashierString.get())
    print(eventString.get())
    excelString = cashierString.get() + "." + eventString.get() + "." + str(datetime.datetime.today().strftime('%d/%m/%Y'))
    print(excelString)

    button1 = ttk.Button(startPopup, text = "Okay", command = lambda: startPopup.destroy())
    button1.grid(row = 2, padx = 5, pady = 5, sticky = "nsew")


app = tk.Frame()
app.after(100, programStart)
app.mainloop()