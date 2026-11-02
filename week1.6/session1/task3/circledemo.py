# Week 1.6, Session 1: Task 3

# Write a program here to create a Circle object and test its
# various features, including inherited methods
# (see README.md for more details)

from shapes import Circle
from point import Point

circle = Circle(Point(2,3),"green",5)

print(circle)

print(f"Area is: {circle.area():.3f}")
print(f"Area is: {circle.perimeter():.3f}")

circle.set_position(Point(5,2))

print(circle)

circle.set_colour("red")

print(circle)