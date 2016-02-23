#!/usr/bin/python
from os import name,system

def clrdisp()
 system('cls' if name=='nt' else 'clear')

def main():
 menu=True
 while(menu)
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
  choice=input("Choose:")
  elif(choice==2):
   update()
  elif(choice==3):
   mainmenu()
  else:
   clrdisp()
   print("Option not recognized!")

main()
