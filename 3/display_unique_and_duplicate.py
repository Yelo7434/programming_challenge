# Create a program that ask user to input a number, continue asking until the user input is invalid. Display "Unique" after input when the inputted number don't have duplicate. Display "Duplicate" after input when the inputted number have duplicate.

# Create an empty list to store the numbers.
numbers = []
# Loop to get user input until the input is invalid.
# If the input is a number, check if the number is in the list.
# If the number is not in the list, add it to the list and display "Unique".
# If the number is in the list, display "Duplicate".
for i in range(10):
    try:
        num = int(input("Enter a number: "))
        if num not in numbers:
            numbers.append(num)
            print("Unique")
        else:
            print("Duplicate")
    except ValueError:
        print("Invalid input. Please enter a number.")
        break
# Display results