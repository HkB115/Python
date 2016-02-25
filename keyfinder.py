#/usr/bin/python
#Made by HkB115. Feel free to use, modify, or distribute.
from itertools import chain
from random import choice, randint, sample, seed
import re
import string
from time import sleep,time
import urllib2

######## Configuration ########
base_url = 'http://pastebin.com/' # Base url for the site.
#just_ascii = True # Disable to use all characters.
max_length = 8 # Maximum length of characters after the base url.
min_length = 2 # Minimum length of characters after the base url.
string_to_find = 'fart' # The key you are looking for. You may use regex here.
###############################

######## Advanced Configuration ########
min_digits = 0 # Minimum number of digits after the base url.
min_lower = 0 # Minimum number of lower case characters after the base url.
min_upper = 0 # Minimum number of upper case characters after the base url.
########################################

if(min_digits < 1):
 min_digits = 0
if(min_lower < 1):
 min_lower = 0
if(min_upper < 1):
 min_upper = 0

def rand_string(length, digits, lower, upper):
 seed(time())
 #lowercase = string.lowercase.translate(None, "o")
 #uppercase = string.uppercase.translate(None, "O")
 lowercase = string.ascii_lowercase
 uppercase = string.ascii_uppercase
 letters = "{0:s}{1:s}".format(lowercase, uppercase)
 a_string = list(
  chain(
   (choice(uppercase) for _ in range(upper)),
   (choice(lowercase) for _ in range(lower)),
   (choice(string.digits) for _ in range(digits)),
   (choice(letters) for _ in range((length - digits - upper - lower)))
        )
    )
 return "".join(sample(a_string, len(a_string)))

not_found = True
while(not_found):
 rand_length = randint(min_length, max_length)
 after_url = rand_string(length = rand_length, digits = min_digits, lower = min_lower, upper = min_upper)
 url = str(base_url + after_url)
 print("######## NEW SEARCH ######")
 print("Trying %s" % url)
 try:
  content = urllib2.urlopen(url).read()
  url_valid = True
  print("%s found. Searching..." % url)
  matches = re.findall(string_to_find, content)
  if(len(matches) == 0):
   print("Key not found. Starting over...")
   sleep(1)
  else:
   print("Ahoy, Cap'n! We found some booty at %s" % url)
   sleep(3)
   not_found = False
 except:
  print("%s returned 404. Starting over..." % url)
  sleep(3) # To prevent IP blocking :/
