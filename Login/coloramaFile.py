# from termcolor import colored
import colorama
from colorama import Fore
from pyfiglet import Figlet

# from main import CreateLogin

colorama.init()


class styleLogin():

    def __init__(self):
        self.d = {}
        f = open("loginData.txt", "a+")
        f.close()

    def intro(self, txt, color="RED"):
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

    def Login_or_Sign(self):
        self.intro("LOGIN / SIGN-UP")
        LorS = input("Welcome! Please type 'S' to sign up! Or already have an account here? type 'L' to Login in! ")

        with open("loginData.txt", "r") as f:
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
        # print(d)

        if LorS.lower() == "s":
            self.Sign()

        elif LorS.lower() == "l":
            self.Log()

        elif LorS == "ADMINMODE":
            self.adminmode()

        else:
            print("Please enter a valid choice!")
            self.Login_or_Sign()

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
                self.intro("WELCOME!!", color="Green")
                return usr_nme

    def Sign(self):
        self.intro("SIGN-UP")
        f = open("loginData.txt", "a+")
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

    def adminmode(self):
        self.intro("ADMIN MODE")
        pass
