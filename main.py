# ----- IMPORTS -----
from Login import tkinterFile
from Backend import commands
from Login import coloramaFile


# ----- MAIN CODE HERE -----
print("----- WELCOME -----")

usr = coloramaFile.StyleLogin()
usr.login_or_sign()
usr_nme, sign_in = usr.name, usr.sign
print(usr_nme, sign_in)

if sign_in:
    base_crawler = commands.DatabaseCommand()
    base_crawler.create_database(usr_nme)
else:
    base_crawler = commands.DatabaseCommand(usr_nme)
