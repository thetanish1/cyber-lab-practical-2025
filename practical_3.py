def run_practical_3(user_input=None):
    try:
        # If there's no user input, prompt the user for input
        if user_input is None:
            a = int(input("Enter the first number (a): "))
            b = int(input("Enter the second number (b): "))
        else:
            # If there is user input passed from the GUI, use it
            a, b = map(int, user_input.split(','))  # Assuming the user input is comma-separated

        # Calculate GCD
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        result = gcd(a, b)
        print(f"The GCD of {a} and {b} is: {result}")
        
        # You can continue with the rest of the code that uses 'a' and 'b'
        # Example for extended GCD calculation
        def extended_gcd(x, y):
            if y == 0:
                return x, 1, 0
            gcd, x1, y1 = extended_gcd(y, x % y)
            return gcd, y1, x1 - (x // y) * y1

        gcd_result, x, y = extended_gcd(a, b)
        print(f"GCD of {a} and {b} is {gcd_result}")
        print(f"Coefficients x and y are: x = {x}, y = {y}")
        print(f"Verification: {a}*({x}) + {b}*({y}) = {gcd_result}")

    except ValueError:
        print("Please enter valid integers for the numbers.")
        # Optionally, return an error or prompt again for input in the GUI
        return "Invalid input. Please enter integers."

