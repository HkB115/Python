#!/usr/bin/python
from os import name,system

def clrdisp()
 system('cls' if name=='nt' else 'clear')

def mainmenu():
 clrdisp()
 print("###################################")
 print("#                                 #")
 print("# 1: Restart                      #")
 print("# 2: Update server                #")
 print("# 3: Update this script           #")
 print("#                                 #")
 print("###################################")
 choice=input("What would you like to do?")

if(choice==1):
 while(restart=='d'):
  restart=input("Are you sure you want to restart? y/n")
  if(restart=='y'):
   restart()
  elif(restart=='n'):
   mainmenu()
  else
   restart='d'
  print("Please enter y or n")
elif(choice==2):
 update()
elif(choice==3):
 mainmenu()
else:
 print("Option not recognized")
 mainmenu()
