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
    prod = 1
    for ni in n:
        prod *= ni  

    result = 0
    for ni, ai in zip(n, a):
        p = prod // ni  
        inv = mod_inverse(p, ni)  
        result += ai * inv * p  

    return result % prod  

n = list(map(int, input("Enter moduli (space-separated): ").split()))
a = list(map(int, input("Enter remainders (space-separated): ").split()))

result = chinese_remainder_theorem(n, a)
print(f" Practical no 4: \nThe solution to the system of congruences is: {result}")

def run_practical_4():
    print("Running Practical 1")
