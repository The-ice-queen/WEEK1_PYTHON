def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    elif operation == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
    else:
        print("Invalid operation selected.")

if __name__ == "__main__":
    calculator()