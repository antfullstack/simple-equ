import math


def power(base: int | float, exponent: int | float) -> int | float:
    """[Summary]: Raise a base value to a given exponent.

    [Description]: Uses Python's exponentiation operator to compute powers for
    integer or floating-point inputs and returns the resulting numeric value.

    [Usage]: Typical usage example:

        result = power(2, 3)
        print(result)
    """
    return base**exponent


def factorial(number: int | float):
    """[Summary]: Return the factorial of a positive number.

    [Description]: Multiplies the input value by each preceding positive value
    until the running number reaches zero. This implementation follows an
    iterative approach instead of recursion.

    [Usage]: Typical usage example:

        result = factorial(5)
        print(result)
    """
    result = 1
    while number > 0:
        result *= number
        number -= 1
    return result


def gcd(a: int | float, b: int | float):
    """[Summary]: Return the greatest common divisor of two numbers.

    [Description]: Applies the Euclidean algorithm recursively by replacing the
    input pair with the divisor and remainder until the remainder becomes zero.

    [Usage]: Typical usage example:

        result = gcd(48, 18)
        print(result)
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def sqrt(number: int | float):
    """[Summary]: Return the square root of a non-negative number.

    [Description]: Uses Newton's method to iteratively approximate the square
    root until the difference between consecutive estimates falls below a small
    tolerance. Raises a ValueError for negative inputs.

    [Usage]: Typical usage example:

        result = sqrt(25)
        print(result)
    """
    if number > 0:
        x = number
        tolerance = 0.000000000001

        while True:
            next = (x + number / x) / 2

            if abs(next - x) < tolerance:
                return next

            x = next
    elif number == 0:
        return 0
    else:
        raise ValueError("Not a real number")


def cbrt(x):
    """[Summary]: Return the cube root of a real number.

    [Description]: Computes the real cube root while preserving the correct sign
    for negative inputs, which keeps the function aligned with real-number
    arithmetic.

    [Usage]: Typical usage example:

        result = cbrt(27)
        print(result)
    """
    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))


def basic_quadratic(a: int | float, b: int | float, c: int | float):
    """[Summary]: Return the roots of a quadratic equation.

    [Description]: Solves the quadratic equation ax^2 + bx + c = 0 by computing
    the discriminant and applying the quadratic formula to obtain both roots.

    [Usage]: Typical usage example:

        root1, root2 = basic_quadratic(1, -3, 2)
        print(root1, root2)
    """
    d = (b**2) - (4 * a * c)
    sqrt_d = sqrt(d)

    root1 = (-b + sqrt_d) / (2 * a)
    root2 = (-b - sqrt_d) / (2 * a)
    return root1, root2


def basic_qubic(a: int | float, b: int | float, c: int | float, d: int | float):
    """[Summary]: Return the roots of a cubic equation.

    [Description]: Solves a cubic equation using a discriminant-based approach
    and returns either one real root plus two complex roots or three real roots,
    depending on the value of delta.

    [Usage]: Typical usage example:

        result = basic_qubic(1, -6, 11, -6)
        print(result)
    """
    q = (2 * b**3 - 9 * a * b * c + 27 * a * a * d) / (27 * a**3)
    p = (3 * a * c - (b * b)) / (3 * (a * a))

    delta = (q / 2) ** 2 + (p / 3) ** 3

    roots = []

    if delta >= 0:
        sqrt_delta = sqrt(delta)
        t1 = cbrt(-q / 2 + sqrt_delta)
        t2 = cbrt(-q / 2 - sqrt_delta)
        t = t1 + t2

        # Real root
        x1 = t - (b / (3 * a))
        roots.append(x1)

        # 2 Complex roots using cube roots of unity
        omega = complex(-0.5, sqrt(3) / 2)
        x2 = t1 * omega + t2 * omega.conjugate() - (b / (3 * a))
        x3 = t1 * omega.conjugate() + t2 * omega - (b / (3 * a))
        roots.extend([x2, x3])

    else:
        # Three real square roots (trig solution)
        r = sqrt(-p / 3)
        phi = math.acos(-q / (2 * r**3))
        # All real
        x1 = 2 * r * math.cos(phi / 3) - b / (3 * a)
        x2 = 2 * r * math.cos((phi + 2 * math.pi) / 3) - b / (3 * a)
        x3 = 2 * r * math.cos((phi + 4 * math.pi) / 3) - b / (3 * a)
        roots.extend([x1, x2, x3])

    # It just removes the artifacts from floating point innacuracies here
    roots = [round(x, 10) for x in roots]
    return roots


def basic_linear(a: int | float, b: int | float):
    """[Summary]: Return the solution to a basic linear equation.

    [Description]: Solves the equation ax + b = 0 by isolating x and returning
    the result of -b divided by a.

    [Usage]: Typical usage example:

        result = basic_linear(2, -8)
        print(result)
    """
    x = -b / a
    return x


def is_divisible(a: int | float, b: int | float) -> bool:
    # Checks if a is divisible by b by checking if the remainder of a divided by b is 0.
    # Raise ValueError if b is zero.
    """[Summary]: Return whether one number is divisible by another.

    [Description]: Checks whether the remainder of a divided by b is zero. Raises
    a ValueError when the divisor is zero to prevent invalid division.

    [Usage]: Typical usage example:

        result = is_divisible(10, 5)
        print(result)
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a % b == 0
