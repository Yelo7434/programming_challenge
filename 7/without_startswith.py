# startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.
def custom_startswith(s, prefix):
    return s[:len(prefix)] == prefix