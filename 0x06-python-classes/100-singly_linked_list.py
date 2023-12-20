#!/usr/bin/python3

"""
This script defines two classes: Node and SinglyLinkedList.
Node represents a node in a singly-linked list.
SinglyLinkedList represents a singly-linked list.
"""



class Node:
    def __init__(self, data, next_node=None):
        """
        Constructor method to initialize a Node.

        Parameters:
        - data: The data value of the node.
        - next_node (Node): The next node in the linked list
		- (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Property to get the data value of the node.

        Returns:
        int: The data value.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Property setter to set the data value of the node.

        Parameters:
        - value (int): The new data value.

        Raises:
        - TypeError: If the value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Property to get the next node in the linked list.

        Returns:
        Node: The next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Property setter to set the next node in the linked list.

        Parameters:
        - value (Node): The next node.

        Raises:
        - TypeError: If the value is not a Node object or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object or None")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        """
        Constructor method to initialize a SinglyLinkedList.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new node with the given value into the sorted linked list.

        Parameters:
        - value: The value to be inserted.
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
        """
        Return a string representation of the linked list.

        Returns:
        str: String representation of the linked list.
        """
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return '\n'.join(values)
