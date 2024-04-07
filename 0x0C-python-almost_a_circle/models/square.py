#!/usr/bin/python3
"""A module defining the Square class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Represents a square, which is a special case of a rectangle.
    Inherits from the Rectangle class.

    Attributes:
        size (int): The size (side length) of the square.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): The identifier of the square.
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initializes a Square instance.

        Args:
            size (int): The size (side length) of the square.
            x (int, optional): The x-coordinate of the top-left corner (default is 0).
            y (int, optional): The y-coordinate of the top-left corner (default is 0).
            id (int, optional): The identifier (default is None).
        """
        super().__init__(size, size, x, y, id)
    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
            str: A string in the format '[Square] (id) x/y - size'.
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """
        Gets the size (side length) of the square.

        Returns:
            int: The size of the square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Sets the size (side length) of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If 'value' is not an integer.
            ValueError: If 'value' is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer")
        if value <= 0:
            raise ValueError("Size must be > 0")

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Updates the attributes of the square based on args or kwargs.

        Args:
            *args (list): List of new attribute values in the order (id, size, x, y).
            **kwargs (dict): Dictionary of new attribute values.

        Notes:
            If 'args' is not empty, attributes are updated based on positional order.
            If 'kwargs' is provided, attributes are updated based on key-value pairs.
        """
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attr_names[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """
        Converts the square object to a dictionary representation.

        Returns:
            dict: A dictionary containing the square's attributes.
        """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
