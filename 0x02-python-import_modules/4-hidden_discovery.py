#!/usr/bin/python3
"""
4-hidden_discovery.py - Program to print non-hidden names from a module.

This program imports a module named hidden_4 and prints all non-hidden names
in the module.

"""


import hidden_4

if __name__ == "__main__":
    # Iterate over all attributes in the hidden_4 module
    for module_attribute in dir(hidden_4):
        # Check if the attribute is not hidden (doesn't start with '__')
        if not module_attribute.startswith("__"):
            # Print the non-hidden attribute name
            print(module_attribute)
