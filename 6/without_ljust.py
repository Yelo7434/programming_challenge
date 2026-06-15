# ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using ljust() function.
def custom_ljust(s, width):
    if len(s) >= width:
        return s
    return s + (' ' * (width - len(s)))