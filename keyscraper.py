#/usr/bin/python
#Made by HkB115. Feel free to use, modify, or distribute.
from random import randint, sample
import re
from sys import exit, version_info
from time import sleep
try:
 import urllib2 as urllib
except:
 import urllib

######## Configuration ########
ask_repeat = True # Ask to try again after each successful find. Setting to default makes it repeat automatically.
base_url = 'http://www.google.com/' # Base url for the site.
# The character set you wish to use. You may use one of the options or give your own.
# 'alphanumeric.lower' includes all lowercase letters and all digits.
# 'alphanumeric.upper' includes all uppercase letters and all digits.
# 'alphanumeric.all' includes all uppercase letters, all lowercase letters, and all digits.
# 'alphabetic.lower' includes all lowercase letters.
# 'alphabetic.upper' includes all uppercase letters.
# 'alphabetic.all' includes all lowercase letters and all uppercase letters
# 'digits' for all digits.
char_set = 'alphanumeric.all' # The character set you wish to use.
delay = 2 # Delay between retries in seconds. Helps prevent IP blocking.
max_length = 8 # Maximum length of characters after the base url.
min_length = 4 # Minimum length of characters after the base url.
key = 'test' # The key you are looking for. You may use regex here.
###############################

python3 = version_info[0] > 2 # Checks for Python 3 environment.
if(char_set == 'alphanumeric.all'):
 char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
elif(char_set == 'alphanumeric.lower'):
 char_set = 'abcdefghijklmnopqrstuvwxyz1234567890'
elif(char_set == 'alphanumeric.upper'):
 char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
elif(char_set == 'alphabetic.all'):
 char_set = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif(char_set == 'alphabetic.lower'):
 char_set = 'abcdefghijklmnopqrstuvwxyz'
elif(char_set == 'alphabetic.upper'):
 char_set = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
elif(char_set == 'digits'):
 char_set = '1234567890'
else:
 char_set = str(char_set)
if(min_length < 1):
 min_length = 0

def main():
 found = False
 while(found != True):
  length = randint(min_length, max_length)
  rand_set = ''.join(sample(char_set, length))
  url = str(base_url + rand_set)
  print("######## NEW SEARCH ########")
  print("Trying %s" % url)
  try:
   content = urllib.urlopen(url).read()
   print("Valid URL found. Searching for key...")
   matches = re.findall(key, content)
   if(len(matches) == 0):
    print("Key not found. Starting over...")
    sleep(delay)
   else:
    filename = str(rand_set + '.txt')
    print("Ahoy, Cap'n! We found some booty at %s! Saving content to %s" % (url, filename))
    fp = open(filename, 'a')
    fp.write(content)
    fp.close()
    sleep(delay)
    found = True
  except:
   print("%s returned 404. Starting over..." % url)
   sleep(delay)
 return

def user_input(msg): 
 if(python3):
  return input(msg) # Uses the input function if a Python 3 environment is being used.
 else:
  return raw_input(msg) # Uses the raw_input function if a Python environment less than 3 is being used.

try_again = True
while(try_again):
 main()
 ask = ask_repeat
 while(ask):
  yn = user_input("Would you like to try again? (y/n): ")
  if(yn == 'y'):
   ask = False
   try_again = True
  elif(yn == 'n'):
   ask = False
   try_again = False
  else:
   print("Please enter y or n")
   ask = True
   try_again = True
