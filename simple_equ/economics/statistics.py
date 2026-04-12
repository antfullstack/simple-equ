def average(lst: list | tuple) -> int | float:
    """[Summary]: Return the arithmetic mean of a list or tuple.

    [Description]: Attempts to convert the provided values to integers before
    summing them and dividing by the number of elements. Prints an error message
    when invalid argument types are encountered.

    [Usage]: Typical usage example:

        result = average([1, 2, 3])
        print(result)
    """
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid argument types.")

    num_sum = sum(lst)
    return num_sum / len(lst)


def median(lst: list | tuple) -> int | float:
    """[Summary]: Return the median value of a list or tuple.

    [Description]: Converts the provided values to integers, sorts them, and
    returns the middle element for odd-length inputs or the average of the two
    central elements for even-length inputs.

    [Usage]: Typical usage example:

        result = median([1, 2, 3, 4])
        print(result)
    """
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid argument types.")

    sorted_list = sorted(lst)
    median_index = (len(sorted_list) - 1) // 2

    if len(sorted_list) % 2 == 0:
        return (sorted_list[median_index] + sorted_list[median_index + 1]) / 2
    return sorted_list[median_index]


def percentage(fraction, whole):
    """[Summary]: Convert a fraction and whole value into a percentage.

    [Description]: Divides the fraction by the whole and multiplies the result
    by one hundred. Prints an error message when the provided arguments cannot
    be used in the calculation.

    [Usage]: Typical usage example:

        result = percentage(25, 200)
        print(result)
    """
    try:
        result = fraction / whole * 100
        return result
    except ValueError:
        print("Invalid argument types.")


# OLS Linear Regression - returns slope and intercept of the best fit line for the given x and y data points
def linear_regression(x: list[float] | list[int], y: list[float] | list[int]) -> float:
    """[Summary]: Return the slope and intercept of a simple linear regression.

    [Description]: Converts the input data to floating-point values, validates
    that both sequences have the same length, and computes the ordinary least
    squares slope and intercept for the best-fit line.

    [Usage]: Typical usage example:

        slope, intercept = linear_regression([1, 2, 3], [2, 4, 6])
        print(slope, intercept)
    """
    try:
        x = list(map(float, x))
        y = list(map(float, y))
    except ValueError:
        print("Invalid argument types.")
        return
    if len(x) != len(y):
        print("x and y must have the same length.")
        return
    n = len(x)
    sum_x = sum(x)
    sum_y = sum(y)
    sum_x_squared = sum(xi**2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x**2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept


def probability(favorable_outcomes: int | float, possible_outcomes: int | float) -> float:
    """[Summary]: Return the probability of an event as a float.

    [Description]: Computes the classical probability by dividing the number of
    favorable outcomes by the total number of possible outcomes. Raises a
    ValueError when possible_outcomes is zero or when either argument is
    negative.

    [Usage]: Typical usage example:

        result = probability(1, 6)   # probability of rolling a 4 on a dice
        print(result)                # 0.16666...
    """
    if possible_outcomes == 0:
        raise ValueError("possible_outcomes must be greater than zero")
    if favorable_outcomes < 0 or possible_outcomes < 0:
        raise ValueError("outcomes must be non-negative")
    return favorable_outcomes / possible_outcomes


def dot(x, w):
    """[Summary]: Return the dot product of two equally sized iterables.

    [Description]: Multiplies each pair of aligned elements from the two input
    iterables and returns the sum of all pairwise products.

    [Usage]: Typical usage example:

        result = dot([1, 2, 3], [4, 5, 6])
        print(result)
    """
    return sum(x_i * w_i for x_i, w_i in zip(x, w))
