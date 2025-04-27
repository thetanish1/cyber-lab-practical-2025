def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

def diffie_hellman(p, g, private_a, private_b):
    public_a = mod_exp(g, private_a, p)
    public_b = mod_exp(g, private_b, p)

    shared_secret_a = mod_exp(public_b, private_a, p)

    shared_secret_b = mod_exp(public_a, private_b, p)

    if shared_secret_a == shared_secret_b:
        print(f" Practical no 8: \n Shared secret successfully established: {shared_secret_a}")
    else:
        print("Error: Shared secrets do not match.")

    return shared_secret_a

p = 23  # Prime number
g = 5   # Generator

private_a = 6  # User A's private key
private_b = 15  # User B's private key

shared_secret = diffie_hellman(p, g, private_a, private_b)

def run_practical_8():
    print("Running Practical 8")
