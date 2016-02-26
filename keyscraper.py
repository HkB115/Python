#/usr/bin/env python
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
ask_repeat = False # Ask to try again after each successful find. Setting to default makes it repeat automatically.
base_url = 'http://www.google.com/*' # URL of the site you will be scraping. Use a * to denote where the URL will change.
# The character set you wish to use. You may use one of the options or give your own.
# 'alphanumeric.lower' includes all lowercase letters and all digits.
# 'alphanumeric.upper' includes all uppercase letters and all digits.
# 'alphanumeric.all' includes all uppercase letters, all lowercase letters, and all digits.
# 'alphabetic.lower' includes all lowercase letters.
# 'alphabetic.upper' includes all uppercase letters.
# 'alphabetic.all' includes all lowercase letters and all uppercase letters
# 'digits' for all digits.
char_set = 'alphanumeric.all' # Use one of the strings provided above or make your own set.
delay = 2 # Delay between retries in seconds. 2 is usually enough to prevent any kind of IP blocking bot.
max_length = 8 # Maximum length of characters after the base url.
min_length = 4 # Minimum length of characters after the base url.
key = 'key|test' # The key you are looking for. You may use regex here.
###############################

def main():
 global hits
 global matches
 repeat = True
 while(repeat):
  global hits
  global matches
  found = False
  while(found != True):
   length = randint(min_length, max_length)
   rand_set = ''.join(sample(char_set, length))
   url = base_url.replace('*', rand_set)
   print("\n################ NEW SEARCH ################")
   print("# [....] Validating %s" % url)
   try:
    content = urllib.urlopen(url).read()
    print("# [ OK ] Valid URL found. Searching for key...")
    hits += 1
    match = re.findall(key, content)
    if(len(match) == 0):
     print("# [FAIL] Key not found. Starting over...")
    else:
     filename = str(rand_set + '.txt')
     print("# [ OK ] Key match found! Saving content to %s" % (filename))
     matches += 1
     fp = open(filename, 'a')
     fp.write(content)
     fp.close()
     found = True
   except:
    print("# [FAIL] URL could not be reached. Starting over...")
   print("############################################")
   print("Valid URLs found: %d   Key matches found: %d" % (hits, matches))
   sleep(delay)
  ask = ask_repeat
  while(ask):
   yn = user_input("Would you like to try again? (y/n): ")
   if(yn == 'y'):
    ask = False
    repeat = True
   elif(yn == 'n'):
    ask = False
    repeat = False
   else:
    print("Please enter y or n")
    ask = True
    repeat = True 
 return

def user_input(msg): 
 if(python3):
  return input(msg) # Uses the input function if a Python 3 environment is being used.
 else:
  return raw_input(msg) # Uses the raw_input function if a Python environment less than 3 is being used.

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
if(max_length < min_length):
 print("[FAIL] Max length must be larger than min length!")
 sleep(3)
 exit()
hits = 0
matches = 0
main()
