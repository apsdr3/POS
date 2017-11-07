import tkinter as tk

LARGE_FONT=("Verdana", 12)

class POS(tk.Tk):
	#initializes on startup
    def __init__(self,*args,**kwargs):
        tk.Tk.__init__(self, *args, **kwargs)	#initializes tk module
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)	#"packs" or pushes the container to the top

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}	#creates an object to hold multiple frames i.e. more windows/tabs

        frame = StartPage(container, self)
        self.frames[StartPage] = frame	#adds frame into frames object
        frame.grid(row=0, column = 0, sticky="nsew")	#sets frame structure, nsew = north south east west
        self.show_frame(StartPage)

    #shows the frame when called
    def show_frame(self,cont):
        frame = self.frames[cont]
        frame.tkraise() 

#Start Page frame
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)


#runs program
app = POS()
app.mainloop()