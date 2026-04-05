def bubble_sort(lst: list[int|float]):
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

def insertion_sort(lst: list[int|float]):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

#Note: Returns a new list 
def merge_sort(lst: list[int|float]):
    if len(lst) <= 1:
        return lst
    
    middle = len(lst) // 2
    left_half = merge_sort(lst[:middle])
    right_half = merge_sort(lst[middle:])

    return merge_helper(left_half, right_half)

def merge_helper(left, right):
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
