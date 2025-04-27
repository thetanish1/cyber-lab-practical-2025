#AES Encryption and Decryption Code in Python

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

# Function to pad the data to make it a multiple of 16 bytes
def pad(data):
    while len(data) % 16 != 0:
        data += ' '
    return data

def encrypt_data(key, data):
    data = pad(data)
    cipher = AES.new(key, AES.MODE_CBC)  # CBC mode of AES
    iv = cipher.iv  # Initialization vector
    encrypted_data = cipher.encrypt(data.encode('utf-8'))
    return base64.b64encode(iv + encrypted_data).decode('utf-8')

def decrypt_data(key, encrypted_data):
    encrypted_data = base64.b64decode(encrypted_data)
    iv = encrypted_data[:16]  # Extract the IV
    encrypted_data = encrypted_data[16:]  

    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
    
    return decrypted_data.strip()

if __name__ == "__main__":
    key = get_random_bytes(16)  
    print(f"Key: {base64.b64encode(key).decode()}")

    # Data to be encrypted
    data = "This is a secret message"
    print(f"Original Data: {data}")

    encrypted = encrypt_data(key, data)
    print(f" Practical no 9: \n Encrypted Data: {encrypted}")

    decrypted = decrypt_data(key, encrypted)
    print(f"Decrypted Data: {decrypted}")

def run_practical_9():
    print("Running Practical 9")
