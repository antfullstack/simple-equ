def average(lst: list | tuple) -> int | float:
    # Converts any numbers in string form to ints and checks for invalid inputs
    try:
        lst = list(map(int, lst))
    except ValueError:
        print("Invalid argument types.")
    
    num_sum = sum(lst)
    return num_sum / len(lst)

def median(lst: list | tuple) -> int | float:
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