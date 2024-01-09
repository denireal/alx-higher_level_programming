#!/usr/bin/python3
"""
Add attribute to an object if possible.
"""


def add_attribute(an_obj, an_attr, a_value):
    """
    Add an attribute to an object if possible.

    Args:
        an_obj: The object to which the attribute will be added.
        an_attr (str): The name of the attribute.
        a_value: The value of the attribute.

    Raises:
        TypeError: If the attribute cannot be added to the object.
    """
    if not hasattr(an_obj, '__slots__') and not hasattr(an_obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(an_obj, '__slots__') and not hasattr(an_obj, an_attr):
        raise TypeError("can't add new attribute")

    setattr(an_obj, an_attr, a_value)
