# rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.
def custom_rstrip(s):
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
        i -= 1
    return s[:i+1]