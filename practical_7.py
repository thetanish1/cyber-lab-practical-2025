#One-Time Pad Encryption and Decryption Code:

import os

def generate_key(length):
    return os.urandom(length)  # Returns a key of random bytes

def encrypt(message, key):
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')
    
    cipher_text = bytes([message_bytes[i] ^ key[i] for i in range(len(message_bytes))])
    
    return cipher_text

def decrypt(cipher_text, key):
    decrypted_message = bytes([cipher_text[i] ^ key[i] for i in range(len(cipher_text))])
    
    return decrypted_message.decode('utf-8')

message = input("Enter the message to encrypt: ")

key = generate_key(len(message))

cipher_text = encrypt(message, key)
print(f"Encrypted Message (in bytes): {cipher_text}")

decrypted_message = decrypt(cipher_text, key)
print(f"Decrypted Message: {decrypted_message}")

def run_practical_7():
    print("Running Practical 7")
