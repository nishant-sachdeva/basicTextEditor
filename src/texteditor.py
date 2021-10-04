import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import *

filename = "Untitled"

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)

def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())

    except:
        tk.messagebox.showerror(title="Oops!", message="Unable to save this file ...")

def openFile():
    f = askopenfile(mode='r')

    global filename
    filename = f.name

    t = f.read()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("My python text editor")
root.minsize(width=600, height=600)
root.maxsize(width=600, height=600)

text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="SaveAs", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Close", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
