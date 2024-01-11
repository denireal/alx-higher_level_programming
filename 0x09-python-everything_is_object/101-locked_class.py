#!/usr/bin/python3

class LockedClass:
    """
    A class demonstrating the use of __slots__ to restrict attribute creation.

    Attributes:
        first_name (str): A string representing the first name of an instance
    """

    __slots__ = ["first_name"]

    def __init__(self, first_name=""):
        """
        Initializes a LockedClass instance.

        Parameters:
            first_name (str): The first name to be assigned.
        """
        self.first_name = first_name
