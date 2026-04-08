from pathlib import Path
from simple_equ.math_general import algebra
from simple_equ.math_general import constants
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
import algebra
import constants

def pythagoras(a: int | float, b: int | float) -> float:
    """[Summary]: Return the hypotenuse of a right triangle.

    [Description]: Squares the two provided legs, sums them, and uses the local
    square-root helper from the algebra module to compute the hypotenuse.

    [Usage]: Typical usage example:

        result = pythagoras(3, 4)
        print(result)
    """
    result = a * a + b * b
    hypotenuse = algebra.sqrt(result)
    return hypotenuse


def square_area(a: int | float):
    """[Summary]: Return the area of a square.

    [Description]: Multiplies the side length by itself to compute the area of a
    square using the standard geometric formula.

    [Usage]: Typical usage example:

        result = square_area(4)
        print(result)
    """
    return a * a


def cube_area(a: int | float):
    """[Summary]: Return the volume of a cube from one edge length.

    [Description]: Multiplies the edge length by itself three times, matching
    the standard formula for the volume of a cube.

    [Usage]: Typical usage example:

        result = cube_area(3)
        print(result)
    """
    return a * a * a


def rectangle_area(a: int | float, b: int | float):
    """[Summary]: Return the area of a rectangle.

    [Description]: Multiplies the length and width values to compute the area of
    a rectangle.

    [Usage]: Typical usage example:

        result = rectangle_area(4, 6)
        print(result)
    """
    return a * b


def circle_area(radius: int | float) -> float:
    """[Summary]: Return the area of a circle.

    [Description]: Uses the mathematical constant pi from the local constants
    module and the standard formula pi * r^2 to compute the result.

    [Usage]: Typical usage example:

        result = circle_area(5)
        print(result)
    """
    return constants.pi * (radius**2)


def sphere_area(radius: int | float) -> float:     
    return 4 * constants.pi * (radius ** 2)

def trapezoid_area(base_one: int | float, base_two: int | float, height: int | float):
    """[Summary]: Return the area of a trapezoid.

    [Description]: Averages the two base lengths and multiplies that value by
    the height to compute the area of the trapezoid.

    [Usage]: Typical usage example:

        result = trapezoid_area(3, 5, 4)
        print(result)
    """
    return (base_one + base_two) / 2 * height


def triangle_area(base: int | float, height: int | float):
    """[Summary]: Return the area of a triangle.

    [Description]: Multiplies the base by the height and divides the result by
    two to compute the triangle's area.

    [Usage]: Typical usage example:

        result = triangle_area(6, 4)
        print(result)
    """
    return (base * height) / 2


def pyramid_surface(length: int | float, width: int | float, height: int | float):
    """[Summary]: Return the surface area of a rectangular pyramid.

    [Description]: Computes the base area and the triangular side areas, then
    sums them to produce the total surface area of the pyramid.

    [Usage]: Typical usage example:

        result = pyramid_surface(3, 4, 5)
        print(result)
    """
    result = (
        length * width
        + length * algebra.sqrt((width / 2) * (width / 2) + height * height)
        + width * algebra.sqrt((length / 2) * (length / 2) + height * height)
    )
    return result


def pyramid_volume(height: int | float, length: int | float, width: int | float):
    """[Summary]: Return the volume of a rectangular pyramid.

    [Description]: Multiplies the base area by the height and divides the result
    by three to compute the pyramid's volume.

    [Usage]: Typical usage example:

        result = pyramid_volume(6, 4, 3)
        print(result)
    """
    return (length * width * height) / 3


def calculate_radius(diameter: int | float):
    """[Summary]: Return the radius derived from a diameter.

    [Description]: Divides the given diameter by two to convert it into a
    radius.

    [Usage]: Typical usage example:

        result = calculate_radius(10)
        print(result)
    """
    return diameter / 2


def circumference(radius: int | float):
    """[Summary]: Return the circumference of a circle.

    [Description]: Uses the standard formula 2 * pi * r to compute the distance
    around a circle for the provided radius.

    [Usage]: Typical usage example:

        result = circumference(5)
        print(result)
    """
    return 2 * constants.pi * radius


def distance(a: tuple | list | list, b: tuple | list | list) -> float:
    # Convert any lists to tuples
    """[Summary]: Return the Euclidean distance between two 2D or 3D points.

    [Description]: Accepts tuples or lists as coordinates, normalizes them to
    tuples, validates the dimensionality, and computes the Euclidean distance in
    either two or three dimensions.

    [Usage]: Typical usage example:

        result = distance((0, 0), (3, 4))
        print(result)
    """
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


# Attempt to calculate sin using the Taylor Series expansion
# sin(x) = x - x^3/3! + x^5/5! - x^7/7! + ...
def sin(angle: int | float):
    # Convert degrees to radians and make angle sensible size
    """[Summary]: Return the sine of an angle given in degrees.

    [Description]: Normalizes the angle, converts it to radians, and evaluates a
    Taylor series approximation until the current term becomes sufficiently
    small.

    [Usage]: Typical usage example:

        result = sin(30)
        print(result)
    """
    angle = angle % 360
    if angle >= 180:
        angle -= 360

    sign = 1 
    if angle > 90: 
        angle = 180 - angle 
    elif angle < -90: 
        angle = -180 - angle
        sign = -1

    x = angle * constants.pi / 180

    term = x 
    tol =  1e-15
    result = 0.0
    i = 0

    while abs(term) > tol:
        result += term 
        i += 1 
        term *= -x * x / ((2 * i) * (2 * i + 1))

    return sign * result


def cosin(angle: int | float):
    """[Summary]: Return the cosine of an angle given in degrees.

    [Description]: Normalizes the angle and derives the cosine value from the
    sine result while correcting the sign according to the quadrant.

    [Usage]: Typical usage example:

        result = cosin(60)
        print(result)
    """
    angle = angle % 360
    # Sign is dependant on tshe angle
    if angle >= 0 and angle < 90 or angle >= 270 and angle <= 360:
        cosine = algebra.sqrt(1 - sin(angle) * sin(angle))
    elif angle >= 90 and angle < 180 or angle >= 180 and angle < 270:
        cosine = -1 * algebra.sqrt(1 - sin(angle) * sin(angle))
    return cosine


def tan(angle: int | float):
    """[Summary]: Return the tangent of an angle given in degrees.

    [Description]: Computes tangent as the quotient of the module's sine and
    cosine helper functions.

    [Usage]: Typical usage example:

        result = tan(45)
        print(result)
    """
    return sin(angle) / cosin(angle)


def sphere_surface(radius: int | float):
    """[Summary]: Return the surface area of a sphere.

    [Description]: Applies the formula 4 * pi * r^2 to compute the total outer
    surface area of a sphere.

    [Usage]: Typical usage example:

        result = sphere_surface(5)
        print(result)
    """
    return 4 * constants.pi * radius**2


def slope(point_one: tuple, point_two: tuple) -> float:
    """[Summary]: Return the slope between two 2D points.

    [Description]: Validates that both inputs represent two-dimensional points
    and then computes the slope using the change in y over the change in x.

    [Usage]: Typical usage example:

        result = slope((1, 2), (3, 6))
        print(result)
    """
    if len(point_one) != 2 or len(point_two) != 2:
        raise ValueError("Points must be 2D coordinates")
    return (point_two[1] - point_one[1]) / (point_two[0] - point_one[0])
