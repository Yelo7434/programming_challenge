# removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.
def custom_removesuffix(s, suffix):
    if s.endswith(suffix): # Assuming standard endswith is allowed; otherwise use s[-len(suffix):] == suffix
        return s[:-len(suffix)]
    return s