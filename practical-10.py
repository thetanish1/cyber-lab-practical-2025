#DES Encryption and Decryption Code in Python

from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import base64

# Function to pad the data to make it a multiple of 8 bytes (since DES uses 8-byte blocks)
def pad(data):
    while len(data) % 8 != 0:
        data += ' '
    return data

# Function to encrypt the data using DES
def encrypt_data(key, data):
    data = pad(data)
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode for simplicity
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    return base64.b64encode(encrypted_data).decode('utf-8')

# Function to decrypt the data using DES
def decrypt_data(key, encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
    return decrypted_data.strip()

# Example usage
if __name__ == "__main__":
    key = get_random_bytes(8)  # DES uses an 8-byte key
    print(f"Key: {base64.b64encode(key).decode()}")

    # Data to be encrypted
    data = "This is a secret message"
    print(f"Original Data: {data}")

    encrypted = encrypt_data(key, data)
    print(f"Encrypted Data: {encrypted}")

    decrypted = decrypt_data(key, encrypted)
    print(f"Decrypted Data: {decrypted}")
