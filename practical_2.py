#find gcd of two using interactive function

def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Interactive input from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")


#find gcd of two using inrecursive function

def find_gcd(a, b):
    if b == 0:
        return a
    else:
        return find_gcd(b, a % b)

# Interactive input from user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = find_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")

def run_practical_2():
    # Add code for Practical 1
    print("Running Practical 1")
