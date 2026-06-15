# Create a program that ask the user to input a complete statement. Print the number of words in the input.
statement = input("Enter a statement: ")
words = statement.split()
print(len(words))