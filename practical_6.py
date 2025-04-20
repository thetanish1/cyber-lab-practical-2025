#euclier totient function code
def gcd(a, b):
    # Function to calculate the greatest common divisor of a and b
    while b:
        a, b = b, a % b
    return a

def euler_totient(n):
    result = n  # Start with the value of n
    p = 2
    
    # Try all integers from 2 to sqrt(n) to find prime factors
    while p * p <= n:
        # If p is a divisor of n, then it's a prime factor
        if n % p == 0:
            # Subtract multiples of p from result
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1

    # If n is still greater than 1, then n itself is a prime number
    if n > 1:
        result -= result // n
    
    return result

# Example usage
n = int(input("Enter a number to find its Euler's Totient Function: "))
phi_n = euler_totient(n)
print(f"Euler's Totient Function value for {n} is: {phi_n}")

def run_practical_6():
    # Add code for Practical 1
    print("Running Practical 1")
