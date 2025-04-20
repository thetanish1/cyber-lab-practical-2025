# Diffie-Hellman Key Exchange Example

# Function to calculate modular exponentiation (base^exponent % modulus)
def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

# Function for Diffie-Hellman Key Exchange
def diffie_hellman(p, g, private_a, private_b):
    # Calculate public keys for both users
    public_a = mod_exp(g, private_a, p)
    public_b = mod_exp(g, private_b, p)

    # Calculate shared secret for user A
    shared_secret_a = mod_exp(public_b, private_a, p)

    # Calculate shared secret for user B
    shared_secret_b = mod_exp(public_a, private_b, p)

    # The shared secrets should be the same
    if shared_secret_a == shared_secret_b:
        print(f"Shared secret successfully established: {shared_secret_a}")
    else:
        print("Error: Shared secrets do not match.")

    return shared_secret_a

# Example usage:

# Choose a large prime number (p) and a generator (g) 
p = 23  # Prime number
g = 5   # Generator

# Private keys chosen by users A and B
private_a = 6  # User A's private key
private_b = 15  # User B's private key

# Execute Diffie-Hellman Key Exchange
shared_secret = diffie_hellman(p, g, private_a, private_b)

