#!/usr/bin/python3

class Square:
    """
    A class representing a square shape.

    Attributes:
    - side: The length of the side of the square.
    """

    def __init__(self, side=0):
        """
        Initializes a square with the given side length.

        Args:
        - side: The length of the side of the square.
        """
        self.side = side

    def area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
        The area of the square.
        """
        return self.side * self.side

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.

        Returns:
        The perimeter of the square.
        """
        return self.side * 4

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        A string representation of the square in the format 'side/side'.
        """
        return "{}/{}".format(self.side, self.side)


if __name__ == "__main__":
    s = Square(side=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
