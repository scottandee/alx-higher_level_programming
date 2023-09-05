#!/usr/bin/python3
"""This module contains the declaration
of the class Node and SinglyLinkedList
"""


class Node:
    """This is the Node class with which all our
    node objects will be gotten from
    """

    def __init__(self, data, next_node=None):
        """This is the method that runs whenever
        a new Node object is created
        """
        if not isinstance(next_node, Node):
            if next_node is not None:
                raise TypeError("next_node must be a Node object")
        if not isinstance(data, int):
            raise TypeError("data must be an integer")

        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """This method returns the value of the
        private attribute, data
        """
        return self.__data

    @data.setter
    def data(self, value):
        """This method assigns a value to the
        private attribute, data
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """This method returns the value of the
        private attribute, next_node
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This method assigns a value to the
        private attribute, next_node
        """
        if not isinstance(value, Node):
            if value is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """This class defines a singly linked list"""

    def __init__(self):
        """This is the class that runs immediately
        a new object is created
        """
        self.__head = None

    def sorted_insert(self, value):
        """This inserts a new node into the correct
        position in the linked list
        """
        current = self.__head
        node = Node(value)

        if current is None:
            self.__head = node
            return

        while current.next_node is not None:
            if value < current.data and current == self.__head:
                node.next_node = current
                self.__head = node
                return
            if value >= current.data and value < current.next_node.data:
                node.next_node = current.next_node
                current.next_node = node
                return
            current = current.next_node

        node = Node(value)
        current.next_node = node

    def __str__(self):
        """This magic method will run when a SinglyLinkedList
        object is printed
        """
        current = self.__head
        string = ""

        while current is not None:
            string = string + str(current.data)
            if current.next_node is not None:
                string = string + "\n"

            current = current.next_node

        return string
