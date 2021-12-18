# ----- IMPORTS -----
from Login import tkinterFile


# ----- MAIN CODE HERE -----
print("----- WELCOME -----")
usr = tkinterFile.GuiWindow()
usr.login_or_sign()
usr_nme, sign_in = usr.name, usr.sign_in
# print(usr_nme, sign_in)
