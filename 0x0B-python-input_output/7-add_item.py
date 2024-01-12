#!/usr/bin/python3
'''Add all arguments to a Python list and save them to a file.'''
import sys
from json import dump, load

if __name__ == "__main__":
    # Load existing items from the JSON file or create an empty list
    try:
        with open("add_item.json", 'r', encoding="utf-8") as file:
            items = load(file)
    except FileNotFoundError:
        items = []

    # Extend the list with command line arguments (excluding the script name)
    items.extend(sys.argv[1:])

    # Save the updated list to the JSON file
    with open("add_item.json", 'w', encoding="utf-8") as file:
        dump(items, file)
