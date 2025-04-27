def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    result = n  
    p = 2
    
    while p * p <= n:
        if n % p == 0:
            # Subtract multiples of p from result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    if n > 1:
        result -= result // n
    
    return result

n = int(input("Enter a number to find its Euler's Totient Function: "))
phi_n = euler_totient(n)
print(f"Practical no 6: \nEuler's Totient Function value for {n} is: {phi_n}")

def run_practical_6():
    print("Running Practical 6")
