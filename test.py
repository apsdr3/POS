from tkinter import *

customerList = [[36218745, 'KER ELIX ULTI CH FINS 100ML US V315', 350, 0, 3474636218745, 1], [36382682, 'NUT BAIN SATIN 2 250ML', 400, 0, 3474636382682, 1], [36397983, 'RES THERAPISTE MASQ 200ML', 550, 0, 3474636397983, 1], [36398850, 'REF CHROMACAPTIVE MASQ 200ML', 550, 0, 3474636398850, 2], [36382668, 'NUT OLEO RELAX MASQ 200ML', 550, 0, 3474636382668, 1], [36397952, 'RES FORCE ARCH MASQ 200ML', 550, 0, 3474636397952, 2], [30458222, 'REF FONDANT CHROMACAPTIVE 1000ML', 800, 0, 3474630458222, 2], [30458062, 'REF CHROMACAPTIVE MASQ 500ML', 950, 0, 3474630458062, 1], [36356003, 'DENSIFIQUE FEMME 30X6ML', 1500, 0, 3474636356003, 3], [30525658, 'SE PRO KERATIN REFILL SHMP 250ML        ', 55, 0, 3474630525658, 2], [26404810, 'HAIR SPA OIL 100ML                      ', 70, 0, 8901526404810, 1], [30641044, 'SE ABS REPAIR LIPIDIUM THER CRM 125ML   ', 85, 0, 3474630641044, 1], [30525870, 'SE PRO KERATIN REFILL COND 150ML        ', 85, 0, 3474630525870, 1], [30640702, 'SE ABS REPAIR LIPIDIUM MASQ 200ML       ', 90, 0, 3474630640702, 2], [30640504, 'SE ABS REPAIR LIPIDIUM SHMP 250ML       ', 90, 0, 3474630640504, 1], [30714946, 'SE VITAMINO COLOR AOX SULFAT FREE 150ML ', 110, 0, 3474630714946, 4], [36202430, 'SE VITAMINO COLOR AOX FRESH MASQ 150ML  ', 115, 0, 3474636202430, 2], [30632196, 'TNA PLAYBALL DEVIATION PASTE 100ML      ', 125, 0, 3474630632196, 1], [36501960, 'MYTHIC OIL HUILE ORIGINAL 100ML         ', 150, 0, 3474636501960, 1], [30643659, 'SERIOXYL THICKER HAIR 90ML              ', 170, 0, 3474630643659, 1], [30633629, 'MYTHIC OIL SERUM DE FORCE 50ML          ', 180, 0, 3474630633629, 2], [36494859, 'REF CHROMACAPTIVE MASQ CX FINS 200ML', 550, 0, 3474636494859, 1], [18251615, 'HAIR SPA NOURISHING MASQ 1000ML         ', 350, 0, 6955818251615, 2], [86130594, 'FIBERSTRONG BRILT MASQ 150ML            ', 90, 0, 884486130594, 1]]

root = Tk()

frame = Frame(root)
frame.pack()

frame3 = Frame(frame, bg = "white", width = 690, height = 400, borderwidth = 1)
frame3.pack(expand = True, fill = Y)

frame3Canvas = Canvas(frame3, width = 690, height = 400, bg = "white")
frame3Frame = Frame(frame3Canvas, bg = "white", width = 690, height = 400, borderwidth = 1)
frame3ScrollBar = Scrollbar(frame3, orient = "vertical", command = frame3Canvas.yview)
frame3Canvas.configure(yscrollcommand=frame3ScrollBar.set)

frame3ScrollBar.pack(side = RIGHT, fill = Y)

frame3Canvas.create_window((690,400), window=frame3Frame, anchor="nw", tags="frame3Frame")

frame3.bind("<Configure>", frame3Canvas.configure(scrollregion=frame3Canvas.bbox("all")))

frame3Frame.pack(expand = True, fill = Y)
frame3Canvas.pack(side = LEFT, fill = Y)



frame3Label1 = Label(frame3Frame, text = "Bar Code", relief = "ridge", width = 15)
frame3Label1.grid(row = 0, column = 0)

frame3Label2 = Label(frame3Frame, text = "Product Description", relief = "ridge", width = 30)
frame3Label2.grid(row = 0, column = 1)

rowNum = 1
totalCost = 0
totalQuantity = 0
for i in range(len(customerList)):

    barCodeString = str(customerList[i][4])
    frame3BarCode = Label(frame3Frame, text = barCodeString, relief = "ridge", width = 15)
    frame3BarCode.grid(row = rowNum, column = 0)

    prodDesc = customerList[i][1]
    frame3ProdDesc = Label(frame3Frame, text = prodDesc, relief = "ridge", width = 30)
    frame3ProdDesc.grid(row = rowNum, column = 1)

    rowNum += 1


root.geometry("690x200")
root.resizable(False, False)
mainloop()