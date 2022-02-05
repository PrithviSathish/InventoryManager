# ----- IMPORTS -----
from Login import coloramaFile
from Backend import commands
from Frontend import userApplication2


# ----- MAIN CODE HERE -----
print("----- WELCOME -----")

usr = coloramaFile.StyleLogin()
usr.login_or_sign()
usr_nme = usr.name
# print(usr_nme, sign_in) 
base = commands.DatabaseCommand()

interface = userApplication2.UI(usr_nme)


