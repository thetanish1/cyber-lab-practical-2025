# Chinese Remainder Theorem (CRT)
def extended_gcd(a, b):
    """ Extended Euclidean Algorithm to find gcd and coefficients """
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

def mod_inverse(a, m):
    """ Function to find modular inverse of a under modulo m """
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        raise Exception(f"No modular inverse for a = {a} and m = {m}, gcd is {gcd}")
    else:
        return x % m

def chinese_remainder_theorem(n, a):
    """ Function to find the solution to the system of congruences """
    # n - list of moduli
    # a - list of remainders
    prod = 1
    for ni in n:
        prod *= ni  # Calculate the product of all moduli

    result = 0
    for ni, ai in zip(n, a):
        p = prod // ni  # Find the product of all moduli except ni
        inv = mod_inverse(p, ni)  # Find modular inverse of p mod ni
        result += ai * inv * p  # Apply the formula

    return result % prod  # Return result modulo the product of all moduli

# Input: List of moduli and remainders
n = list(map(int, input("Enter moduli (space-separated): ").split()))
a = list(map(int, input("Enter remainders (space-separated): ").split()))

# Calculate the result using Chinese Remainder Theorem
result = chinese_remainder_theorem(n, a)
print(f"The solution to the system of congruences is: {result}")

def run_practical_4():
    # Add code for Practical 1
    print("Running Practical 1")
