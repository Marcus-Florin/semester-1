# Week 1.6, Session 1: Task 3

import math
from point import Point

VALID_COLOURS = {"red", "orange", "yellow", "green", "blue", "purple"}


class Shape:
    """
    Superclass for different types of shape.
    """

    def __init__(self, position, colour="red"):
        """
        Creates a shape with the specified position & colour.
        """
        self.set_position(position)
        self.set_colour(colour)

    def set_position(self, position):
        """
        Moves this shape to the given position.
        """
        if not isinstance(position, Point):
            raise TypeError("position must be a Point")

        self.position = position

    def set_colour(self, colour):
        """
        Sets this shape's colour to the given colour.
        """
        if colour not in VALID_COLOURS:
            raise ValueError(f"invalid color: must be one of {VALID_COLOURS}")

        self.colour = colour


# Implement your Circle class here
# Make sure that it inherits properly from Shape!

class Circle(Shape):
    """
    Creates a circle with a given position, colour, and radius.
    """

    def __init__(self, position, colour, radius):
        """
        Creates a circle with a given position, colour, and radius.
        """
        super().__init__(position, colour) 

        self.set_radius(radius)

    def set_radius(self, radius):
        """
        Sets the radius of the circle to the given radius.
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("Supplied value must be a number")

        if radius <= 0:
            raise ValueError("Supplied value must be greater than zero")

        self.radius = radius

    def __str__(self):
        """
        Formats string output as required
        """
        return f"{self.colour} circle, radius {self.radius}, at {self.position}"

    def area(self):
        """
        Calculates and returns the area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Calculates and returns the perimeter of the circle.
        """
        return 2 * math.pi * self.radius