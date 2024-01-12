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
        if attrs is None:
            return self.__dict__.copy()

        return {
                attr: getattr(self, attr, None)
                for attr in attrs if isinstance(attr, str)
                }

    def reload_from_json(self, json):
        """
        Method that updates instance attributes from a JSON-formatted dict.

        Args:
            json (dict): A dictionary containing attribute-value pairs.

        Returns:
            None
        """
        for attr, value in json.items():
            setattr(self, attr, value)
