#!/usr/bin/python3

class LockedClass:
    """
    A class that restricts the creation of new instance attributes,
    except for 'first_name'.
    """

    def __init__(self, first_name=""):
        """
        Initializes a LockedClass instance.

        Parameters:
            first_name (str): The first name to be assigned.
        """
        self.__dict__['first_name'] = first_name

    def __setattr__(self, name, value):
        """
        Overrides the default setattr method to restrict attribute creation.

        Parameters:
            name (str): The name of the attribute.
            value: The value to be assigned to the attribute.
        """
        if name != 'first_name':
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        self.__dict__[name] = value
