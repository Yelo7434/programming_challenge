# Create a program that ask user to input 10 numbers. Display all numbers that have duplicate.
# Create an empty list to store the numbers.
# Loop to get user input until the user has entered 10 numbers.
# If the input is a number, add it to the list.
numbers = []
while len(numbers) < 10:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number.")

# Find and display duplicate numbers
duplicates = []
for n in numbers:
    if numbers.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

if duplicates:
    print("Duplicate numbers:", duplicates)
else:
    print("No duplicate numbers.")