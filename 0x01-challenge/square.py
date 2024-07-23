#!/usr/bin/python3

class Square:
    """
    A class representing a square shape.

    Attributes:
    - size: The size of the square's sides.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
        - size: The size of the square's sides.
        """
        self.size = size

    def area_of_my_square(self):
        """
        Calculates the area of the square.

        Returns:
        The area of the square.
        """
        return self.size ** 2

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.

        Returns:
        The perimeter of the square.
        """
        return self.size * 4

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        A string representation of the square in the format 'size/size'.
        """
        return "{}/{}".format(self.size, self.size)


if __name__ == "__main__":
    s = Square(size=12)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
