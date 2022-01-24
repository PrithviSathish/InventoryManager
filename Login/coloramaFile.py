# from termcolor import colored
import colorama
from colorama import Fore
from pyfiglet import Figlet

colorama.init()


class StyleLogin:

    def __init__(self):
        self.name = ""
        self.sign = False
        self.d = {}
        f = open("Login/loginData.txt", "a+")
        f.close()

    def intro(self, txt, color="Blue"):
        f = Figlet(font='slant')
        word = txt
        CLEAR_SCREEN = '\033[2J'
        if color.lower() == "red":
            col = Fore.RED
        elif color.lower() == "blue":
            col = Fore.BLUE
        elif color.lower() == "green":
            col = Fore.GREEN
        else:
            col = Fore.RED
        print(CLEAR_SCREEN + col + f.renderText(word) + Fore.RESET)

    def login_or_sign(self):
        self.intro("LOGIN / SIGN-UP")
        LorS = input("Welcome! Please type 'S' to sign up! Or already have an account here? type 'L' to Login in! ")

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
        print(self.d)

        if LorS.lower() == "s":
            self.name = self.Sign()
            self.sign = True

        elif LorS.lower() == "l":
            self.name = self.Log()
            self.sign = False

        elif LorS == "ADMINMODE":
            if input("YOU ARE ENTERING A FORBIDDEN MODE! PWD: ") == "GODMODE":
                self.adminmode()

        else:
            print("Please enter a valid choice!")
            self.login_or_sign()

    # Log function::Sign function
    def Log(self):
        self.intro("LOGIN")
        usr_nme = input("Enter your username: ")

        if usr_nme not in self.d.keys():
            print("Invalid Username! Don't have an account? Try signing up!")
            self.Log()

        else:
            usr_pwd = input("Enter your password: ")

            if self.d[usr_nme] != usr_pwd:
                print("Invalid Password! Don't have an account? Try signing up!")
                self.Log()
            else:
                self.intro("WELCOME !!", color="Green")
                return usr_nme

    def Sign(self):
        self.intro("SIGN-UP")
        f = open("Login/loginData.txt", "a+")
        good_nme = False
        while not good_nme:
            usr_nme = input("What username do you prefer? ")

            if usr_nme in self.d.keys():
                print("Username already exists!")

            else:
                good_nme = True

        good_pwd = False
        while not good_pwd:
            usr_pwd = input("Type out your password: ")
            usr_confPwd = input("Re-Type password: ")

            if usr_confPwd == usr_pwd:
                good_pwd = True

            else:
                print("Passwords do not match!")

        self.intro("WELCOME!!", color="Green")
        # f = open(self.filename, "a+")
        f.write(usr_nme + ":" + usr_pwd + "\n")
        return usr_nme

    def adminmode(self):
        self.intro("ADMIN MODE", color="Red")
        cmd = True
        while cmd:
            cmd = input("Enter your commands: ")
            if cmd == "show users":
                print([x for x in self.d.keys()])
                continue
            if cmd == "show users w pwd":
                for user in self.d:
                    print(user, ":", self.d[user])
                continue
            if cmd == "quit":
                cmd = False
                break
            else:
                print("Unusual activity recognized...Exiting")
                cmd = False
