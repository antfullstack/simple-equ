import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ.cs.locating import greatest_algorithm, lowest_algorithm, binary_search, interpolation_search, exponential_search
from simple_equ.cs.sorting import bubble_sort, insertion_sort, merge_sort, heap_sort, heapify


# ==============================================================================
# greatest_algorithm()
# ==============================================================================

@pytest.mark.parametrize(
    "arr,expected",
    [
        ([3, 7, 2], 7),
        ([1], 1),
        ([-3, -1, -2], -1),
        ([0, 0, 0], 0),
        ((4, 9, 5), 9),
        ([100, 99, 98], 100),
        ([-10, 0, 10], 10),
    ],
)
def test_greatest_algorithm_numeric(arr, expected):
    """[Summary]: Verify that greatest_algorithm returns the largest element.

    [Description]: Runs parametrized inputs covering positive, negative, zero,
    single-element, and tuple sequences, comparing the result against the known
    largest value.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_greatest_algorithm_numeric
    """
    assert greatest_algorithm(arr) == expected


def test_greatest_algorithm_empty_raises():
    """[Summary]: Verify that greatest_algorithm raises for an empty sequence.

    [Description]: Confirms that passing an empty list causes a ValueError
    since there is no element to evaluate.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_greatest_algorithm_empty_raises
    """
    with pytest.raises(ValueError, match="Array or tuple cannot be empty"):
        greatest_algorithm([])


def test_greatest_algorithm_all_equal():
    """[Summary]: Verify that greatest_algorithm handles all-equal elements.

    [Description]: Confirms the function returns the single repeated value when
    every element in the sequence is identical.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_greatest_algorithm_all_equal
    """
    assert greatest_algorithm([5, 5, 5]) == 5


# ==============================================================================
# lowest_algorithm()
# ==============================================================================

@pytest.mark.parametrize(
    "arr,expected",
    [
        ([3, 7, 2], 2),
        ([1], 1),
        ([-3, -1, -2], -3),
        ([0, 0, 0], 0),
        ((4, 9, 5), 4),
        ([100, 99, 98], 98),
        ([-10, 0, 10], -10),
    ],
)
def test_lowest_algorithm_numeric(arr, expected):
    """[Summary]: Verify that lowest_algorithm returns the smallest element.

    [Description]: Runs parametrized inputs covering positive, negative, zero,
    single-element, and tuple sequences, comparing the result against the known
    smallest value.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_lowest_algorithm_numeric
    """
    assert lowest_algorithm(arr) == expected


def test_lowest_algorithm_empty_raises():
    """[Summary]: Verify that lowest_algorithm raises for an empty sequence.

    [Description]: Confirms that passing an empty list causes a ValueError
    since there is no element to evaluate.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_lowest_algorithm_empty_raises
    """
    with pytest.raises(ValueError, match="Array or tuple cannot be empty"):
        lowest_algorithm([])


def test_lowest_algorithm_all_equal():
    """[Summary]: Verify that lowest_algorithm handles all-equal elements.

    [Description]: Confirms the function returns the single repeated value when
    every element in the sequence is identical.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_lowest_algorithm_all_equal
    """
    assert lowest_algorithm([5, 5, 5]) == 5


# ==============================================================================
# binary_search()
# ==============================================================================

@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([1, 3, 5, 7, 9], 5, 2),
        ([1, 3, 5, 7, 9], 1, 0),
        ([1, 3, 5, 7, 9], 9, 4),
        ([10, 20, 30], 20, 1),
        ([42], 42, 0),
        ((-5, -3, -1, 0, 2), -1, 2),
    ],
)
def test_binary_search_found(arr, target, expected):
    """[Summary]: Verify that binary_search returns the correct index when the target exists.

    [Description]: Runs parametrized sorted sequences including first element,
    last element, middle element, single-element, and negative-value cases,
    confirming the returned index matches the expected position.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_binary_search_found
    """
    assert binary_search(arr, target) == expected


@pytest.mark.parametrize(
    "arr,target",
    [
        ([1, 3, 5, 7, 9], 4),
        ([1, 3, 5], 10),
        ([], 1),
        ([2, 4, 6], 5),
    ],
)
def test_binary_search_not_found(arr, target):
    """[Summary]: Verify that binary_search returns -1 when the target is absent.

    [Description]: Confirms the function returns -1 for a missing value,
    an empty sequence, and a target outside the range of the array.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_binary_search_not_found
    """
    assert binary_search(arr, target) == -1


def test_binary_search_single_element_not_found():
    """[Summary]: Verify that binary_search returns -1 for a non-matching single element.

    [Description]: Ensures the algorithm correctly handles the minimal case
    where the only element does not match the target.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_binary_search_single_element_not_found
    """
    assert binary_search([7], 3) == -1


# ==============================================================================
# interpolation_search()
# ==============================================================================

@pytest.mark.parametrize(
    "arr,target,expected",
    [
        ([10, 20, 30, 40, 50], 30, 2),
        ([10, 20, 30, 40, 50], 10, 0),
        ([10, 20, 30, 40, 50], 50, 4),
        ([1, 2, 3, 4, 5], 3, 2),
        ([5, 10, 15], 10, 1),
    ],
)
def test_interpolation_search_found(arr, target, expected):
    """[Summary]: Verify that interpolation_search returns the correct index when the target exists.

    [Description]: Runs parametrized uniformly distributed sorted sequences
    including first, last, and middle element cases, confirming the returned
    index matches the expected position.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_interpolation_search_found
    """
    assert interpolation_search(arr, target) == expected


@pytest.mark.parametrize(
    "arr,target",
    [
        ([10, 20, 30, 40, 50], 25),
        ([10, 20, 30], 99),
    ],
)
def test_interpolation_search_not_found(arr, target):
    """[Summary]: Verify that interpolation_search returns -1 when the target is absent.

    [Description]: Confirms the function returns -1 for a value that is missing
    from the sequence or lies outside its range.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_interpolation_search_not_found
    """
    assert interpolation_search(arr, target) == -1


# ==============================================================================
# bubble_sort()
# ==============================================================================

@pytest.mark.parametrize(
    "lst,expected",
    [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1], [1]),
        ([], []),
        ([-3, -1, -2], [-3, -2, -1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([1.5, 0.5, 2.5], [0.5, 1.5, 2.5]),
    ],
)
def test_bubble_sort(lst, expected):
    """[Summary]: Verify that bubble_sort returns a correctly sorted list.

    [Description]: Runs parametrized inputs covering already-sorted, reversed,
    single-element, empty, negative, duplicate, and float-value lists,
    confirming the result matches the expected ascending order.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_bubble_sort
    """
    assert bubble_sort(lst) == expected


def test_bubble_sort_mutates_in_place():
    """[Summary]: Verify that bubble_sort sorts the original list in place.

    [Description]: Confirms the function modifies the input list directly,
    returning the same object rather than a new one.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_bubble_sort_mutates_in_place
    """
    lst = [3, 1, 2]
    result = bubble_sort(lst)
    assert result is lst


# ==============================================================================
# insertion_sort()
# ==============================================================================

@pytest.mark.parametrize(
    "lst,expected",
    [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1], [1]),
        ([], []),
        ([-3, -1, -2], [-3, -2, -1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([1.5, 0.5, 2.5], [0.5, 1.5, 2.5]),
    ],
)
def test_insertion_sort(lst, expected):
    """[Summary]: Verify that insertion_sort returns a correctly sorted list.

    [Description]: Runs parametrized inputs covering already-sorted, reversed,
    single-element, empty, negative, duplicate, and float-value lists,
    confirming the result matches the expected ascending order.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_insertion_sort
    """
    assert insertion_sort(lst) == expected


def test_insertion_sort_mutates_in_place():
    """[Summary]: Verify that insertion_sort sorts the original list in place.

    [Description]: Confirms the function modifies the input list directly,
    returning the same object rather than a new one.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_insertion_sort_mutates_in_place
    """
    lst = [3, 1, 2]
    result = insertion_sort(lst)
    assert result is lst


# ==============================================================================
# merge_sort()
# ==============================================================================

@pytest.mark.parametrize(
    "lst,expected",
    [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([1, 2, 3, 4], [1, 2, 3, 4]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1], [1]),
        ([], []),
        ([-3, -1, -2], [-3, -2, -1]),
        ([3, 1, 4, 1, 5, 9, 2, 6], [1, 1, 2, 3, 4, 5, 6, 9]),
        ([1.5, 0.5, 2.5], [0.5, 1.5, 2.5]),
    ],
)
def test_merge_sort(lst, expected):
    """[Summary]: Verify that merge_sort returns a new correctly sorted list.

    [Description]: Runs parametrized inputs covering already-sorted, reversed,
    single-element, empty, negative, duplicate, and float-value lists,
    confirming the returned list matches the expected ascending order.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_merge_sort
    """
    assert merge_sort(lst) == expected


def test_merge_sort_returns_new_list():
    """[Summary]: Verify that merge_sort does not mutate the original list.

    [Description]: Confirms the function returns a distinct list object, leaving
    the input unchanged, consistent with its documented behaviour.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_merge_sort_returns_new_list
    """
    lst = [3, 1, 2]
    result = merge_sort(lst)
    assert result is not lst
    assert lst == [3, 1, 2]


def test_merge_sort_large_input():
    """[Summary]: Verify that merge_sort correctly handles a larger input.

    [Description]: Confirms the recursive implementation produces a correctly
    sorted result for a list with many elements.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_merge_sort_large_input
    """
    import random
    lst = list(range(100, 0, -1))
    assert merge_sort(lst) == list(range(1, 101))

def test_exponential_search_finds_element():
    """[Summary]: Verify that exponential_search correctly finds an existing element.

    [Description]: Confirms the function returns the correct index when the
    target value is present in a sorted sequence.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_exponential_search_finds_element
    """
    arr = [1, 3, 5, 7, 9]
    assert exponential_search(arr, 5) == 2


def test_exponential_search_not_found():
    """[Summary]: Verify that exponential_search returns -1 when target is absent.

    [Description]: Confirms the function correctly indicates absence of the
    target value in a sorted sequence.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_exponential_search_not_found
    """
    arr = [1, 3, 5, 7, 9]
    assert exponential_search(arr, 4) == -1


def test_exponential_search_first_element():
    """[Summary]: Verify that exponential_search handles the first element correctly.

    [Description]: Confirms the function immediately returns index 0 when the
    target matches the first element of the sequence.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_exponential_search_first_element
    """
    arr = [1, 3, 5, 7, 9]
    assert exponential_search(arr, 1) == 0


def test_exponential_search_last_element():
    """[Summary]: Verify that exponential_search correctly finds the last element.

    [Description]: Confirms the function properly expands the search range to
    include and locate the final element in the sequence.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_exponential_search_last_element
    """
    arr = [1, 3, 5, 7, 9]
    assert exponential_search(arr, 9) == 4


def test_exponential_search_empty_list():
    """[Summary]: Verify that exponential_search handles an empty list.

    [Description]: Confirms the function returns -1 when invoked on an empty
    sequence.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_exponential_search_empty_list
    """
    assert exponential_search([], 10) == -1


def test_exponential_search_single_element():
    """[Summary]: Verify that exponential_search handles a single-element list.

    [Description]: Confirms correct behavior when the sequence contains only
    one element, for both matching and non-matching targets.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_exponential_search_single_element
    """
    arr = [5]
    assert exponential_search(arr, 5) == 0
    assert exponential_search(arr, 1) == -1

def test_heapify_basic_case():
    """[Summary]: Verify that heapify enforces max-heap property on a subtree.

    [Description]: Confirms that heapify correctly rearranges elements so that
    the parent node is greater than its children for a simple unsorted subtree.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_heapify_basic_case
    """
    arr = [3, 9, 2]
    heapify(arr, len(arr), 0)
    assert arr == [9, 3, 2]


def test_heapify_no_change_needed():
    """[Summary]: Verify that heapify leaves a valid heap unchanged.

    [Description]: Confirms that heapify does not modify the array when the
    subtree already satisfies the max-heap property.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_heapify_no_change_needed
    """
    arr = [9, 3, 2]
    heapify(arr, len(arr), 0)
    assert arr == [9, 3, 2]


def test_heap_sort_empty_list():
    """[Summary]: Verify that heap_sort handles an empty list.

    [Description]: Confirms the function returns an empty list when given
    an empty input.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_heap_sort_empty_list
    """
    assert heap_sort([]) == []


def test_heap_sort_single_element():
    """[Summary]: Verify that heap_sort handles a single-element list.

    [Description]: Confirms the function correctly returns a list containing
    the single element without modification.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_heap_sort_single_element
    """
    assert heap_sort([5]) == [5]


def test_heap_sort_multiple_elements():
    """[Summary]: Verify that heap_sort correctly sorts multiple elements.

    [Description]: Confirms the function returns a new list with all elements
    sorted in ascending order for a typical unsorted input.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_heap_sort_multiple_elements
    """
    arr = [12, 11, 13, 5, 6, 7]
    assert heap_sort(arr) == [5, 6, 7, 11, 12, 13]


def test_heap_sort_does_not_modify_input():
    """[Summary]: Verify that heap_sort does not modify the original list.

    [Description]: Confirms the function returns a new sorted list while
    leaving the input list unchanged.

    [Usage]: Typical usage example:

        pytest tests/test_algorithms.py -k test_heap_sort_does_not_modify_input
    """
    arr = [4, 1, 3]
    _ = heap_sort(arr)
    assert arr == [4, 1, 3]