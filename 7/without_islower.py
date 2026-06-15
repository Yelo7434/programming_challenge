# islower() check if all characters of the string is on lower case. Create a program that do the same functionality without using islower() function.
def custom_islower(s):
    has_alpha = False
    for char in s:
        if 'A' <= char <= 'Z':
            return False
        if 'a' <= char <= 'z':
            has_alpha = True
    return has_alpha