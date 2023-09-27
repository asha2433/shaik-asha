# Initialize an empty history list to store calculations
history = []

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

while True:
    print("Options:")
    print("Enter 'add' for addition")
    print("Enter 'subtract' for subtraction")
    print("Enter 'multiply' for multiplication")
    print("Enter 'divide' for division")
    print("Enter 'history' to show calculation history")
    print("Enter 'exit' to end the program")
    
    user_input = input(": ")

    if user_input == "exit":
        break
    elif user_input == "history":
        for item in history:
            print(item)
    elif user_input in ["add", "subtract", "multiply", "divide"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if user_input == "add":
            result = add(num1, num2)
        elif user_input == "subtract":
            result = subtract(num1, num2)
        elif user_input == "multiply":
            result = multiply(num1, num2)
        elif user_input == "divide":
            result = divide(num1, num2)
        print("Result:", result)
        history.append(f"{num1} {user_input} {num2} = {result}")
    else:
        print("Invalid input. Please try again.")
