# capitalize() makes the first letter of the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using capitalize() function.
def custom_capitalize(s):
    if not s: return s
    return s[0].upper() + s[1:].lower()
    