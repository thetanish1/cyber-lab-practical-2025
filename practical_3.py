def run_practical_3(user_input=None):
    try:
        if user_input is None:
            a = int(input(" Practical no 3 \n Enter the first number (a): "))
            b = int(input("Enter the second number (b): "))
        else:
            a, b = map(int, user_input.split(','))

        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        result = gcd(a, b)
        print(f"Practical no 3:\nThe GCD of {a} and {b} is: {result}")

        def extended_gcd(x, y):
            if y == 0:
                return x, 1, 0
            gcd_val, x1, y1 = extended_gcd(y, x % y)
            return gcd_val, y1, x1 - (x // y) * y1

        gcd_result, x, y = extended_gcd(a, b)
        print(f"Practical no 3:\nGCD of {a} and {b} is {gcd_result}")
        print(f"Coefficients x and y are: x = {x}, y = {y}")
        print(f"Verification: {a}*({x}) + {b}*({y}) = {gcd_result}")

    except ValueError:
        print("Invalid input. Please enter integers.")

run_practical_3("30,20") 
