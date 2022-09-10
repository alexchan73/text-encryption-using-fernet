from cryptography.fernet import Fernet

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

    key_var =  generate_key()
    
    print("This is your encrypted string: " + str(encrypt(usr_input, key_var).decode()))
    encry_token = encrypt(usr_input, key_var)

    print("This is your decrypted string: " + str(decrypt(key_var, encry_token).decode()))
main()
