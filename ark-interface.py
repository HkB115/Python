#!/usr/bin/python
## Created by HkB115
## Feel free to use this code
from os import name,system
import socket
from time import sleep

######## Configuration ########
server_address="127.0.0.1" # Enter the IP of the server you are connecting to.
server_port="" # Enter the port of the server through which you are connecting to. If left empty, defaults to 22.

ver=0.0.1 # DO NOT CHANGE THIS
###############################

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
  clrdisp()
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
  elif(option=='0'):
   menu=False
  else:
   print("Option not recognized!")
   sleep(3)

def server_status():
 print("Code here")
 create_connection(server_address,30)

def restart_server():
 print("Code here")

def start_server():
 print("Code here")

def stop_server():
 print("Code here")

def update_server():
 print("Code here")

def update_script():
 print("Code here")



main()
