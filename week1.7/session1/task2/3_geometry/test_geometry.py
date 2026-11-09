# Week 1.7, Session 1: Task 2 - unit tests for the methods in Point and Circle

from geometry import Point, Circle
import math

def test_point_constructor():
    p = Point(5, -2)
    assert p.x == 5
    assert p.y == -2

def test_point_distance():
    assert Point(0, 0).distance() == 0.0
    assert Point(6, 8).distance() == 10.0
    
def test_point_distance_to():
    p1 = Point(0, 0)
    p2 = Point(3, 4)
    assert p1.distance_to(p2) == 5.0

def test_circle_constructor():
    p = Point(0,0)
    c = Circle(5,p)
    assert c.radius == 5
    assert c.centre == p

def test_circle_area():
    assert round(Circle(5).area(),2) == 78.54
    
def test_circle_perimeter():
    assert Circle(5).perimeter() == 10 * math.pi