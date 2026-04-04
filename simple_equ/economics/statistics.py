def average(lst):
    # Converts any numbers in string form to ints and checks for invalid inputs
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid argument types.")
    
    num_sum = sum(lst)
    return num_sum / len(lst)

def median(lst):
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
    try: 
        result = fraction / whole * 100
        return result
    except ValueError:
        print("Invalid argument types.")

# OLS Linear Regression - returns slope and intercept of the best fit line for the given x and y data points
def linear_regression(x, y):
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