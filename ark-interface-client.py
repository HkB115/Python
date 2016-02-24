#!/usr/bin/python
## Created by HkB115
ver = '16.02.24.00' # DO NOT CHANGE THIS
from os import name,system
import socket
from sys import exit,version_info
from time import sleep

######## Configuration ########
server_ip = 'localhost' # Enter the IP of the server you are connecting to. If left empty, defaults to localhost.
server_port = 8888 # Enter the port of the server through which you are connecting to. If left empty, defaults to 8888.
###############################

try: # Sets server_ip to 127.0.0.1 if it is not defined, or if 'localhost' is used.
 if(server_ip == '' or server_ip == 'localhost'):
  server_ip = '127.0.0.1'
 server_ip = str(server_ip)
except:
 print("Enter a valid IP or domain as a string for the server IP!")
 sleep(3)
 exit()
try: # Sets server_port to 8888 if it is not defined.
 if(server_port == None):
  server_port = 8888
 server_port = int(server_port)
except:
 print("Enter a valid integer for the server port!")
 sleep(3)
 exit()

def clrdisp(): # Defines the function clrdisp.
 system('cls' if name == 'nt' else 'clear') # Clears the display using 'cls' if the system is Windows or 'clear' if the system is UNIX.

def main(): # Defines the function main.
 menu = {} # Sets up menu as an array.
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
  selection = userInput("Select an option: ") # Stores the user's input into the literal 'selection' as a string.
  clrdisp()
  # Get server status
  if(selection == '1'):
   server_status()
  # Restart server
  elif(selection == '2'):
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
  # Start server
  elif(selection == '3'):
   start_server()
  # Stop server
  elif(selection == '4'):
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
  # Update server
  elif(selection == '5'):
   update_server()
  # Update this script
  elif(selection == '6'):
   update_script()
  # Exit the program
  elif(selection == '7'):
   sock.close()
   exit()
  # Repeats the menu function if an invalid option is given.
  else:
   print("Option not recognized!")
   sleep(3)

def userInput(msg): 
 if(python3):
  return input(msg) # Uses the input function if a Python 3 environment is being used.
 else:
  return raw_input(msg) # Uses the raw_input function if a Python environment less than 3 is being used.

def server_status():
 print("Code here")

def start_server():
 print("Code here")

def update_server():
 print("Code here")

def update_script():
 print("Code here")

python3 = version_info[0] > 2 # Checks for Python 3 environment.
try:
 print("Connecting to %s through port %s" %server_address)
 server_address = (str(server_ip),int(server_port)) # Stores the specified server IP and port to the literal server_address.
 sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # Attempts to create a socket.
except:
 print("Failed to create a connection with the server")
 sleep(3) # Sleeps for 3 seconds.
 exit() # Exits the program.
connected = False # Stores False to the literal 'connected'.
tries = 0 # Stores 0 to the literal 'tries'.
while(connected != True):
 try:
  sock.create_connection((server_ip,server_port)) # Attempts to create a connection with the specified server and port.
  connected = True # Stores True to the literal 'connected'.
 except: # Increases the number of tries by 1 for each failed attempt at creating a connection.
  tries += 1 # Adds 1 to the literal 'tries'.
  sleep(3) # Sleeps for 3 seconds.
 if(tries > 5): # Exits the program if the number of attempts to create a connection with the server exceeds 5.
  print("Connection timed out")
  sleep(3) # Sleeps for 3 seconds.
  exit() # Exits the program.
try: # Tries to verify the connection by sending a key to the server. If the key matches, it sends back a string to ensure a secure connection.
 print("Verifying connection...")
 send = "Ping!" # Message to send the server for verification.
 sock.sendall(send) # Sends the string 'send' to the connected server.
 data_received = 0 # Sets up the variable for how much data has been received from the server.
 data_expected = len(send) # Sets up the variable for how much data is expected to be received from the server.
 while(data_received < data_expected):
  data = sock.recv(64)
  amount_received += len(data)
  print('received "%s"' % data) # Prints out the data that was received from the server.
except:
 print("Connection could not be verified")
 sleep(3) # Sleeps for 3 seconds.
 exit() # Exits the program.
print("Connected!")
sleep(2) # Sleeps for 2 seconds.
try:
 main() # Calls the function main.
finally: # Executes the following no matter what.
 exit() # Exits the program.
