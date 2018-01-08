import tkinter as tk

# --- functions ---

def check():
    print('len:', len(var.get()))

# --- main ---

root = tk.Tk()

var = tk.StringVar()

ent = tk.Entry(root, textvariable=var)
ent.pack()

but = tk.Button(root, text="Check", command=check)
but.pack()

root.mainloop()