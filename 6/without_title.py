# title() makes all first letter of each word in the string, capital letter. And all other letter in small case. Create a program that do the same functionality without using title() function.
def custom_title(s):
    result = ""
    capitalize_next = True
    for char in s:
        if char == ' ':
            result += char
            capitalize_next = True
        elif capitalize_next:
            result += char.upper()
            capitalize_next = False
        else:
            result += char.lower()
    return result