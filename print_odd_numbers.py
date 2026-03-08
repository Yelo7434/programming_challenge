# Create a program that ask user to input 10 numbers. Print how many are odd numbers.

# Initialize a counter for odd numbers.
odd_count = 0
# Get user input for 10 numbers and count how many are odd.
# Loop through a range of 10 to get 10 numbers from the user.
for i in range(10):
    num = float(input(f"Enter number {i + 1}: "))
    if num % 2 != 0:
        odd_count += 1  
# Print the final count of odd numbers.
print(f"The number of odd numbers entered is {odd_count}")