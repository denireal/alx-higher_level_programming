#!/usr/bin/python3

class LockedClass:
    """
    A class that restricts the creation of new instance attributes,
    except for 'first_name'.
    """
    __slots__ = ['first_name']


    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError
        (f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name != 'first_name':
            raise AttributeError
        (f"'LockedClass' object has no attribute '{name}'")
