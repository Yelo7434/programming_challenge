# rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.
def custom_rindex(s, sub):
    sub_len = len(sub)
    for i in range(len(s) - sub_len, -1, -1):
        if s[i:i + sub_len] == sub:
            return i
    raise ValueError("substring not found")