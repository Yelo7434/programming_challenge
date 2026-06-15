# removeprefix() remove the characters at the beginning of the string that matches the function parameter. Create a program that do the same functionality without using removeprefix() function.
def custom_removeprefix(s, prefix):
    if s[:len(prefix)] == prefix:
        return s[len(prefix):]
    return s