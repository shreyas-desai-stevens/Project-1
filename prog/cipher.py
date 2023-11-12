import argparse
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os
import sys

def derive_key(password, salt, length=32):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        iterations=100000,
        salt=salt,
        length=length,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def encrypt_file(file_path, password):
    salt = os.urandom(16)
    key = derive_key(password, salt)

    with open(file_path, 'rb') as file:
        plaintext = file.read()

    cipher = Cipher(algorithms.AES(key), modes.CFB(salt), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path , 'wb') as file:
        file.write(salt + ciphertext)
    

def decrypt_file(file_path, password):
    with open(file_path, 'rb') as file:
        data = file.read()

    salt = data[:16]
    ciphertext = data[16:]

    key = derive_key(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CFB(salt), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(file_path, 'wb') as file:
        file.write(plaintext)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using a password.")
    parser.add_argument("file_path", type=str, default=sys.stdin, help="Path to the file to be encrypted or decrypted.")
    parser.add_argument("password", type=str, help="Password for encryption or decryption.")
    parser.add_argument("-e", "--encrypt",  action="store_true", help="Encrypt the file.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file.")


    args = parser.parse_args()

    print(args._get_args)

    if args.encrypt:
        encrypt_file(args.file_path, args.password)
        print("File encrypted successfully.")
    elif args.decrypt:
        decrypt_file(args.file_path, args.password)
        print("File decrypted successfully.")
    else:
        print("Please specify either --encrypt or --decrypt.")

if __name__ == "__main__":
    main()
