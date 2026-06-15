# Create a program that ask the user to input their fullname in incorrect casing. Print the input in snake case.
fullname = input("Enter fullname: ")
# Convert to lower, split by spaces, and join with underscores
print("_".join(fullname.lower().split()))