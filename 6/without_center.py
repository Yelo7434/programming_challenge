# center() add space characters at the beginning and at the end of the string to print the string at the center. Create a program that do the same functionality without using center() function.
def custom_center(s, width):
    if len(s) >= width:
        return s
    pad = (width - len(s)) // 2
    return (' ' * pad) + s + (' ' * (width - len(s) - pad))