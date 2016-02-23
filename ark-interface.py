#!/usr/bin/python
from os import name,system
import socket

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
  option=input("Select an option: ")
  if(option=='1')
   server_status()
  elif(option=='2'):
   restart_server()
  elif(option=='3'):
   start_server()
  elif(option=='4'):
   stop_server()
  elif(option=='5'):
   update_server()
  elif(option=='6'):
   update_script()
  elif(option=='7'):
   clrdisp()
   exit()
  else:
   clrdisp()
   print("Option not recognized!")


def server_status():
 clrdisp()
 print("Code here")

def restart_server():
 clrdisp()
 print("Code here")

def start_server():
 clrdisp()
 print("Code here")

def stop_server():
 clrdisp()
 print("Code here")

def update_server():
 clrdisp()
 print("Code here")

def update_script():
 clrdisp()
 print("Code here")


main()
