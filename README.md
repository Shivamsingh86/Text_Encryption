# Text_Encryption
This project is a Python-based encryption tool that secures sensitive score data using three widely-known encryption algorithms: AES, DES, and RSA.
# 🔐 Multi-Algorithm Score Data Encryption Tool

This Python project provides a simple command-line tool to encrypt and decrypt **score data** using three different encryption algorithms: **AES**, **DES**, and **RSA**. It is designed for learning and demonstration of the differences between symmetric and asymmetric encryption techniques.

---

## 📌 Features

- Encrypt and decrypt text-based score data
- Supports three major encryption algorithms:
  - **AES** (Advanced Encryption Standard)
  - **DES** (Data Encryption Standard)
  - **RSA** (Rivest–Shamir–Adleman)
- View encrypted output in **Base64 format**
- Includes a **comparison summary** of all algorithms
- Generates a **PDF report** with code and explanation

---

## 🛠 Technologies Used

- **Python 3**
- **PyCryptodome** – for AES, DES, and RSA implementations
- **Base64** – for encoding binary encrypted data
- **FPDF** – for generating project documentation in PDF format

---

## 📁 Project Structure
encryption_tool/
├── main.py # Main script for user interaction
├── aes_encryption.py # AES algorithm implementation
├── des_encryption.py # DES algorithm implementation
├── rsa_encryption.py # RSA algorithm implementation
├── requirements.txt # Required Python libraries

---

## 🔧 Installation & Setup

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/encryption_tool.git
cd encryption_tool
pip install -r requirements.txt
python main.py

Enter score data (e.g. Alice: 95): Alice: 95
Choose encryption method:
1. AES
2. DES
3. RSA
Enter your choice: 1

Encrypted (AES): b'...'
Decrypted: Alice: 95

Learning Outcomes
Understand the difference between symmetric and asymmetric encryption

Explore the structure of cryptographic functions in Python

Learn how to package and document Python projects

---

Would you like me to add this to your project folder as a file you can download?
