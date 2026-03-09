# Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
# Initialize a variable to keep track of the current number.
num = 0
# Loop through numbers from 0 to 100 and print the odd numbers.
while num <= 100:
    if num % 2 != 0:
        print(num)
    num += 1