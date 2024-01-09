#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Append a new string after each occurrence of a specified search string
	in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for in each line.
        new_string (str): The string to append after the search string.

    Returns:
        None
    """
    updated_content = ""

    with open(filename, 'r') as file_r:
        for current_line in file_r:
            updated_content += current_line
            if search_string in current_line:
                updated_content += new_string

    with open(filename, 'w') as file_w:
        file_w.write(updated_content)
