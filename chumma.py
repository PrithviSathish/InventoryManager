from tkinter import *


def NewProject():
    print("A new project would be created")


def New():
    print("A new command is initialized")


def Save():
    print("Your program is saved")


def SaveAs():
    print("Where do you want to save the program?")


def Exit():
    print("You have exited")


def Redo():
    print("Your change has been redone")


def Image():
    print("Image has been inserted")


def Print():
    print("Text would be printed")


root = Tk()

# ***** Main Menu *****

menu = Menu(root)
root.config(menu=menu)

fileMenu = Menu(menu)
menu.add_cascade(label="file", menu=fileMenu)

fileMenu.add_command(label="New Project...", command=NewProject)
fileMenu.add_command(label="New...", command=New)

fileMenu.add_separator()

fileMenu.add_command(label="Save...", command=Save)
fileMenu.add_command(label="Save As...", command=SaveAs)

fileMenu.add_separator()

fileMenu.add_command(label="Exit", command=Exit)

editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=Redo)

# ***** Toolbar *****
toolbar = Frame(root, bg="gray")

insertButton = Button(toolbar, text="Insert Image", command=Image)
insertButton.pack(side=LEFT, padx=2, pady=2)
PrintButton = Button(toolbar, text="Print", command=Print)
PrintButton.pack(side=LEFT, padx=2, pady=2)

toolbar.pack(side=TOP, fill=X)

# ***** StatusBar *****
status = Label(root, text="Preparing...", bd=1, anchor=W, relief=SUNKEN)
status.pack(side=BOTTOM, fill=X)

root.mainloop()