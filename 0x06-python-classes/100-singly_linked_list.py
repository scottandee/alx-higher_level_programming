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
        if isinstance(next_node, Node):
            if next_node is not None:
                raise TypeError("next_node must be a Node object")
        if isinstance(data, int):
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
        if isinstance(value, int):
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
        if isinstance(value, Node):
            if value is not None:
                raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __repr__(self):
        """This returns the official representation
        of a node
        """
        return "Node(" + str(self.__data) + ', ' + str(self.__next_node) + ")"


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
        self.current = self.__head

        if self.current is None:
            self.__head = eval("Node(" + str(value) + ", None)")
            return

        while self.current.next_node is not None:
            if value < self.current.data:
                self.node = eval("Node(" + str(self.current.data) + ", "
                                 + self.current.next_node.__repr__() + ")")
                self.current.data = value
                self.current.next_node = self.node
                return
            elif value == self.current.data:
                self.node = eval("Node(" + str(value) + ", "
                                 + self.current.next_node.__repr__() + ")")
                self.current.next_node = self.node
                return
            else:
                self.current = self.current.next_node

        self.node = eval("Node(" + str(value) + ", None)")
        self.current.next_node = self.node

    def __str__(self):
        """This magic method will run when a SinglyLinkedList
        object is printed
        """
        self.current = self.__head

        while self.current.next_node is not None:
            print(self.current.data)
            self.current = self.current.next_node
        return str(self.current.data)
