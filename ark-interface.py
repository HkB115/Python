#!/usr/bin/python
## Created by HkB115
ver = '16.2.23.00' # DO NOT CHANGE THIS
from os import name,system
import socket
from sys import exit,version_info
from time import sleep

######## Configuration ########
server_ip = 'localhost' # Enter the IP of the server you are connecting to.
server_port = 8888 # Enter the port of the server through which you are connecting to. If left empty, defaults to 8888.

###############################

if(server_address == '' or server_address == 'localhost'):
 server_address = '127.0.0.1'

try:
 server_port = int(server_port)
except:
 print("Enter a valid integer for the server port!"
 sleep(3)
 exit()

def clrdisp():
 system('cls' if name == 'nt' else 'clear')

def main():
 menu={}
 menu[0] = "####################################"
 menu[1] = "Get server status"
 menu[2] = "Restart server"
 menu[3] = "Start server"
 menu[4] = "Stop server"
 menu[5] = "Update server"
 menu[6] = "Update this script"
 menu[7] = "Exit"
 menu[9] = "####################################"
 while(in_loop):
  in_loop = True
  clrdisp()
  for entry in menu:
   if(entry == 0 or entry == 9):
    print(str(menu[entry]))
   else:
    print("#",str(entry),menu[entry])
  selection = userInput("Select an option: ")
  clrdisp()
  if(selection == '1'):
   server_status()
  elif(selection == '2'):
   restart_server()
  elif(selection == '3'):
   start_server()
  elif(selection == '4'):
   stop_server()
  elif(selection == '5'):
   update_server()
  elif(selection == '6'):
   update_script()
  elif(selection == '7'):
   exit()
  else:
   print("Option not recognized!")
   sleep(3)
   
def userInput(msg):
 if(python3):
  return input(msg)
 else:
  return raw_input(msg)

def server_status():
 print("Code here")
 socket.create_connection(server_address,30)

def restart_server():
 in_loop = true
 yn0 = userInput("Are you sure you want to restart the server? (y/n): ")
 clrdisp()
 if(yn0 == 'y'):
  yn1 = userInput("Would you like to enable a 10 minute countdown? (y/n): ")
  while(in_loop):
   in_loop = True
   if(yn1 == 'y'):
    #Send restart command with 10 minute countdown option through socket
    in_loop = False
   elif(yn1 == 'n'):
    #Send restart command without 10 minute countdown option through socket
    in_loop = False
   else:
    print("Please enter y or n")
  return
 elif(yn0 == 'n'):
  return
 else:
  print("Please enter y or n")
  restart_server()
 
 print("Code here")

def start_server():
 print("Code here")

def stop_server():
 yn0 = userInput("Are you sure you want to restart the server? (y/n): ")
 clrdisp()
 if(yn0 == 'y'):
  #Send stop command through socket
  return
 elif(yn0 == 'n'):
  return
 else:
  print("Please enter y or n")
  stop_server()

def update_server():
 print("Code here")

def update_script():
 print("Code here")

python3 = version_info[0] > 2 # Python 3 check
server_address = (str(server_ip),int(server_port))
print("Connecting to %s through port %s" %server_address)
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
 sock.bind(server_address)
 sock.listen(1)
except:
 print("Connection failed!")
 sleep(3)
 exit()
connecting = True
tries = 0
while(connecting):
 sock.send('Ping!')
 recv = connection.recv(16)
 if(recv == 'Pong!'):
  connected = False
 else:
  tries += 1
 sleep(5)
 if(tries > 3):
  print("Connection failed!")
  sleep(3)
  exit()
print("Connected!")
sleep(3)
main()
finally:
 exit()
