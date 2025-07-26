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
