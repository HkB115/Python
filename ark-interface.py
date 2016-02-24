#!/usr/bin/python
## Created by HkB115
ver = '16.2.23.00' # DO NOT CHANGE THIS
from os import name,system
import socket
from sys import exit,version_info
from time import sleep

######## Configuration ########
server_ip = 'localhost' # Enter the IP of the server you are connecting to. If left empty, defaults to localhost.
server_port = 8888 # Enter the port of the server through which you are connecting to. If left empty, defaults to 8888.

###############################

try:
 if(server_ip == '' or server_ip == 'localhost'):
  server_ip = '127.0.0.1'
 server_ip = str(server_ip)
except:
 print("Enter a valid IP or domain as a string for the server IP!")
 sleep(3)
 exit()
 
try:
 if(server_port == None):
  server_port = 8888
 server_port = int(server_port)
except:
 print("Enter a valid integer for the server port!")
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
 while(True):
  clrdisp()
  for entry in menu:
   if(entry == 0 or entry == 9):
    print(str(menu[entry]))
   else:
    print("#",str(entry),menu[entry])
  selection = userInput("Select an option: ")
  clrdisp()
  if(selection == '1'): # Get server status
   server_status()
  elif(selection == '2'): # Restart server
   inloop = True
   while(inloop):
    clrdisp()
    yn0 = userInput("Are you sure you want to restart the server? (y/n): ")
    if(yn0 == 'y'):
     while(inloop):
      clrdisp()
      yn1 = userInput("Would you like to enable a 10 minute countdown? (y/n): ")
      if(yn1 == 'y'):
       #Send restart command with 10 minute countdown option through socket
       inloop = False
      elif(yn1 == 'n'):
       #Send restart command without 10 minute countdown option through socket
       inloop = False
      else:
       print("Please enter y or n")
     inloop = False
    elif(yn0 == 'n'):
     inloop = False
    else:
     print("Please enter y or n")
  elif(selection == '3'): # Start server
   start_server()
  elif(selection == '4'): # Stop server
   inloop = True
   while(inloop):
    clrdisp()
    yn0 = userInput("Are you sure you want to restart the server? (y/n): ")
    if(yn0 == 'y'):
     #Send stop command through socket
     in_loop = False
    elif(yn0 == 'n'):
     inloop = False
    else:
     print("Please enter y or n")
  elif(selection == '5'):
   update_server()
  elif(selection == '6'):
   update_script()
  elif(selection == '7'):
   sock.close()
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

def start_server():
 print("Code here")

def update_server():
 print("Code here")

def update_script():
 print("Code here")

python3 = version_info[0] > 2 # Check for Python3
server_address = (str(server_ip),int(server_port))
print("Connecting to %s through port %s" %server_address)
#sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
 sock = socket.create_connection((server_ip,server_port))
except:
 print("Failed to create a connection with the server!")
 sleep(3)
 exit()
connected = False
tries = 0
while(connected != True):
 try:
  sock.connect(server_address)
  connected = True
 except:
  tries += 1
  sleep(3)
 if(tries > 5):
  print("Connection failed!")
  sleep(3)
  break
try:
 print("Verifying connection...")
 send = "Ping!"
 sock.sendall(send)
 amount_received = 0
 amount_expected = len(send)
 while(amount_received < amount_expected):
  data = sock.recv(64)
  amount_received += len(data)
  print('received "%s"' % data)
except:
 print("Connection terminated!")
print("Connected!")
sleep(2)
try:
 main()
finally:
 exit()
