from . import constants
import simple_equ.algebra.algebra as algebra

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

def _tan_rad(rad: float):
    # Newton's method for arctan(x) is derived as the root of tan(theta) - x = 0
    # This derivation assumes theta is in radians.
    # sin and cosin take degrees, so we convert rad to deg.
    return sin(rad * 180 / constants.pi) / cosin(rad * 180 / constants.pi)

def arctan(x: float | int, iter=20): 
    """
    [Summary]: Tests and explanation for the arctan() function.

    [Description]:
    This file contains notes and explanations for the custom `arctan()` function,
    which computes the inverse tangent (arctangent) of a number or ratio. 
    The function returns the angle (in radians) whose tangent is the given input.
    [Usage]:
    - Call arctan(x) with a single float input to get the angle in radians.
    - Can be used to convert a tangent ratio (opposite/adjacent) to an angle in triangles.
    - Can be extended to degrees by multiplying result by 180/π.
    """
    if x > 1:
        return constants.pi / 2 - arctan(1 / x, iter)
    if x < -1:
        return -constants.pi / 2 - arctan(1 / x, iter)

    theta = 0.0 
    for _ in range(iter):
        # f(theta) = tan(theta) - x
        # f'(theta) = 1 + tan(theta)^2
        # Note: Newton's method for tan(theta) = x is stable for theta in (-pi/4, pi/4)
        # which corresponds to x in [-1, 1].
        theta = theta - (_tan_rad(theta) - x) / (1 + _tan_rad(theta)**2)
    return theta


def arctan2(x: float | int, y: float | int) -> float:
    """[Summary]: Return the angle in radians between the positive x-axis and the
    point (x, y), computed as a two-argument arctangent.

    [Description]: Unlike arctan(y/x), arctan2 takes both the sign of y and x
    into account to determine the correct quadrant of the resulting angle.
    The return value is in the range (-π, π].

    [Usage]: Typical usage example:

        result = arctan2(1, 1)   # returns π/4 (first quadrant)
        result = arctan2(1, -1)  # returns 3π/4 (second quadrant)
        print(result)
    """
    if x > 0:
        return arctan(y / x)
    if x < 0 and y >= 0:
        return arctan(y / x) + constants.pi
    if x < 0 and y < 0:
        return arctan(y / x) - constants.pi
    if x == 0 and y > 0:
        return constants.pi / 2
    if x == 0 and y < 0:
        return -constants.pi / 2
    # x == 0 and y == 0: undefined, match math.atan2 behaviour
    return 0.0

def arcsin(x: float | int) -> float:
    """[Summary]: Return the arcsine of x in radians.

    [Description]: Computes the inverse sine by delegating to arctan2 with
    x and sqrt(1 - x²) as arguments, exploiting the identity
    arcsin(x) = arctan2(x, sqrt(1 - x²)). Input must satisfy -1 <= x <= 1.

    [Usage]: Typical usage example:

        result = arcsin(0.5)
        print(result)  # ~0.5236 (π/6)
    """
    result = arctan2(x, algebra.sqrt(1 - x**2))
    return result


def arccos(x: float | int) -> float:
    """[Summary]: Return the arccosine of x in radians.

    [Description]: Derives the inverse cosine from arcsin using the
    complementary-angle identity arccos(x) = π/2 - arcsin(x).
    Input must satisfy -1 <= x <= 1; the result lies in [0, π].

    [Usage]: Typical usage example:

        result = arccos(0.5)
        print(result)  # ~1.0472 (π/3)
    """
    result = constants.pi / 2 - arcsin(x)
    return result