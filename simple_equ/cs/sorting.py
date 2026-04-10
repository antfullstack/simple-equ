def bubble_sort(lst: list[int | float]):
    """[Summary]: Sort a list in ascending order using bubble sort.

    [Description]: Repeatedly compares adjacent elements and swaps them when
    they are out of order. The input list is sorted in place and then returned.

    [Usage]: Typical usage example:

        result = bubble_sort([4, 2, 1, 3])
        print(result)
    """
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(lst: list[int | float]):
    """[Summary]: Sort a list in ascending order using insertion sort.

    [Description]: Builds the sorted output one element at a time by shifting
    larger elements to the right until the current value can be inserted into
    its correct position.

    [Usage]: Typical usage example:

        result = insertion_sort([4, 2, 1, 3])
        print(result)
    """
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def quick_sort(lst: list[int | float]):
    """[Summary]: Return a new list sorted in ascending order using quick sort.
    [Description]: Selects a pivot element and partitions the input into values
    less than, equal to, and greater than the pivot. Each partition is sorted
    recursively and the results are concatenated into a new sorted list.
    [Usage]: Typical usage example:
        result = quick_sort([4, 2, 1, 3])
        print(result)
    """
    # Note: Returns a new list
    if len(lst) <= 1:
        return lst
 
    pivot = lst[len(lst) // 2]
    left   = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right  = [x for x in lst if x > pivot]
 
    return quick_sort(left) + middle + quick_sort(right)

# Note: Returns a new list
def merge_sort(lst: list[int | float]):
    """[Summary]: Return a new list sorted in ascending order with merge sort.

    [Description]: Recursively splits the input into smaller halves, sorts each
    half, and merges the intermediate results back together. Unlike the in-place
    sorting functions, this function returns a newly merged list.

    [Usage]: Typical usage example:

        result = merge_sort([4, 2, 1, 3])
        print(result)
    """
    if len(lst) <= 1:
        return lst

    middle = len(lst) // 2
    left_half = merge_sort(lst[:middle])
    right_half = merge_sort(lst[middle:])

    return merge_helper(left_half, right_half)


def merge_helper(left, right):
    """[Summary]: Merge two sorted lists into one sorted list.

    [Description]: Compares the leading elements from each sorted input list and
    appends the smaller value to the result until one side is exhausted. Any
    remaining elements are then appended to the merged output.

    [Usage]: Typical usage example:

        result = merge_helper([1, 4], [2, 3])
        print(result)
    """
    sorted_lst = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_lst.append(left[i])
            i += 1
        else:
            sorted_lst.append(right[j])
            j += 1
    sorted_lst.extend(left[i:])
    sorted_lst.extend(right[j:])

    return sorted_lst

def heapify(arr, n, i):
    """[Summary]: Ensure subtree rooted at index i satisfies max-heap property.

    [Description]: Compares a node with its left and right children and swaps it
    with the largest value if necessary. This process is applied recursively to
    maintain the max-heap structure within the subtree.

    [Usage]: Typical usage example:

        arr = [3, 9, 2, 1, 4, 5]
        heapify(arr, len(arr), 0)
    """
    largest = i 
    left = 2 * i + 1 
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        right = largest
    
    if largest != i: 
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    """[Summary]: Sort a list using the heap sort algorithm and return a new list.

    [Description]: Creates a copy of the input list and transforms it into a
    max heap. It then repeatedly extracts the largest element (root) and places
    it at the end of the list, shrinking the heap each time until fully sorted.

    [Usage]: Typical usage example:

        result = heap_sort([12, 11, 13, 5, 6, 7])
        print(result)
    """
    new_arr = arr.copy()   
    n = len(new_arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(new_arr, n, i)

    # Extract elements
    for i in range(n - 1, 0, -1):
        new_arr[i], new_arr[0] = new_arr[0], new_arr[i]
        heapify(new_arr, i, 0)

    return new_arr