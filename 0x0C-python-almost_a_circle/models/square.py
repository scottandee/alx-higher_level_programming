#!/usr/bin/python3
"""
This modeule contains the Square class
that inherits from the Rectangle class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This is the Square class that inherits from the Rectangle class"""

    def __init__(self, size, x=0, y=0, id=None):
        """
        This method runs when a new instance
        of the square class is created
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """This prints out the string representation of the Square object"""

        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """This returns the size of the square instance"""

        return self.width

    @size.setter
    def size(self, value):
        """This sets the size of the square instance"""

        self.height = value
        self.width = value

    def update(self, *args, **kwargs):
        """This updates the values of the instance attributes"""

        if not args and kwargs:
            for key in kwargs:
                if key == "size":
                    self.size = kwargs[key]
                if key == "id":
                    self.id = kwargs[key]
                if key == "x":
                    self.x = kwargs[key]
                if key == "y":
                    self.y = kwargs[key]
        else:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[i]
                if i == 1:
                    self.size = args[i]
                if i == 2:
                    self.x = args[i]
                if i == 3:
                    self.y = args[i]

    def to_dictionary(self):
        """Returns the square representation of a Square instance"""

        dic = {'id': self.id, 'size': self.size,
               'x': self.x, 'y': self.y}
        return dic
