# Worksheet 1.5: Rectangle Class

class Rectangle:
    """
    A rectangle, with a width and a height.
    """
    def __init__(self, width, height):
        """
        Creates a Rectangle, given values for width and height.
        """

        #Check for integer input and positive values for width and height
        if not isinstance(width, int) and not isinstance(height, int):
            raise TypeError("Width and height must be integers.")
        
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        
        self.width = width
        self.height = height

    def is_square(self):
        """
        Returns True if the rectangle is a square.
        """
        if self.width == self.height:
            return True
        else:
            return False

    def area(self):
        """
        Returns the area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)