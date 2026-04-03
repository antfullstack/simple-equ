import constants
import algebra

def pythagoras(a, b):
    result = a*a + b*b
    hypotenuse = algebra.sqrt(result)
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
    result = length * width + length * algebra.sqrt((width/2) * (width/2) + height * height) + width * algebra.sqrt((length/2) * (length/2) + height*height)
    return result

def pyramid_volume(height, length, width):
    return (length * width * height) / 3

def calculate_radius(diameter):
    return diameter / 2

def circumference(radius):
    return 2 * constants.pi * radius

def distance(a: tuple, b: tuple):
    # Convert any lists to tuples
    a, b = [tuple(p) if isinstance(p, list) else p for p in (a, b)]
    
    if all(isinstance(x, tuple) for x in (a, b)):
        if len(a) == 2 and len(b) == 2:    
            formula = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2)
            result = algebra.sqrt(formula)
            return result
        elif len(a) == 3 and len(b) == 3:
            formula = ((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2) + ((a[2] - b[2]) ** 2)
            result = algebra.sqrt(formula)
            return result   
        raise ValueError("Inputs must be either 2d or 3d coordinates")
    raise TypeError("Must input tuples or lists as coordinates for points")

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
    x = (angle % 360) * constants.pi / 180
    if x > constants.pi:
        x -= 2 * constants.pi
    
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

def cosin(angle):
    angle = angle % 360
    #Sign is dependant on tshe angle
    if angle >= 0 and angle < 90 or angle >= 270 and angle <= 360:
        cosine = algebra.sqrt(1- sin(angle) * sin(angle))
    elif angle >= 90 and angle < 180 or angle >= 180 and angle < 270:
        cosine = -1 * algebra.sqrt(1- sin(angle) * sin(angle))
    return cosine

def tan(angle):
    return sin(angle) / cosin(angle)

def sphere_surface(radius):
    return 4 * constants.pi * radius**2
