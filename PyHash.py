import os
import hashlib
from getpass import getpass

def Hashfunction():

            password = getpass("Passwort zum Hashen: \n")

            key2 = hashlib.sha1(password.encode())
            key2 = key2.hexdigest()
            key2 = format(key2)
            print(key2)
            print("\n")
            
            print("1: Weiteres Passwort Hashen")
            print("2: Programm Beenden")
            if input() == "1":
                Hashfunction()
            else:
                exit


print("1: Hashen")
print("2: Programm Beenden")

if input() == "1":
    Hashfunction()

else:
    exit
        
1