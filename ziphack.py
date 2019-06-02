#!/usr/bin/python2
#coded by Sayuk Beast

space = " " * 66
cya = "Bye!!Hope see you again :)"
print(" ____                    _    ____                 _")
print("/ ___|  __ _ _   _ _   _| | _| __ )  ___  __ _ ___| |_")
print("\___ \ / _` | | | | | | | |/ /  _ \ / _ \/ _` / __| __|")
print(" ___) | (_| | |_| | |_| |   <| |_) |  __/ (_| \__ \ |_")
print("|____/ \__,_|\__, |\__,_|_|\_\____/ \___|\__,_|___/\__|")
print("             |___/")
print(space)
print("This Tool is created by Sayuk Beast")
print(space)
print("DO NOT COPY THIS SCRIPT WITHOUT MY PERMISION")
print("PLEASE APRECIATE MY HARD WORK")
print(space)

import zipfile

zip = raw_input("Insert your zipfile name[path] :  ")
passfile = raw_input("Insert your PasswordList name[path] : ")
zfile = zipfile.ZipFile(zip)
passfile = open(passfile, "r")
for password in passfile.readlines():
    password = password.strip("\n").strip("\r")
    try:
        zfile.extractall(pwd=password)
        print ("password founded >> " + password + " << ")
    except Exception, e:
        print (" [!] trying password > " + password +'')
print(cya)
