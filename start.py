#Simple calculator program

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


selection = input("Select operation (+, -, *, /): ")

if selection == "+":
    result = num1 + num2
elif selection == "-":
    result = num1 - num2
elif selection == "*":
    result = num1 * num2
elif selection == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Division by zero error"
else:
    result = "Invalid operation"

print("Result:", result)