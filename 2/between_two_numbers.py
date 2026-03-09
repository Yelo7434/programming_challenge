# Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.
# Get user input two numbers.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
# Compare the two numbers and print all the numbers between them.
if num1 < num2:
    for i in range(num1 + 1, num2):
        print(i)
elif num1 > num2:
    for i in range(num2 + 1, num1):
        print(i)
else:
    print("The numbers are equal. There are no numbers between them.")
