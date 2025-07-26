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
