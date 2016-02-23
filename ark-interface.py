#!/usr/bin/python
from os import name,system

def clrdisp()
 system('cls' if name=='nt' else 'clear')

def mainmenu():
 clrdisp()
 print("####################################")
 print("#                                  #")
 print("# 1: Get server status             #")
 print("# 2: Restart server                #")
 print("# 3: Start server                  #")
 print("# 4: Stop server                   #")
 print("# 5: Update server                 #")
 print("# 6: Update this script.           #")
 print("# 0: Exit.                         #")
 print("#                                  #")
 print("####################################")
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
