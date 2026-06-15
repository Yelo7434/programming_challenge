# Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
numbers = []
while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        break
    numbers.append(int(user_input))
if numbers:
    print(f"Average: {sum(numbers) / len(numbers)}")