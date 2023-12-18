#!/usr/bin/python3

import sys



def safe_print_integer_err(value):
    try:
        # Attempt to print the integer representation of 'value'
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # Catch exceptions (ValueError or TypeError) and print to stderr
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return False
