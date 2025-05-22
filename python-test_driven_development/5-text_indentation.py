#!/usr/bin/python3
"""Module to print text with indentation after certain characters."""

def text_indentation(text):
    """Prints text with 2 new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to format.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    current_line = []
    skip_spaces = False

    for char in text:
        if skip_spaces and char == ' ':
            continue
        skip_spaces = False

        current_line.append(char)
        if char in ('.', '?', ':'):
            print(''.join(current_line).strip())
            print()
            current_line = []
            skip_spaces = True

    if current_line:
        print(''.join(current_line).strip(), end='')