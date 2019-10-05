import crypt

# # How to get h_id and salt from the passwd string
# f = open('mypassword.txt', 'r')
# mypasshash = f.read()
# print mypasshash
# mypass = mypasshash.split(':')[1]
# print mypass
# h_id, salt = mypass.split('$')[1:3]
# print h_id
# print salt


# # Code for calculating SHA512 Hash Shadow
# h_id = 6
# salt = 'MQrgwqU1'
# # input_salt = $6$/zpAihl2
# input_salt = '${}${}'.format(h_id, salt)
# print input_salt
# password = 'abc123'

# calcHashValue = crypt.crypt(password, input_salt)
# print(calcHashValue)

# Code for calculating default md5 Hash Shadow
password = 'toor'
input_salt = 'X0'
calcHashValue = crypt.crypt(password, input_salt)
print(calcHashValue)
