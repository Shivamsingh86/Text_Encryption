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
