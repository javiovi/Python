from tkinter import *

def seleccionar():
    monitor.config(text="{}".format(opcion.get()))
def reset():
    opcion.set(None)
    monitor.config(text="")

root = Tk()
opcion = StringVar()
opcion.set(None)
Radiobutton(root, text="OP 1", variable=opcion,
            value='Opcion 1', command=seleccionar).pack()
Radiobutton(root, text="OP 2", variable=opcion,
            value='Opcion 2', command=seleccionar).pack()
Radiobutton(root, text="OP 3", variable=opcion,
            value='Opcion 3', command=seleccionar).pack()
Radiobutton(root, text="OP 4", variable=opcion,
            value='Opcion 4', command=seleccionar).pack()

monitor = Label(root)
monitor.pack()
Button(root, text="Reiniciar", command=reset).pack()

root.mainloop()