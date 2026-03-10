# Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.

# Loop to get user input 10 numbers and store them in the list.
numbers = []
for i in range(10):
    num = int(input("Enter a number: "))
    numbers.append(num)
# Create an empty list to store the numbers.
unique_numbers = []
for num in numbers:
    if numbers.count(num) == 1:
        unique_numbers.append(num)
# Print the list of numbers that don't have duplicate.
print(unique_numbers)