import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ.statistics.statistics import mode, standardization, average, median, percentage, linear_regression, dot, bayes_theorem


# ==============================================================================
# average()
# ==============================================================================

@pytest.mark.parametrize(
    "lst,expected",
    [
        ([1, 2, 3], 2.0),
        ([1, 2], 1.5),
        ([5], 5.0),
        ([-1, -2, -3], -2.0),
        ([-5, 5], 0.0),
        ([0, 0, 0], 0.0),
        (list(range(1, 101)), 50.5),
    ],
)
def test_average_numeric(lst, expected):
    """[Summary]: Verify that average returns the correct arithmetic mean.

    [Description]: Runs a range of numeric list inputs including positive,
    negative, zero, and large lists, comparing the result against the known
    expected mean.

    [Usage]: Typical usage example:

        pytest tests/test_math_utils.py -k test_average_numeric
    """
    assert average(lst) == pytest.approx(expected)


def test_average_tuple_input():
    """[Summary]: Verify that average accepts a tuple as input.

    [Description]: Confirms the function handles tuple arguments the same way
    it handles lists, returning the correct arithmetic mean.

    [Usage]: Typical usage example:

        pytest tests/test_average_tuple_input
    """
    assert average((4, 8, 12)) == pytest.approx(8.0)


def test_average_string_integers():
    """[Summary]: Verify that average coerces string digits to integers.

    [Description]: Confirms that a list of numeric strings is converted via
    int() before computing the mean, returning the correct result.

    [Usage]: Typical usage example:

        pytest tests/test_average_string_integers
    """
    assert average(["1", "2", "3"]) == pytest.approx(2.0)


def test_average_invalid_types_prints_error(capsys):
    """[Summary]: Verify that average prints an error for non-numeric strings.

    [Description]: Passes a list of non-numeric strings and confirms the
    expected error message is printed to stdout via capsys.

    [Usage]: Typical usage example:

        pytest tests/test_average_invalid_types_prints_error
    """
    average(["a", "b", "c"])
    captured = capsys.readouterr()
    assert "Invalid argument types." in captured.out


def test_average_empty_list_raises():
    """[Summary]: Verify that average raises for an empty list.

    [Description]: Confirms that passing an empty list causes a ZeroDivisionError
    since there are no elements to divide by.

    [Usage]: Typical usage example:

        pytest tests/test_average_empty_list_raises
    """
    with pytest.raises(ZeroDivisionError):
        average([])


# ==============================================================================
# median()
# ==============================================================================

@pytest.mark.parametrize(
    "lst,expected",
    [
        ([1, 2, 3], 2),
        ([1, 2, 3, 4], 2.5),
        ([7], 7),
        ([5, 1, 3], 3),
        ([-3, -1, -2], -2),
        ([1, 3], 2.0),
        ([10, 20, 30, 40], 25.0),
        ([1, 1, 1, 1], 1.0),
    ],
)
def test_median_numeric(lst, expected):
    """[Summary]: Verify that median returns the correct middle value.

    [Description]: Runs parametrized inputs covering odd-length, even-length,
    single-element, unsorted, negative, and duplicate-value lists, comparing
    results against known expected medians.

    [Usage]: Typical usage example:

        pytest tests/test_median_numeric
    """
    assert median(lst) == pytest.approx(expected)


def test_median_tuple_input():
    """[Summary]: Verify that median accepts a tuple as input.

    [Description]: Confirms the function handles tuple arguments the same way
    it handles lists, returning the correct median value.

    [Usage]: Typical usage example:

        pytest tests/test_median_tuple_input
    """
    assert median((10, 20, 30)) == pytest.approx(20)


def test_median_string_integers():
    """[Summary]: Verify that median coerces string digits to integers.

    [Description]: Confirms that a list of numeric strings is converted to
    integers before sorting and selecting the median.

    [Usage]: Typical usage example:

        pytest tests/test_median_string_integers
    """
    assert median(["3", "1", "2"]) == pytest.approx(2)


def test_median_unsorted_even():
    """[Summary]: Verify that median sorts before selecting the middle elements.

    [Description]: Passes an unsorted even-length list and confirms the function
    sorts first, then averages the two central elements correctly.

    [Usage]: Typical usage example:

        pytest tests/test_median_unsorted_even
    """
    assert median([4, 1, 3, 2]) == pytest.approx(2.5)


def test_median_invalid_types_prints_error(capsys):
    """[Summary]: Verify that median prints an error for non-numeric strings.

    [Description]: Passes a list of non-numeric strings and confirms the
    expected error message is printed to stdout via capsys.

    [Usage]: Typical usage example:

        pytest tests/test_median_invalid_types_prints_error
    """
    median(["x", "y", "z"])
    captured = capsys.readouterr()
    assert "Invalid argument types." in captured.out


def test_median_empty_list_raises():
    """[Summary]: Verify that median raises for an empty list.

    [Description]: Confirms that passing an empty list causes an error since
    there is no element to return as the median.

    [Usage]: Typical usage example:

        pytest tests/test_median_empty_list_raises
    """
    with pytest.raises((IndexError, ZeroDivisionError)):
        median([])


# ==============================================================================
# percentage()
# ==============================================================================

@pytest.mark.parametrize(
    "fraction,whole,expected",
    [
        (25, 200, 12.5),
        (100, 100, 100.0),
        (0, 50, 0.0),
        (300, 100, 300.0),
        (-25, 100, -25.0),
        (1, 4, 25.0),
        (0.5, 4, 12.5),
    ],
)
def test_percentage_numeric(fraction, whole, expected):
    """[Summary]: Verify that percentage returns the correct percentage value.

    [Description]: Runs a range of fraction and whole inputs including zero,
    negative, float, and over-100% cases, comparing results against known
    expected percentages.

    [Usage]: Typical usage example:

        pytest tests/test_percentage_numeric
    """
    assert percentage(fraction, whole) == pytest.approx(expected)


def test_percentage_float_precision():
    """[Summary]: Verify that percentage handles non-terminating float results.

    [Description]: Uses a fraction and whole whose result is a repeating
    decimal and confirms the output matches the expected approximation.

    [Usage]: Typical usage example:

        pytest tests/test_percentage_float_precision
    """
    assert percentage(1, 3) == pytest.approx(33.3333, rel=1e-3)


def test_percentage_zero_whole_raises():
    """[Summary]: Verify that percentage raises when whole is zero.

    [Description]: Confirms that dividing by zero raises a ZeroDivisionError
    since the function does not guard against a zero denominator.

    [Usage]: Typical usage example:

        pytest tests/test_percentage_zero_whole_raises
    """
    with pytest.raises(ZeroDivisionError):
        percentage(10, 0)


def test_percentage_negative_whole():
    """[Summary]: Verify that percentage handles a negative whole value.

    [Description]: Confirms the function correctly computes a negative-whole
    percentage without raising an error.

    [Usage]: Typical usage example:

        pytest tests/test_percentage_negative_whole
    """
    assert percentage(50, -100) == pytest.approx(-50.0)


def test_percentage_both_negative():
    """[Summary]: Verify that percentage handles both negative inputs.

    [Description]: Confirms that a negative fraction over a negative whole
    returns a positive percentage value.

    [Usage]: Typical usage example:

        pytest tests/test_percentage_both_negative
    """
    assert percentage(-50, -100) == pytest.approx(50.0)


# ==============================================================================
# linear_regression()
# ==============================================================================

@pytest.mark.parametrize(
    "x,y,expected_slope,expected_intercept",
    [
        ([1, 2, 3], [2, 4, 6], 2.0, 0.0),
        ([1, 2, 3], [6, 4, 2], -2.0, 8.0),
        ([1, 2, 3], [5, 5, 5], 0.0, 5.0),
        ([0.5, 1.5, 2.5], [1.0, 3.0, 5.0], 2.0, 0.0),
        ([0, 1, 2, 3], [1, 3, 5, 7], 2.0, 1.0),
    ],
)
def test_linear_regression_slope_intercept(x, y, expected_slope, expected_intercept):
    """[Summary]: Verify that linear_regression returns the correct slope and intercept.

    [Description]: Runs parametrized inputs covering positive slope, negative
    slope, horizontal line, float inputs, and non-zero intercept cases,
    comparing computed slope and intercept against known expected values.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_slope_intercept
    """
    slope, intercept = linear_regression(x, y)
    assert slope == pytest.approx(expected_slope)
    assert intercept == pytest.approx(expected_intercept)


def test_linear_regression_returns_tuple():
    """[Summary]: Verify that linear_regression returns a two-element tuple.

    [Description]: Confirms the return value is a tuple of length two,
    representing the slope and intercept respectively.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_returns_tuple
    """
    result = linear_regression([1, 2, 3], [2, 4, 6])
    assert isinstance(result, tuple)
    assert len(result) == 2


def test_linear_regression_string_numbers():
    """[Summary]: Verify that linear_regression coerces string digits to floats.

    [Description]: Confirms that lists of numeric strings are converted via
    float() before computing the regression, returning the correct slope and
    intercept.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_string_numbers
    """
    slope, intercept = linear_regression(["1", "2", "3"], ["2", "4", "6"])
    assert slope == pytest.approx(2.0)
    assert intercept == pytest.approx(0.0)


def test_linear_regression_mismatched_lengths_prints_error(capsys):
    """[Summary]: Verify that linear_regression prints an error for mismatched lengths.

    [Description]: Passes x and y sequences of different lengths and confirms
    the expected error message is printed to stdout and None is returned.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_mismatched_lengths_prints_error
    """
    result = linear_regression([1, 2, 3], [1, 2])
    captured = capsys.readouterr()
    assert "same length" in captured.out
    assert result is None


def test_linear_regression_mismatched_lengths_returns_none():
    """[Summary]: Verify that linear_regression returns None for mismatched lengths.

    [Description]: Confirms the function returns None rather than raising an
    exception when x and y have different numbers of elements.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_mismatched_lengths_returns_none
    """
    assert linear_regression([1, 2, 3], [1, 2]) is None


def test_linear_regression_invalid_types_prints_error(capsys):
    """[Summary]: Verify that linear_regression prints an error for non-numeric input.

    [Description]: Passes non-numeric strings and confirms the expected error
    message is printed to stdout and None is returned.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_invalid_types_prints_error
    """
    result = linear_regression(["a", "b"], [1, 2])
    captured = capsys.readouterr()
    assert "Invalid argument types." in captured.out
    assert result is None


def test_linear_regression_invalid_types_returns_none():
    """[Summary]: Verify that linear_regression returns None on invalid input.

    [Description]: Confirms the function returns None rather than raising an
    exception when non-numeric values are provided.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_invalid_types_returns_none
    """
    assert linear_regression(["a", "b"], [1, 2]) is None


def test_linear_regression_single_point_raises():
    """[Summary]: Verify that linear_regression raises for a single data point.

    [Description]: Confirms that providing only one x-y pair causes a
    ZeroDivisionError since the OLS denominator collapses to zero.

    [Usage]: Typical usage example:

        pytest tests/test_linear_regression_single_point_raises
    """
    with pytest.raises(ZeroDivisionError):
        linear_regression([1], [1])


# ==============================================================================
# dot()
# ==============================================================================

@pytest.mark.parametrize(
    "x,w,expected",
    [
        ([1, 2, 3], [4, 5, 6], 32),
        ([0, 0, 0], [1, 2, 3], 0),
        ([1, 1, 1], [7, 8, 9], 24),
        ([-1, -2], [3, 4], -11),
        ([3], [7], 21),
        ([-1, 2, -3], [4, -5, 6], -32),
    ],
)
def test_dot_numeric(x, w, expected):
    """[Summary]: Verify that dot returns the correct dot product.

    [Description]: Runs parametrized inputs covering positive, zero, unit,
    negative, single-element, and mixed-sign vectors, comparing results against
    known expected dot products.

    [Usage]: Typical usage example:

        pytest tests/test_dot_numeric
    """
    assert dot(x, w) == pytest.approx(expected)


def test_dot_float_values():
    """[Summary]: Verify that dot handles floating-point vector elements.

    [Description]: Confirms the function correctly multiplies and sums float
    elements, returning the expected floating-point dot product.

    [Usage]: Typical usage example:

        pytest tests/test_dot_float_values
    """
    assert dot([0.5, 1.5], [2.0, 4.0]) == pytest.approx(7.0)
