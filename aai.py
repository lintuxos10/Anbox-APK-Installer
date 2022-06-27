#!/usr/bin/python3

import sys, os
from tkinter import *

x = sys.argv[1]

def install():
    os.system("adb install "+x)
    label.config(text="Sucess!")
    yes.pack_forget()

window = Tk()
window.title("Anbox APK Installer")
label = Label(master=window, text="Install "+x+"?")
yes = Button(master=window, command=install, text="Install")

label.pack()
yes.pack()
window.mainloop()
