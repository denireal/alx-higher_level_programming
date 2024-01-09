#!/usr/bin/python3
"""
Base class for geometry-related operations.
"""


class BaseGeometry:
    """The base geometry."""

    def area(self):
        """
        Abstract method to be implemented by subclasses.

        Raises:
            Exception: This method should be implemented in subclasses.
        """
        raise Exception("area() is not implemented")
