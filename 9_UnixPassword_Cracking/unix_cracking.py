'''
###########################################
Author: Qaidjohar Jawadwala
Organization: QJ Technologies.
--------------------------------------------
Code Title: Dictionary based Unix Password Cracking
-------------------------------------------
#Steps fo Implementation:
---Import crypt
---Read worllist into a python list
---Read password file and extract hash_id and salt
---Iterate throuh the wordlist, put password and salt to crypt as input
---if the output of crypt match with password in file, then you found the match
---print the incorrect password in case password do not match

#Extensions to be performed
--Add command line arguments and user inputs on execution
--Make the user interface good looking
Example:
python unix_cracking.y <name_of_wordlist> <name of unixpassword file>

#################################################
'''


import crypt  # To perform Hashing and Cryptography functions

f = open('mypassword.txt', 'r')  # Open the password hash file
filehashval = f.read()  # reading the password hash
hashpass = filehashval.split(":")[1]
# Parsing and extracting hash id and salt
h_id, salt = hashpass.split("$")[1:3]
# h_id = 6  #Given manually for demo purpose
# salt = 'ZdD8oJF1' #Given manually for demo purpose
# input_salt is to format the hash id and salt like $6$/zpAihl2
input_salt = '${}${}'.format(h_id, salt)

password = 'secret'  # ToDo: Provide password from File to perform dictionary based attack

# Verify if output is matching with password hash of the file you read. if equal then password is correct else incorrect
calcHashValue = crypt.crypt(password, input_salt)
print(calcHashValue)


# This is for cracking the simple kali linux root password where password is toor
salt = 'X0'
calcHashValue = crypt.crypt('toor', salt)
print calcHashValue
