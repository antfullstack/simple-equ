def greatest_algorithm(arr: list[int] | tuple[int]) -> int:
    """[Summary]: Return the greatest element in a list or tuple.

    [Description]: Iterates through the provided sequence and keeps track of the
    largest value encountered. Raises a ValueError when the input sequence is
    empty.

    [Usage]: Typical usage example:

        result = greatest_algorithm([3, 7, 2])
        print(result)
    """
    if not arr:
        raise ValueError("Array or tuple cannot be empty")

    greatest = arr[0]
    for num in arr:
        if num > greatest:
            greatest = num
    return greatest


def lowest_algorithm(arr: list[int] | tuple[int]) -> int:
    """[Summary]: Return the lowest element in a list or tuple.

    [Description]: Iterates through the provided sequence and keeps track of the
    smallest value encountered. Raises a ValueError when the input sequence is
    empty.

    [Usage]: Typical usage example:

        result = lowest_algorithm([3, 7, 2])
        print(result)
    """
    if not arr:
        raise ValueError("Array or tuple cannot be empty")

    lowest = arr[0]
    for num in arr:
        if num < lowest:
            lowest = num
    return lowest


def binary_search(arr: list[int] | tuple[int], target: int):
    """[Summary]: Return the index of a target value using binary search.

    [Description]: Searches a sorted sequence by repeatedly halving the search
    interval until the target is found or the interval is exhausted. Returns -1
    when the target is not present.

    [Usage]: Typical usage example:

        result = binary_search([1, 3, 5, 7], 5)
        print(result)
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
    """[Summary]: Return the index of a target value using interpolation search.

    [Description]: Estimates the most likely position of the target in a sorted
    and uniformly distributed sequence, then narrows the search range based on
    comparisons. Returns -1 when the target is not present.

    [Usage]: Typical usage example:

        result = interpolation_search([10, 20, 30, 40], 30)
        print(result)
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

def exponential_search(arr, target):
    """[Summary]: Return the index of a target value using exponential search.

    [Description]: Quickly identifies a search range in a sorted sequence by 
    repeatedly doubling the index (1, 2, 4, 8, ...) until the target is less 
    than or equal to the current value or the array bounds are exceeded. Once 
    the range is found, applies binary search within that interval to locate 
    the target. Returns -1 when the target is not present.

    [Usage]: Typical usage example:

        result = exponential_search([10, 20, 30, 40, 50], 30, binary_search)
        print(result)
    """

    n = len(arr)

    if n == 0: 
        return -1 
    
    #If target is found at first position
    if arr[0] == target: 
        return 0 
    
    #Here, we find the range for binary search 
    i = 1
    while i < n and arr[i] <= target:
        i *= 2

    left = i // 2
    right = min (i, n- 1)

    resulting_arr = arr[left:right]
    return binary_search(resulting_arr, target)

