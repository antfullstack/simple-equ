import math
import constants

def pythagoras(a, b):
    result = a*a + b*b
    hypotenuse = math.sqrt(result)
    return hypotenuse

def square_area(a):
    return a*a

def rectangle_area(a, b):
    return a*b

def circle_area(radius):
    return constants.pi * (radius ** 2)

def trapezoid_area(base_one, base_two, height):
    return (base_one + base_two) / 2 * height

def triangle_area(base, height):
    return (base * height) / 2