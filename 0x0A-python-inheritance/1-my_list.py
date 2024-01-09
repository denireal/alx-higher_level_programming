#!/usr/bin/python3
"""
Custom list class that inherits from the built-in list class.
"""


class MyList(list):
    """
    Attributes:
        Inherits all attributes and methods from the list class.

    Methods:
    print_sorted(self): Print the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the elements of the list in sorted order.

        Args:
            self: The MyList object.

        Returns:
            None
        """
        new_list = sorted(self)
        print("{}".format(new_list))
