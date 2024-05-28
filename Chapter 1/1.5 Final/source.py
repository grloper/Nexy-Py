FILE_PATH = r'C:\Users\ofekv\Desktop\Nexy Py\Chapter 1\1.5 Final\names.txt'


# סעיף 1
def get_longest_name():
    """
    Retrieves the longest name from a file.

    Reads the contents of a file specified by `FILE_PATH` and returns the longest name found in the file.

    Returns:
        str: The longest name found in the file.
    """
    # Return the longest name
    print(max(open(FILE_PATH).read().splitlines(), key=len))
# סעיף 2
def get_total_length():
    """
    Calculates and prints the total length of all lines in a file.

    Reads the contents of the file specified by FILE_PATH, splits it into lines,
    and calculates the total length of all lines combined. The result is then printed.

    Note: The FILE_PATH variable should be defined before calling this function.

    Example usage:
    get_total_length()
    """
    # Print the total length of all names
    print(sum(len(name) for name in open(FILE_PATH).read().splitlines()))
# סעיף 3
def get_shortest_names():
    """
    Retrieves the shortest names from a file and prints them.

    Reads the contents of a file specified by `FILE_PATH`, splits the lines into a list,
    sorts the list based on the length of each line, and prints the first two shortest names.

    Args:
        None

    Returns:
        None
    """
    # Print the first two shortest names
    print('\n'.join(sorted(open(FILE_PATH).read().splitlines(), key=len)[:2]))
# סעיף 4
def create_name_length_file():
    """
    Reads names from a file and creates a new file 'name_length.txt' that contains the length of each name.

    Parameters:
    None

    Returns:
    None
    """
    with open(FILE_PATH) as f, open('name_length.txt', 'w') as out:
        # Write the length of each name to the output file
        out.write('\n'.join(str(len(name)) for name in f.read().splitlines()))
# סעיף 5
def get_names_by_length():
    """
    Retrieves names from a file that have a specific length.

    Prompts the user to enter a name length and then reads a file to find names
    that have the specified length. Prints the matching names separated by newlines.

    Args:
        None

    Returns:
        None
    """
    name_length = int(input('Enter name length: '))
    # Print names with the specified length
    print('\n'.join(name for name in open(FILE_PATH).read().splitlines() if len(name) == name_length))


def main():
    get_longest_name() 
    get_total_length()
    get_shortest_names()
    create_name_length_file()
    get_names_by_length()

if __name__ == '__main__':
    main()
