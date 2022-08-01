from tkinter import *

master = Tk()
elemento = StringVar()
listbox = Listbox(master)

for item in ["Argentina", "Brasil", "Colombia", "Ecuador", "Bolivia", "Paraguay", "Peru"]:
    listbox.insert(END, item)
    listbox.pack()


label = Label(text="Paises sudamericanos")
label.pack()
master.mainloop()
