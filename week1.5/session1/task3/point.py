# Week 1.5, Session 1: Task 3
import math

class Point:
    """
    A Point in 2D space.
    """

    # Add constructor here
    def __init__(self, x_coordinate, y_coordinate):
        """
        Creates a Point, given x & y coordinates.
        """
        self.x = x_coordinate
        self.y = y_coordinate

    # Add distance() method here
    def distance(self):
        """
        Calculates the distance from the origin (0, 0) to the point.
        """
        return math.hypot(self.x, self.y)

    # Add distance_to() method here
    # (This will need a parameter representing another point)
    def distance_to(self, other_point):
        """
        Calculates the distance from this point to another point.
        """
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

# Finally, add code here to demonstrate use of Point
p1 = Point(3, 10)
p2 = Point(0, 4)

print(f"Distance from origin to p1: {p1.distance()}")
print(f"Distance from p1 to p2: {p1.distance_to(p2)}")
