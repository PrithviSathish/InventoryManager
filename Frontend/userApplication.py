import tkinter as tk
from tkinter import *
from tkinter import messagebox


class UserUI:

    def __init__(self, name):
        self.root = tk.Tk()
        self.name = name
        self.root.geometry = "600x600"
        self.root.configure(bg="white")
        self.root.title("Inventory Manager")

    def home(self, name):
        title = Label(self.root, text=f"WELCOME, {name}", pady=20, font=("Arial Bold", 25))
        title.place(x=300, y=25, anchor="center")
