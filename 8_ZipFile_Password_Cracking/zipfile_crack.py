import zipfile

# Open a Dictionary File
f = open("dictionary.txt", 'r')
listofpass = f.readlines()
for password in listofpass:
    #print password.split('\n')[0]
    #print password[:-1]
    try:
        zipF = zipfile.ZipFile("secure.zip")
        zipF.extractall(pwd=password[:-1])
        print password[:-1], ' is the Matching Password'
        break
    except:
        print password[:-1], ' not matching'
