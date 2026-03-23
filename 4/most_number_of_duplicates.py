# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number with the most number of duplicate.
# Create an empty list to store the numbers.
# Loop to get user input until the input is invalid.
# If the input is a number, add it to the list.
# If the input is invalid, break the loop.
# After the loop, check if the list is empty. If it is empty, display "No numbers entered". If it is not empty, find the number with the most number of duplicate and display it.
numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except ValueError:
        print("Invalid input. Please enter a number.")
        break
if not numbers:
    print("No numbers entered.")
else:
    most_duplicates = None
    max_count = 0
    for n in set(numbers):
        count = numbers.count(n)
        if count > max_count:
            max_count = count
            most_duplicates = n
    print("Number with the most duplicates:", most_duplicates)