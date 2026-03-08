# Create a program that ask user to input 10 numbers. Print the sum of all the numbers.\

# Initialize a variable to store the sum of the numbers.
total_sum = 0
# Get user input for 10 numbers and calculate the sum.
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    total_sum += num
# Loop through a range of 10 to get 10 numbers from the user.
# Print the final sum of the numbers.
