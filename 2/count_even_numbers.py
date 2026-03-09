# Create a program that ask user to input 10 numbers. Print how many are even numbers.
# Initialize a counter for even numbers.
even_count = 0
# Get user input for 10 numbers.
numbers = []
for i in range(10):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num) 
    # Check if the number is even and increment the counter if it is.
    if num % 2 == 0:
        even_count += 1
# Convert the input to integers and store them in a list. Initialize an empty list to store the numbers.
print("The number of even numbers is:", even_count)