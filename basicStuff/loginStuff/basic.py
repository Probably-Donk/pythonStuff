from cryptography.fernet import Fernet
from cryptography import *

def generate_key():
    # Generate a key and save it to a file for later use
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Load the previously generated key from the file
    with open("encryption_key.key", "rb") as key_file:
        return key_file.read()

def encrypt_message(message, key):
    f = Fernet(key)
    encrypted_message = f.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, key):
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message).decode()
    return decrypted_message