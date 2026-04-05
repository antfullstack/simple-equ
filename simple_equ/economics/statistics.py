def average(lst: list | tuple) -> int | float:
    """Calculates the average of a list of numbers.

    This function takes a list or tuple of numbers and returns their average.
    It attempts to convert all elements to integers, and handles potential errors
    if the input contains non-numeric values.
    """
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid argument types.")
    
    num_sum = sum(lst)
    return num_sum / len(lst)

def median(lst: list | tuple) -> int | float:
    """Finds the middle value of a list of numbers.

    This function takes a list or tuple of numbers and returns the median.
    It sorts the list and identifies the middle value. If the list has an even
    number of elements, it returns the average of the two middle values.
    It attempts to convert all elements to integers, and handles potential errors
    if the input contains non-numeric values.
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
    """Calculates the percentage of a fraction relative to a whole.

    This function takes a fraction and a whole number and returns the percentage
    that the fraction represents of the whole. It handles potential errors
    if the input contains invalid argument types.
    """
    try: 
        result = fraction / whole * 100
        return result
    except ValueError:
        print("Invalid argument types.")

def linear_regression(x: list[float] | list[int] , y: list[float] | list[int]) -> float:
    """Calculates the slope and intercept of a linear regression line.

    This function takes two lists of numbers, x and y, and calculates the
    slope and intercept of the best-fit line using the Ordinary Least Squares
    (OLS) method. It ensures that both lists have the same length and handles
    potential errors if the input contains non-numeric values.
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
    sum_x_squared = sum(xi ** 2 for xi in x)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))

    slope = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
    intercept = (sum_y - slope * sum_x) / n

    return slope, intercept