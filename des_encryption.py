
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
