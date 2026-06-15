# endswith() check if the string end part matches the function parameter. Create a program that do the same functionality without using endswith() function.
def custom_endswith(s, suffix):
    return s[-len(suffix):] == suffix