#extended euclideian algorithm

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # gcd, x, y
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Example usage
a = 30
b = 20
gcd, x, y = extended_gcd(a, b)
print(f"GCD of {a} and {b} is {gcd}")
print(f"Coefficients x and y are: x = {x}, y = {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")


#Extended Euclidean Algorithm with User Input
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0  # gcd, x, y
    else:
        gcd, x1, y1 = extended_gcd(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

# Taking user input for the two numbers
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))

# Find GCD and coefficients
gcd, x, y = extended_gcd(a, b)

# Display results
print(f"GCD of {a} and {b} is {gcd}")
print(f"Coefficients x and y are: x = {x}, y = {y}")
print(f"Verification: {a}*({x}) + {b}*({y}) = {a*x + b*y}")
