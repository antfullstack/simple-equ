def greatest_algorithm(arr: list[int] | tuple[int]) -> int:
    """
    Finds the greatest element in an array or tuple.
    """
    if not arr:
        raise ValueError("Array or tuple cannot be empty")
    
    greatest = arr[0]
    for num in arr:
        if num > greatest:
            greatest = num
    return greatest

def lowest_algorithm(arr: list[int] | tuple[int]) -> int:
    """
    Finds the lowest element in an array or tuple.
    """
    if not arr:
        raise ValueError("Array or tuple cannot be empty")
    
    lowest = arr[0]
    for num in arr:
        if num < lowest:
            lowest = num
    return lowest
