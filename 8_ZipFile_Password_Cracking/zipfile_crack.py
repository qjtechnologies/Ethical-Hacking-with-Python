'''
###########################################
Author: Qaidjohar Jawadwala
Organization: QJ Technologies.
--------------------------------------------
Code Title: Dictionary based Zip File Password Cracking
-------------------------------------------
#Steps fo Implementation:
---Import zipfile
---Read worllist into a python list
---Initialize zipfile library
---Iterate through the wordlist using for loop
---in each iteration, try to extract the zipfile with the word as password
---handle exception incase password is incorrect

#Extensions to be performed
--Add command line arguments and user inputs on execution
--Make the user interface good looiking
Example:
python zipfile_crack.y <name_of_wordlist> <name of zipfile>

#################################################
'''

import zipfile  # Importing zipfile to work with zipfile
import time  # Just to add some useless delays

dict_file = 'dictionary.txt'  # raw_input("Enter the name of wordlist: ")
zipName = 'zipfile.zip'

f = open(dict_file, 'r')  # Opening the dictionary file
# Initializing the zipfile class with an object
zipF = zipfile.ZipFile(zipName)

# looping through the read dictionary words
for word in f.readlines():
    #print word[:-1]
    #print word.split('\n')[0]
    try:  # in case of wronng password, exception occurs.
        time.sleep(0.2)  # Useless time delay to get the feel
        zipF.extractall(pwd=word[:-1])  # Extraction attempt for the zipfile
        print word[:-1], "is the correct Password"
        break
    except:
        # Exception is thrown in case of wrong password from the list
        print word[:-1], "is not the Password"
