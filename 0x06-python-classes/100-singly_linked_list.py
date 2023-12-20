#!/usr/bin/python3


"""Linked List Module.

This module contains classes to represent a linked list.

Example Usage:

    from my_module import Node, SinglyLinkedList

    # Create a linked list and insert nodes
    linked_list = SinglyLinkedList()
    linked_list.sorted_insert(5)
    linked_list.sorted_insert(3)
    linked_list.sorted_insert(8)

    # Print the linked list
    print(linked_list)

Classes:
    Node: Represents a node in the linked list.
    SinglyLinkedList: Represents a singly linked list.
"""


class Node:
    """Represents a node in the linked list.

    Attributes:
        data (int): The data stored in the node.
        next_node (Node): The next node in the linked list.
    """

    def __init__(self, data, next_node=None):
        """Initializes a node with the given data and next node."""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """Gets the data stored in the node.

        Returns:
            int: The data in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """Sets the data in the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Gets the next node in the linked list.

        Returns:
            Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Sets the next node in the linked list.

        Args:
            value (Node): The new next node.

        Raises:
            TypeError: If the value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list.

    Attributes:
        head (Node): The head of the linked list.
    """

    def __init__(self):
        """Initializes an empty singly linked list."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the linked list in sorted order.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (int): The new value to insert.
        """
        new_node = Node(value)
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Converts the linked list to a string for printing.

        Returns:
            str: A string representation of the linked list.
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(values)
