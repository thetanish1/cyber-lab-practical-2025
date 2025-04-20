
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
num1 = 56
num2 = 98
print("GCD is:", find_gcd(num1, num2))

def run_practical_1():
    print("Running Practical 1")

