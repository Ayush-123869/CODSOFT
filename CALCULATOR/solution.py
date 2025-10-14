# calculator.py

def calculator():
    """
    A simple calculator that performs basic arithmetic operations
    based on user input.
    """
    print("Welcome to the Simple Calculator! 🧮")
    print("------------------------------------")

    try:
        # Prompt the user for the first number
        num1 = float(input("Enter the first number: "))

        # Prompt the user for the second number
        num2 = float(input("Enter the second number: "))

        # Prompt the user for the operation
        print("\nChoose an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        operation = input("Enter the symbol for your choice (+, -, *, /): ")

        # Perform the calculation based on the chosen operation
        if operation == '+':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif operation == '-':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif operation == '*':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif operation == '/':
            # Handle division by zero error
            if num2 == 0:
                print("\nError! Division by zero is not allowed. ❌")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nInvalid operation selected. Please run the program again. 🙁")

    except ValueError:
        # Handle cases where the input is not a number
        print("\nInvalid input. Please enter valid numbers. 🔢")
    except Exception as e:
        # Handle any other unexpected errors
        print(f"\nAn error occurred: {e}")

# Run the calculator function
if __name__ == "__main__":
    calculator()
