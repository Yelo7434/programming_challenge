# Prog04: Create a program that ask user to input a number, continue asking until the user input is invalid. Display the number from highest to lowest. Clue: sort() function
numbers = []
while True:
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        break
    numbers.append(int(user_input))
numbers.sort(reverse=True)
print(numbers)