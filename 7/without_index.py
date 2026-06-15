# index() return the first location of the function parameter in the string. Create a program that do the same functionality without using index() function.
def custom_index(s, sub):
    sub_len = len(sub)
    for i in range(len(s) - sub_len + 1):
        if s[i:i + sub_len] == sub:
            return i
    raise ValueError("substring not found")