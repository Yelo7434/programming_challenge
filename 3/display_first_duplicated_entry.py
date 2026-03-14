# Create a program that ask user to input 10 numbers. Display all numbers. For numbers with duplicate, display only the first entry.

# Loop to get user input 10 numbers and store them in the list.
numbers = [int(input("Enter a number: ")) for i in range(10)]
# List to store numbers without duplicates
result = []
for num in numbers:
    if num not in result:
        result.append(num)
# Display all numbers
print("Numbers without duplicates:", result)