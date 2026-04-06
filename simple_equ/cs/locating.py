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

def binary_search(arr: list[int] | tuple[int], target: int):
    """
        Finds a target element's index. Array must be sorted for the search to work. O(log n) time complexity. 
    """
    low = 0 
    high = len(arr) - 1
    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == target: 
            return middle
        
        elif target < arr[middle]: 
            high = middle - 1
        
        else: 
            low = middle + 1
    return -1

def interpolation_search(arr: list[int] | tuple[int], target: int):
    """
        Finds a target element's index. Array must be sorted for the search to work. O(log n) time complexity. 
    """
    low = 0 
    high = len(arr) - 1
    while low <= high:
        pos = low + (((target - arr[low]) * (high - low)) // (arr[high] - arr[low]))

        if arr[pos] == target: 
            return pos
        
        elif target < arr[pos]: 
            high = pos - 1
        
        else: 
            low = pos + 1
    return -1