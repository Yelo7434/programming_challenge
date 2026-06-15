# isupper() check if all characters of the string is on upper case. Create a program that do the same functionality without using isupper() function.
def custom_isupper(s):
    has_alpha = False
    for char in s:
        if 'a' <= char <= 'z':
            return False
        if 'A' <= char <= 'Z':
            has_alpha = True
    return has_alpha