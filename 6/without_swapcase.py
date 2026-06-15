# swapcase() reverse the casing of each of the character of the string. Create a program that do the same functionality without using swapcase() function.
def custom_swapcase(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result