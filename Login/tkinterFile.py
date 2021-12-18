import tkinter
from tkinter import *
from tkinter import messagebox


# Class for the GUI window 
class GuiWindow:

    def __init__(self):
        self.root = tkinter.Tk()
        self.name = ""
        self.root.geometry("600x500")
        self.root.configure(bg="light sky blue")
        self.sign_in = False
        self.sign_page = False

        # Create the dictionary
        self.d = {}
        with open("Login/loginData.txt", "r") as f:
            for line in f:
                try:
                    if line == "":
                        continue
                    else:
                        (key, value) = line.rstrip("\n").split(":")
                        # print(1)
                except ValueError:
                    pass

                self.d[key] = value

        # print(self.d.keys())

        # Assign the variable names
        self.name_var = StringVar()
        self.pwd_var = StringVar()
        self.re_pwd_var = StringVar()

    def login_or_sign(self):
        self.root.title("Login or Sign-Up")
        self.login()

        self.root.mainloop()

    def log_submit(self):
        self.name = self.name_var.get()
        pwd = self.pwd_var.get()

        if self.name == "ADMINMODE" and pwd == "GODMODE":
            res = tkinter.messagebox.askquestion("Admin Mode",
                                                 "You're about to enter admin mode. You would have complete access to "
                                                 "the database. Are you sure you want to continue?") 
            if res == "yes":
                self.admin_enable()
            else:
                self.login()

        elif self.name not in self.d.keys():
            tkinter.messagebox.showerror("Verification", "Invalid Username! Don't have an account? Try signing up!")

        else:
            if self.d[self.name] != pwd:
                tkinter.messagebox.showerror("Verification", "Invalid Password! Don't have an account? Try signing up!")

            else:
                tkinter.messagebox.showinfo("Verification", "Username and Password verified!")
                self.sign_in = False
                self.root.destroy()
                # self.top.destroy()
                return True

        # print(name, pwd)

    def sign_submit(self):
        self.name = self.name_var.get()
        pwd = self.pwd_var.get()
        re_pwd = self.re_pwd_var.get()

        if self.name != "" or pwd != "":

            if self.name not in self.d.keys():
                if pwd == re_pwd:
                    self.f.write(self.name + ":" + pwd + "\n")
                    tkinter.messagebox.showinfo("Verification", "Account created successfully")
                    self.sign_in = True
                    self.top.destroy()
                    self.root.destroy()
                    return True
                else:
                    tkinter.messagebox.showerror("Verification", "Re-entered password does not match!")
            else:
                tkinter.messagebox.showerror("Verification", "Username already exists")

        else:
            tkinter.messagebox.showerror("Verification", "Please enter valid input")

    def login(self):
        self.root.title("Inventory Manager")
        if self.sign_page:
            self.root.deiconify()
            self.top.withdraw()
        else:

            # WINDOW HEADER
            title = Label(self.root, text="LOGIN", bg="light sky blue", pady=20, font=("Arial Bold", 25))
            title.place(x=300, y=25, anchor="center")

            # USER INPUTS
            uname = Label(self.root, text="     Username: ", bg="light sky blue")
            pwd = Label(self.root, text="     Password: ", bg="light sky blue")

            uname.place(x=170, y=125, anchor="center")
            pwd.place(x=170, y=185, anchor="center")

            e1 = Entry(self.root, textvariable=self.name_var)
            e2 = Entry(self.root, textvariable=self.pwd_var, show="*")

            e1.place(x=250, y=110)
            e2.place(x=250, y=170)

            # BUTTONS
            sub_btn = tkinter.Button(self.root, text="Login", width=25, fg="green", bg="white",
                                     command=self.log_submit)
            sign_btn = tkinter.Button(self.root, text="Don't have an account? Sign In!", fg="blue", bg="white",
                                      width=40,
                                      command=self.sign)
            sub_btn.place(x=180, y=300)
            sign_btn.place(x=120, y=400)

        self.root.mainloop()

    def sign(self):
        if not self.sign_page:
            # Creating a new window
            self.top = Toplevel()
            self.top.geometry("600x500")
            self.top.title("Inventory Manager")
            self.top.configure(bg="light sky blue")

        if self.sign_page:
            self.top.deiconify()

        self.sign_page = True
        self.root.withdraw()

        self.f = open("Login/loginData.txt", "a+")

        # WINDOW HEADER
        title = Label(self.top, text="INVENTORY MANAGER", bg="light sky blue", pady=20, font=("Arial Bold", 25))
        title.place(x=300, y=25, anchor="center")

        # USER INPUT
        uname = Label(self.top, text="Choose a Username: ", bg="light sky blue")
        pwd = Label(self.top, text="Type out your Password: ", bg="light sky blue")
        re_pwd = Label(self.top, text="Re-Type out your Password: ", bg="light sky blue")

        uname.place(x=170, y=125, anchor="center")
        pwd.place(x=170, y=185, anchor="center")
        re_pwd.place(x=170, y=245, anchor="center")

        e1 = Entry(self.top, textvariable=self.name_var)
        e2 = Entry(self.top, textvariable=self.pwd_var, show="*")
        e3 = Entry(self.top, textvariable=self.re_pwd_var, show="*")

        e1.place(x=270, y=110)
        e2.place(x=270, y=170)
        e3.place(x=270, y=230)

        # BUTTONS
        sub_btn = tkinter.Button(self.top, text="Sign Up for free!", width=25, fg="green", bg="white",
                                 command=self.sign_submit)
        log_btn = tkinter.Button(self.top, text="Already have an account? Login!", fg="blue", bg="white", width=40,
                                 command=self.login)

        sub_btn.place(x=180, y=300)
        log_btn.place(x=120, y=400)

        # self.root.mainloop()
        self.top.mainloop()

    def admin_enable(self):
        print("\n\n\n---- ADMIN MODE ----")

        while True:
            cmd = input("Enter your commands: ")
            if cmd == "show users":
                print([i for i in self.d])

            elif cmd == "show pwds":
                for i in self.d:
                    print(i, ":", self.d[i])

            elif cmd == "quit":
                break

            else:
                print("Invalid user received! Exiting admin mode...")
                break

        self.login_or_sign()
