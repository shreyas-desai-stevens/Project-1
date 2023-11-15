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
    try:
        stdin_flag = file_path.name == '<stdin>'
        if not stdin_flag:
            file_path = file_path.name
        # salt = os.urandom(16)
        salt = "some_salt_string".encode('utf-8')
        key = derive_key(password, salt)

        if stdin_flag:            
            plaintext  = sys.stdin.read().strip().encode('utf-8')
        else:
            with open(file_path, 'rb') as file:
                plaintext = file.read()
        # print("plaintext",plaintext)

        cipher = Cipher(algorithms.AES(key), modes.CFB(salt), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()

        if not stdin_flag:        
            with open(file_path+'.enc' , 'wb') as file:
                file.write(salt + ciphertext)
        print(salt + ciphertext)
    except Exception as e:
        sys.stderr.write(f"{e}")
        sys.exit(1)

        
def decrypt_file(file_path, password):
    try:
        stdin_flag = file_path.name == '<stdin>'
        if not stdin_flag:
            file_path = file_path.name

        if stdin_flag:
            data = sys.stdin.read().encode('utf-8')
        else:
            with open(file_path+'.enc', 'rb') as file:
                data = file.read()
        ciphertext = data[16:]
        if data:        
            salt = data[:16]
        else:
            salt="some_salt_string".encode('utf-8')

        key = derive_key(password, salt)

        cipher = Cipher(algorithms.AES(key), modes.CFB(salt), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()

        if not stdin_flag:
            with open(file_path+'.dec', 'wb') as file:
                file.write(plaintext)
        print(plaintext)
    except Exception as e:
        sys.stderr.write(f"{e}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Encrypt or decrypt a file using a password.")
    parser.add_argument("file_path", nargs='?', type=argparse.FileType("r"), default=sys.stdin, help="Path to the file to be encrypted or decrypted.")
    # parser.add_argument("password", nargs=1,type=str,default="pword", help="Password for encryption or decryption.")
    parser.add_argument("-e", "--encrypt",  action="store_true", help="Encrypt the file.")
    parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file.")

    args = parser.parse_args()
    password = 'password'

    if args.encrypt:
        encrypt_file(args.file_path, password)
        # print("File encrypted successfully.")
    elif args.decrypt:
        decrypt_file(args.file_path, password)
        # print("File decrypted successfully.")
    else:
        sys.stderr.write(f"Please specify either --encrypt or --decrypt.")
        sys.exit(1)

if __name__ == "__main__":
    main()
