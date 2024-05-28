def is_funny(string):
    return all(char == 'h' or char == 'a' for char in string)