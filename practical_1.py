
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = 56
num2 = 98
print("Practical no 1: \n GCD is:", find_gcd(num1, num2))

def run_practical_1():
    print("Running Practical 1")
