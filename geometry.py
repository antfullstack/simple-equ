import math
import constants
import algebra

def pythagoras(a, b):
    result = a*a + b*b
    hypotenuse = math.sqrt(result)
    return hypotenuse

def square_area(a):
    return a*a

def cube_area(a):
    return a*a*a

def rectangle_area(a, b):
    return a*b

def circle_area(radius):
    return constants.pi * (radius ** 2)

def trapezoid_area(base_one, base_two, height):
    return (base_one + base_two) / 2 * height

def triangle_area(base, height):
    return (base * height) / 2

def pyramid_surface(length, width, height):
    result = length * width + length * math.sqrt((width/2) * (width/2) + height * height) + width * math.sqrt((length/2) * (length/2) + height*height)
    return result

def pyramid_volume(height, length, width):
    return (length * width * height) / 3

def calculate_radius(diameter):
    return diameter / 2

def circumference(radius):
    return 2 * constants.pi * radius

#Attempt to calculate sin using the Taylor Series expansion
#sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def sin(angle):
    # Convert degrees to radians and make angle sensible size
    angle = angle % 360
    radians = angle * constants.pi / 180
    result = 0
    for i in range(10): # 10 terms for good precision
        sign = (-1) ** i
        exponent = 2 * i + 1
        result += sign * (radians ** exponent) / algebra.factorial(exponent)
    return result

def sin(angle):
    # Reduce angle to [-pi, pi]
    x = (angle % 360) * math.pi / 180
    if x > algebra.pi:
        x -= 2 * algebra.pi
    
    term = x  # first term
    result = x
    i = 1
    while True:
        term *= -x*x / ((2*i)*(2*i+1))
        if abs(term) < 1e-15:
            break
        result += term
        i += 1
    return result
