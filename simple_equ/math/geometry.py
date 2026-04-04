import simple_equ.math.algebra as algebra
import simple_equ.constants.constants as constants

def pythagoras(a: int | float, b: int | float) -> float:
    result = a*a + b*b
    hypotenuse = algebra.sqrt(result)
    return hypotenuse

def square_area(a: int | float):
    return a*a

def cube_area(a: int | float):
    return a*a*a

def rectangle_area(a: int | float, b: int | float):
    return a*b

def circle_area(radius: int | float) -> float:
    return constants.pi * (radius ** 2)

def trapezoid_area(base_one: int | float, base_two: int | float, height: int | float):
    return (base_one + base_two) / 2 * height

def triangle_area(base: int | float, height: int | float):
    return (base * height) / 2

def pyramid_surface(length: int | float, width: int | float, height: int | float):
    result = length * width + length * algebra.sqrt((width/2) * (width/2) + height * height) + width * algebra.sqrt((length/2) * (length/2) + height*height)
    return result

def pyramid_volume(height: int | float, length: int | float, width: int | float):
    return (length * width * height) / 3

def calculate_radius(diameter: int | float):
    return diameter / 2

def circumference(radius: int | float):
    return 2 * constants.pi * radius

def distance(a: tuple | list | list, b: tuple | list | list) -> float:
    # Convert any lists to tuples
    a, b = tuple(a), tuple(b)
    
    if not all(isinstance(x, tuple) for x in (a, b)):
        raise TypeError("Must input tuples or lists as coordinates for points")
            
    if len(a) == 2 and len(b) == 2:    
        formula = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)
        result = algebra.sqrt(formula)
        return result
    elif len(a) == 3 and len(b) == 3:
        formula = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)
        result = algebra.sqrt(formula)
        return result   
    raise ValueError("Inputs must be either 2d or 3d coordinates")

#Attempt to calculate sin using the Taylor Series expansion
#sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def sin(angle: int | float):
    # Convert degrees to radians and make angle sensible size
    angle = angle % 360
    radians = angle * constants.pi / 180
    result = 0
    for i in range(10): # 10 terms for good precision
        sign = (-1) ** i
        exponent = 2 * i + 1
        result += sign * (radians ** exponent) / algebra.factorial(exponent)
    return result

def cosin(angle: int | float):
    angle = angle % 360
    #Sign is dependant on tshe angle
    if angle >= 0 and angle < 90 or angle >= 270 and angle <= 360:
        cosine = algebra.sqrt(1- sin(angle) * sin(angle))
    elif angle >= 90 and angle < 180 or angle >= 180 and angle < 270:
        cosine = -1 * algebra.sqrt(1- sin(angle) * sin(angle))
    return cosine

def tan(angle: int | float):
    return sin(angle) / cosin(angle)

def sphere_surface(radius: int | float):
    return 4 * constants.pi * radius**2

def slope(point_one: tuple, point_two: tuple) -> float:
    # Ensure points are 2D coordinates
    if len(point_one) != 2 or len(point_two) != 2:
        raise ValueError("Points must be 2D coordinates")
    return (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])
