#!/usr/bin/python3
"""Class to create student instances."""


class Student:
    """Class to create student instances."""

    def __init__(self, first_name, last_name, age):
        """Special method to initialize."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Method that returns a dictionary description.

        Args:
            attrs (list): A list of attribute names.

        Returns:
            dict: A dictionary containing the specified attributes.
        """
        obj = self.__dict__.copy()

        if isinstance(attrs, list):
            d_list = {}

            for attr in attrs:
                if not isinstance(attr, str):
                    return obj

            for attr in attrs:
                if attr in obj:
                    d_list[attr] = obj[attr]

            return d_list

        return obj
