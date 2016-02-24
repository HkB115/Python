#!/usr/bin/python
## Created by HkB115
ver='02.23.16' # DO NOT CHANGE THIS
from os import name,system
import socket
from time import sleep

######## Configuration ########
server_address='127.0.0.1' # Enter the IP of the server you are connecting to.
server_port='' # Enter the port of the server through which you are connecting to. If left empty, defaults to 8888.


###############################

def clrdisp():
 system('cls' if name=='nt' else 'clear')

def main():
 menu={}
 menu[0]="####################################"
 menu[1]="Get server status"
 menu[2]="Restart server"
 menu[3]="Start server"
 menu[4]="Stop server"
 menu[5]="Update server"
 menu[6]="Update this script"
 menu[7]="Exit"
 menu[9]="####################################"
 while(True):
  clrdisp()
  for entry in menu:
   if(entry==0 or entry==9):
    print(str(menu[entry]))
   else:
    print("#",str(entry),menu[entry])
  selection=input("Select an option: ")
  clrdisp()
  if(selection=='1'):
   server_status()
  elif(selection=='2'):
   restart_server()
  elif(selection=='3'):
   start_server()
  elif(selection=='4'):
   stop_server()
  elif(selection=='5'):
   update_server()
  elif(selection=='6'):
   update_script()
  elif(selection=='7'):
   break
  else:
   print("Option not recognized!")
   sleep(3)

def server_status():
 print("Code here")
 socket.create_connection(server_address,30)

def restart_server():
 yn=input("Are you sure you want to restart the server? (y/n): ")
 clrdisp()
 if(yn=='y'):
  #Send restart command through socket
 elif(yn=='n'):
  main()
 else:
  print("Please enter y or n")
  restart_server()
 
 print("Code here")

def start_server():
 print("Code here")

def stop_server():
 yn=input("Are you sure you want to restart the server? (y/n): ")
 clrdisp()
 if(yn=='y'):
  #Send stop command through socket
 elif(yn=='n'):
  main()
 else:
  print("Please enter y or n")
  stop_server()

def update_server():
 print("Code here")

def update_script():
 print("Code here")

client_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if(server_port==''):
 server_port=8888
yn='null'
main()
