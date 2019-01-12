# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def diamond(height):
    '''Given a height (even integer number of lines)
    returns a string containing an ASCII diamond of said height.
    '''
    lines_left = height
    slash = '/'
    backslash = '\\'

    lines = []

    while lines_left:
        number_of_characters = int(lines_left / 2)
        slashes = slash * number_of_characters
        backslashes = backslash * number_of_characters
        upper_line = (slashes + backslashes).center(height)
        lower_line = (backslashes + slashes).center(height)
        lines.insert(0, upper_line)
        lines.append(lower_line)
        lines_left -= 2

    return '\n'.join(lines)

print(diamond(2))
print(diamond(4))
print(diamond(10))
