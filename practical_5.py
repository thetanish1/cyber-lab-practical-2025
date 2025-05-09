import random
from sympy import isprime

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    # Using extended Euclidean algorithm
    d = 0
    x1, x2, y1, y2 = 0, 1, 1, 0
    while e > 1:
        q = e // phi
        phi, e = e % phi, phi
        d, x1 = x1 - q * d, d
        y1, y2 = y2 - q * y1, y1
    if x1 < 0:
        x1 += phi
    return x1

def generate_keys():
    p = q = 1
    while not isprime(p):
        p = random.randint(100, 500)  # Generate random prime number p
    while not isprime(q) or q == p:
        q = random.randint(100, 500)  # Generate random prime number q

    n = p * q
    phi_n = (p - 1) * (q - 1)

    e = 65537  # A common choice for e
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n)

    d = mod_inverse(e, phi_n)

    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]  # Encryption
    return ciphertext

def decrypt(private_key, ciphertext):
    d, n = private_key
    decrypted_text = ''.join([chr(pow(char, d, n)) for char in ciphertext])  # Decryption
    return decrypted_text

def rsa_demo():
    print("Generating RSA keys...")
    public_key, private_key = generate_keys()
    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = "Hello, RSA!"
    print("Original Message:", message)

    encrypted_msg = encrypt(public_key, message)
    print("Practical no 5: \nEncrypted Message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)

# Run RSA Demo
rsa_demo()
def run_practical_5():
    print("Running Practical 5")
