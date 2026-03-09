# Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point.

# Get user input for the first number.
num1 = float(input("Enter the first number: "))
# Get user input for the second number.
num2 = float(input("Enter the second number: "))
# Calculate the quotient of the two numbers and print the result.
if num2 != 0:
    quotient_result = num1 / num2
    print(f"The quotient of the two numbers is {quotient_result}")
else:
    print("Error: Division by zero is not allowed.")
