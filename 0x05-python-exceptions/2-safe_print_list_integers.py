#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed_count = 0
    try:
        for index in range(x):
            # Attempt to print only integers using "{:d}".format()
            value = my_list[index]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                printed_count += 1
    except (TypeError, ValueError, IndexError):
        pass
    print()
    return printed_count
