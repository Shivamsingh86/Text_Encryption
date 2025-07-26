## File: main.py

from aes_encryption import encrypt_aes, decrypt_aes
from des_encryption import encrypt_des, decrypt_des
from rsa_encryption import encrypt_rsa, decrypt_rsa, generate_keys
from Crypto.Random import get_random_bytes

def main():
 print("Score Encryption Tool")
 data = input("Enter score data (e.g. Alice: 95): ")
 print("Choose encryption method:\n1. AES\n2. DES\n3. RSA")
 choice = input("Enter your choice: ")
 if choice == '1':
 key = get_random_bytes(16)
 encrypted = encrypt_aes(data, key)
 print("Encrypted (AES):", encrypted)
 print("Decrypted:", decrypt_aes(encrypted, key))
 elif choice == '2':
 key = get_random_bytes(8)
 encrypted = encrypt_des(data, key)
 print("Encrypted (DES):", encrypted)
 print("Decrypted:", decrypt_des(encrypted, key))
 elif choice == '3':
 private_key, public_key = generate_keys()
 encrypted = encrypt_rsa(data, public_key)
 print("Encrypted (RSA):", encrypted)
 print("Decrypted:", decrypt_rsa(encrypted, private_key))
 else:
 print("Invalid choice")
if __name__ == "__main__":
 main()


## File: aes_encryption.py

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
BLOCK_SIZE = 16
def pad(data):
 return data + ' ' * (BLOCK_SIZE - len(data) % BLOCK_SIZE)
def encrypt_aes(data, key):
 cipher = AES.new(key, AES.MODE_ECB)
 return base64.b64encode(cipher.encrypt(pad(data).encode()))
 def decrypt_aes(encrypted_data, key):
 cipher = AES.new(key, AES.MODE_ECB)
 return cipher.decrypt(base64.b64decode(encrypted_data)).decode().rstrip()


## File: des_encryption.py

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64
BLOCK_SIZE = 8
def pad(data):
 return data + ' ' * (BLOCK_SIZE - len(data) % BLOCK_SIZE)
def encrypt_des(data, key):
 cipher = DES.new(key, DES.MODE_ECB)
 return base64.b64encode(cipher.encrypt(pad(data).encode()))
def decrypt_des(encrypted_data, key):
 cipher = DES.new(key, DES.MODE_ECB)
 return cipher.decrypt(base64.b64decode(encrypted_data)).decode().rstrip()


## File: rsa_encryption.py

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64
def generate_keys():
 key = RSA.generate(2048)
 return key.export_key(), key.publickey().export_key()
def encrypt_rsa(data, public_key_bytes):
 public_key = RSA.import_key(public_key_bytes)
 cipher = PKCS1_OAEP.new(public_key)
 return base64.b64encode(cipher.encrypt(data.encode()))
def decrypt_rsa(encrypted_data, private_key_bytes):
 private_key = RSA.import_key(private_key_bytes)
 cipher = PKCS1_OAEP.new(private_key)
 return cipher.decrypt(base64.b64decode(encrypted_data)).decode()


## File: requirements.txt

pycryptodome
