# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Check for division by zero
if num2 != 0:
    result = num1 / num2
    print("The result of division is:", result)
else:
    print("Error: Division by zero is not allowed")
