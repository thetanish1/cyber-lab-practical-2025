#One-Time Pad Encryption and Decryption Code:

import os

# Function to generate a random key of the same length as the message
def generate_key(length):
    return os.urandom(length)  # Returns a key of random bytes

# Function to encrypt the message using the One-Time Pad
def encrypt(message, key):
    # Convert the message to bytes
    message_bytes = message.encode('utf-8')
    
    # Perform XOR operation between message and key
    cipher_text = bytes([message_bytes[i] ^ key[i] for i in range(len(message_bytes))])
    
    return cipher_text

# Function to decrypt the cipher text using the One-Time Pad
def decrypt(cipher_text, key):
    # Perform XOR operation between cipher text and key (same as encryption)
    decrypted_message = bytes([cipher_text[i] ^ key[i] for i in range(len(cipher_text))])
    
    # Convert bytes back to string
    return decrypted_message.decode('utf-8')

# Example usage
message = input("Enter the message to encrypt: ")

# Generate a random key of the same length as the message
key = generate_key(len(message))

# Encrypt the message
cipher_text = encrypt(message, key)
print(f"Encrypted Message (in bytes): {cipher_text}")

# Decrypt the cipher text
decrypted_message = decrypt(cipher_text, key)
print(f"Decrypted Message: {decrypted_message}")


def run_practical_7():
    # Add code for Practical 1
    print("Running Practical 1")
