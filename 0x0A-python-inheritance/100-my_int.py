#!/usr/bin/python3
"""
Creates a class that inherits from int.
"""


class MyInt(int):
    """The MyInt Class"""

    def __eq__(self, other):
        """
        Override the equality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if not equal, False if equal.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Override the inequality operator.

        Args:
            other: The value to compare with.

        Returns:
            bool: True if equal, False if not equal.
        """
        return super().__eq__(other)
