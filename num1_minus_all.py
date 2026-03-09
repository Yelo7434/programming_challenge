# Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
# Get user input for 10 numbers.
numbers = []
for i in range(10):
    # Convert the input to integers and store them in a list. Initialize an empty list to store the numbers.
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num) 
# Calculate the result of the first number minus all of the remaining numbers and print the result.
result = numbers[0]
for num in numbers[1:]:
    result -= num
print("The result of the first number minus all of the remaining numbers is:", result)