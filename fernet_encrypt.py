from cryptography.fernet import Fernet
import os
from os import system, name
def clear():
    if(name == 'nt'):
        _ = system('cls')
    else:
        _ = system('clear')

def generate_key():
    key = Fernet.generate_key()
    key_var  = Fernet(key)
    return key_var


def encrypt(usr_input, key_var):
    encry_token = key_var.encrypt(usr_input)
    return(encry_token)

def decrypt(key_var, encry_token):
    return key_var.decrypt(encry_token)
#when an output has b in front, it is in byte format, to get rid of it -> .decode()
def main():
    usr_input = input("Please enter a message you want to encrypt: ").encode() #converting to byte format
    clear() 
    key_var =  generate_key()
    print("This is your encrypted string: " + str(encrypt(usr_input, key_var).decode())) #decoding byte format

    dec_input = input("Do you wish to decrypt your message?(y/n): ")
    encry_token = encrypt(usr_input, key_var)
    if(dec_input == "y"):
        print("This is your decrypted string: " + str(decrypt(key_var, encry_token).decode()))
    else:
        print("I will keep your message a secret ;) ")
main()
