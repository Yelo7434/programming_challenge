# Create a program that ask user to input 2 numbers. Print the bigger number.

# Get user input for the first number.
num1 = float(input("Enter the first number: "))
# Get user input for the second number.
num2 = float(input("Enter the second number: "))
# Compare the two numbers and print the bigger one.
if num1 > num2:
    print(f"The bigger number is: {num1}")
elif num2 > num1:
    print(f"The bigger number is: {num2}")
else:
    print("Both numbers are equal.")