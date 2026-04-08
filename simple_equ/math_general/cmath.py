def complex_num(real_part, imagineary_part=0):
    """[Summary]: Create a complex number represented as a tuple.

    [Description]: Returns a tuple in the form (real, imaginary) so other helper
    functions in this module can perform arithmetic on a lightweight complex
    number representation.

    [Usage]: Typical usage example:

        result = complex_num(3, 4)
        print(result)
    """
    return (real_part, imagineary_part)


def add(a, b):
    """[Summary]: Add two tuple-based complex numbers.

    [Description]: Adds the real components together and the imaginary
    components together, then returns the resulting complex tuple.

    [Usage]: Typical usage example:

        result = add((1, 2), (3, 4))
        print(result)
    """
    return (a[0] + b[0], a[1] + b[1])


def sub(a, b):
    """[Summary]: Subtract one tuple-based complex number from another.

    [Description]: Subtracts the real and imaginary components independently and
    returns the resulting complex tuple.

    [Usage]: Typical usage example:

        result = sub((5, 4), (1, 2))
        print(result)
    """
    return (a[0] - b[0], a[1] - b[1])


def mul(a, b):
    """[Summary]: Multiply two tuple-based complex numbers.

    [Description]: Applies the standard complex multiplication formula to the
    provided tuple-based values and returns the resulting real and imaginary
    parts as a tuple.

    [Usage]: Typical usage example:

        result = mul((1, 2), (3, 4))
        print(result)
    """
    real = a[0] * b[0] - a[1] * b[1]
    imag = a[0] * b[1] + a[1] * b[0]
    return (real, imag)


def magnitude(a):
    """[Summary]: Return the magnitude of a tuple-based complex number.

    [Description]: Computes the Euclidean norm of the real and imaginary parts
    by taking the square root of the sum of their squares.

    [Usage]: Typical usage example:

        result = magnitude((3, 4))
        print(result)
    """
    return (a[0] ** 2 + a[1] ** 2) ** 0.5
