# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number.

# Create an empty list to store the numbers.
numbers = []
# Loop to get user input until the input is invalid.
# If the input is a number, add it to the list.
# If the input is invalid, break the loop.
# After the loop, check if the list is empty. If it is empty, display "No numbers entered". If it is not empty, display the lowest number in the list.
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
    print("The lowest number is:", min(numbers))