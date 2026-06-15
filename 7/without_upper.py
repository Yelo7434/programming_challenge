# upper() converts all characters of the string into upper case. Create a program that do the same functionality without using upper() function.
def custom_upper(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result