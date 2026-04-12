import math
from pathlib import Path
import sys
import pytest

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ import geometry as geo


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (3, 4, 5.0),
        (5, 12, 13.0),
        (0.0, 5.0, 5.0),
        (1.5, 2.5, math.hypot(1.5, 2.5)),
    ],
)
def test_pythagoras(a, b, expected):
    """[Summary]: Verify that pythagoras returns the expected hypotenuse.

    [Description]: Runs multiple right-triangle inputs and compares the
    calculated hypotenuse against the expected value with a floating-point
    tolerance.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_pythagoras
    """
    assert geo.pythagoras(a, b) == pytest.approx(expected, rel=1e-9)


def test_pythagoras_negative():
    # Negatives ok since squared
    """[Summary]: Verify that pythagoras handles negative leg values correctly.

    [Description]: Confirms that negative coordinates do not affect the final
    hypotenuse because the implementation squares both inputs.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_pythagoras_negative
    """
    assert geo.pythagoras(-3, 4) == pytest.approx(5.0)


@pytest.mark.parametrize(
    "a,expected",
    [
        (4, 16.0),
        (0, 0.0),
        (2.5, 6.25),
    ],
)
def test_square_area(a, expected):
    """[Summary]: Verify that square_area returns the expected area.

    [Description]: Checks several side lengths and compares the returned square
    area against the known expected values.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_square_area
    """
    assert geo.square_area(a) == expected


@pytest.mark.parametrize(
    "a,expected",
    [
        (2, 8.0),
        (0, 0.0),
    ],
)
def test_cube_area(a, expected):
    """[Summary]: Verify that cube_area returns the expected volume.

    [Description]: Exercises the cube calculation with basic edge lengths and
    confirms the function returns the expected cubic result.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_cube_area
    """
    assert geo.cube_area(a) == expected


@pytest.mark.parametrize(
    "a,b,expected",
    [
        (2, 3, 6.0),
        (0, 5, 0.0),
    ],
)
def test_rectangle_area(a, b, expected):
    """[Summary]: Verify that rectangle_area returns the expected area.

    [Description]: Validates the rectangle area helper with representative
    length and width combinations.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_rectangle_area
    """
    assert geo.rectangle_area(a, b) == expected


@pytest.mark.parametrize(
    "radius,expected",
    [
        (1, geo.pi),
        (0, 0.0),
        (5, 25 * geo.pi),
    ],
)
def test_circle_area(radius, expected):
    """[Summary]: Verify that circle_area returns the expected area.

    [Description]: Confirms the circle area implementation matches the standard
    pi * r^2 calculation for several radii.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_circle_area
    """
    assert geo.circle_area(radius) == expected


@pytest.mark.parametrize(
    "b1,b2,h,expected",
    [
        (2, 4, 3, 9.0),
        (0, 0, 5, 0.0),
    ],
)
def test_trapezoid_area(b1, b2, h, expected):
    """[Summary]: Verify that trapezoid_area returns the expected area.

    [Description]: Checks a small set of trapezoid dimensions and confirms the
    computed values match the expected results.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_trapezoid_area
    """
    assert geo.trapezoid_area(b1, b2, h) == expected


@pytest.mark.parametrize(
    "base,h,expected",
    [
        (4, 5, 10.0),
        (0, 10, 0.0),
    ],
)
def test_triangle_area(base, h, expected):
    """[Summary]: Verify that triangle_area returns the expected area.

    [Description]: Exercises the triangle area helper with representative base
    and height values.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_triangle_area
    """
    assert geo.triangle_area(base, h) == expected


@pytest.mark.parametrize(
    "l,w,h,expected",
    [
        (1, 1, 1, pytest.approx(3.236, rel=1e-3)),
    ],
)
def test_pyramid_surface(l, w, h, expected):
    """[Summary]: Verify that pyramid_surface returns the expected result.

    [Description]: Confirms the rectangular pyramid surface formula produces the
    expected value for a known input.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_pyramid_surface
    """
    assert geo.pyramid_surface(l, w, h) == expected


@pytest.mark.parametrize(
    "h,l,w,expected",
    [
        (3, 3, 3, 9.0),
        (0, 5, 5, 0.0),
    ],
)
def test_pyramid_volume(h, l, w, expected):
    """[Summary]: Verify that pyramid_volume returns the expected result.

    [Description]: Validates the pyramid volume helper with representative
    dimensions, including a zero-height edge case.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_pyramid_volume
    """
    assert geo.pyramid_volume(h, l, w) == expected


@pytest.mark.parametrize(
    "d,expected",
    [
        (10, 5.0),
        (0, 0.0),
    ],
)
def test_calculate_radius(d, expected):
    """[Summary]: Verify that calculate_radius returns half the diameter.

    [Description]: Checks standard diameter values and confirms the conversion
    from diameter to radius is correct.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_calculate_radius
    """
    assert geo.calculate_radius(d) == expected


@pytest.mark.parametrize(
    "r,expected",
    [
        (1, 2 * geo.pi),
        (0, 0.0),
    ],
)
def test_circumference(r, expected):
    """[Summary]: Verify that circumference returns the expected value.

    [Description]: Confirms the function matches the standard 2 * pi * r formula
    for representative radii.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_circumference
    """
    assert geo.circumference(r) == expected


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        ((0, 0), (3, 4), 5.0),
        ([1.0, 1.0], [4.0, 5.0], 5.0),
        ((0, 0, 0), (3, 4, 0), 5.0),
        ((0, 0, 0), (1, 1, 1), math.sqrt(3)),
    ],
)
def test_distance(p1, p2, expected):
    """[Summary]: Verify that distance returns the expected Euclidean result.

    [Description]: Covers two-dimensional and three-dimensional inputs using
    both tuples and lists to validate the distance helper.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_distance
    """
    assert geo.distance(p1, p2) == pytest.approx(expected, rel=1e-9)


def test_distance_invalid_type():
    """[Summary]: Verify that distance fails for unsupported coordinate types.

    [Description]: Ensures an invalid coordinate input triggers an exception
    instead of returning an incorrect result.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_distance_invalid_type
    """
    with pytest.raises(ValueError):
        geo.distance([1, 2], "invalid")


def test_distance_invalid_dim():
    """[Summary]: Verify that distance fails for unsupported dimensions.

    [Description]: Confirms the function rejects coordinate inputs that are not
    two-dimensional or three-dimensional.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_distance_invalid_dim
    """
    with pytest.raises(ValueError):
        geo.distance((1, 2, 3, 4), (1, 2, 3, 4))


@pytest.mark.parametrize(
    "angle_deg,expected",
    [
        (0, pytest.approx(0.0, rel=1e-2)),
        (30, pytest.approx(0.5, rel=1e-2)),
    ],
)
def test_sin(angle_deg, expected):
    """[Summary]: Verify that sin returns the expected trigonometric values.

    [Description]: Compares a few degree-based sine values against expected
    approximations.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_sin
    """
    assert geo.sin(angle_deg) == expected


@pytest.mark.parametrize(
    "angle_deg,expected",
    [
        (0, pytest.approx(1.0, rel=1e-2)),
        (60, pytest.approx(0.5, rel=1e-2)),
    ],
)
def test_cosin(angle_deg, expected):
    """[Summary]: Verify that cosin returns the expected trigonometric values.

    [Description]: Checks that the cosine helper returns expected approximations
    for representative degree inputs.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_cosin
    """
    assert geo.cosin(angle_deg) == expected


@pytest.mark.parametrize(
    "angle_deg,expected",
    [
        (45, pytest.approx(1.0, rel=1e-2)),
        (0, pytest.approx(0.0, rel=1e-2)),
    ],
)
def test_tan(angle_deg, expected):
    """[Summary]: Verify that tan returns the expected trigonometric values.

    [Description]: Compares degree-based tangent values against expected
    approximations for common angles.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_tan
    """
    assert geo.tan(angle_deg) == expected


def test_tan_90():
    """[Summary]: Verify that tan raises at ninety degrees.

    [Description]: Confirms the tangent helper propagates the division-by-zero
    behavior expected at ninety degrees.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_tan_90
    """
    with pytest.raises(ZeroDivisionError):
        geo.tan(90)


@pytest.mark.parametrize(
    "r,expected",
    [
        (1, 4 * geo.pi),
        (0, 0.0),
    ],
)
def test_sphere_surface(r, expected):
    """[Summary]: Verify that sphere_surface returns the expected area.

    [Description]: Confirms the duplicate sphere surface helper still matches
    the standard 4 * pi * r^2 formula.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_sphere_surface
    """
    assert geo.sphere_surface(r) == expected


@pytest.mark.parametrize(
    "p1,p2,expected",
    [
        ((0, 0), (3, 4), 4 / 3),
    ],
)
def test_slope(p1, p2, expected):
    """[Summary]: Verify that slope returns the expected value.

    [Description]: Checks the slope helper with a known pair of two-dimensional
    points.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_slope
    """
    assert geo.slope(p1, p2) == expected


def test_slope_vertical():
    """[Summary]: Verify that slope raises for a vertical line.

    [Description]: Confirms the implementation raises a division-by-zero error
    when both points share the same x-coordinate.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_slope_vertical
    """
    with pytest.raises(ZeroDivisionError):
        geo.slope((1, 1), (1, 5))


def test_slope_invalid_dim():
    """[Summary]: Verify that slope rejects non-2D inputs.

    [Description]: Ensures the slope helper raises a ValueError when either
    input point is not two-dimensional.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_slope_invalid_dim
    """
    with pytest.raises(ValueError):
        geo.slope((1, 2, 3), (4, 5, 6))

@pytest.mark.parametrize(
    "x,expected",
    [
        (0, 0.0),                       # arctan(0) = 0
        (1, geo.PI / 4),          # arctan(1) = π/4
        (-1, -geo.PI / 4),        # arctan(-1) = -π/4
        (1 / math.sqrt(3), geo.PI / 6),  # arctan(1/√3) = π/6
        (10, math.atan(10)),            # large positive number
        (-10, math.atan(-10)),          # large negative number
    ],
)
def test_arctan(x, expected):
    """[Summary]: Verify that arctan returns the expected angle in radians.

    [Description]: Tests the custom arctan() function for multiple inputs, 
    including zero, positive, negative, fractional, and large numbers.
    The returned angle is compared against expected values using a floating-point
    tolerance.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_arctan
    """
    assert geo.arctan(x) == pytest.approx(expected, rel=1e-9)


def test_arctan_near_pi_over_2():
    """[Summary]: Verify that arctan approaches π/2 for large positive inputs.

    [Description]: Checks that the function returns a value close to π/2 when
    the input is very large, validating proper handling of limits.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_arctan_near_pi_over_2
    """
    x = 1e6
    result = geo.arctan(x)
    assert result == pytest.approx(geo.PI / 2, rel=1e-6)


def test_arctan_near_minus_pi_over_2():
    """[Summary]: Verify that arctan approaches -π/2 for large negative inputs.

    [Description]: Checks that the function returns a value close to -π/2 when
    the input is very large and negative, validating proper handling of limits.

    [Usage]: Typical usage example:

        pytest tests/geometry/test_geometry.py -k test_arctan_near_minus_pi_over_2
    """
    x = -1e6
    result = geo.arctan(x)
    assert result == pytest.approx(-geo.PI / 2, rel=1e-6)

def test_arcsin_zero():
    """[Summary]: Verify that arcsin(0) returns 0.0.

    [Description]: Confirms that the base case of zero input produces
    exactly zero, since arctan2(0, 1) == 0.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arcsin_zero
    """
    assert geo.arcsin(0) == pytest.approx(0.0)


def test_arcsin_one_half():
    """[Summary]: Verify that arcsin(0.5) returns π/6.

    [Description]: Confirms that a well-known exact value is computed
    correctly, checking the result against math.pi / 6.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arcsin_one_half
    """
    assert geo.arcsin(0.5) == pytest.approx(math.pi / 6)


def test_arcsin_one():
    """[Summary]: Verify that arcsin(1) returns π/2.

    [Description]: Confirms the upper boundary of the domain, where the
    result should equal π/2 (90 degrees).

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arcsin_one
    """
    assert geo.arcsin(1) == pytest.approx(math.pi / 2)


def test_arcsin_negative():
    """[Summary]: Verify that arcsin returns a negative value for negative input.

    [Description]: Confirms that arcsin(-0.5) equals -π/6, validating
    the odd-function symmetry of the inverse sine.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arcsin_negative
    """
    assert geo.arcsin(-0.5) == pytest.approx(-math.pi / 6)


def test_arcsin_integer_input():
    """[Summary]: Verify that arcsin accepts an integer argument.

    [Description]: Confirms that passing an int (rather than a float)
    does not raise a TypeError and still returns the correct result.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arcsin_integer_input
    """
    assert geo.arcsin(0) == pytest.approx(0.0)


# ---------------------------------------------------------------------------
# arccos
# ---------------------------------------------------------------------------

def test_arccos_zero():
    """[Summary]: Verify that arccos(0) returns π/2.

    [Description]: Confirms the base case where the cosine of π/2 is 0,
    so the inverse should return π/2.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arccos_zero
    """
    assert geo.arccos(0) == pytest.approx(math.pi / 2)


def test_arccos_one():
    """[Summary]: Verify that arccos(1) returns 0.0.

    [Description]: Confirms the upper boundary of the domain, where
    cos(0) == 1 so the inverse must return 0.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arccos_one
    """
    assert geo.arccos(1) == pytest.approx(0.0)


def test_arccos_negative_one():
    """[Summary]: Verify that arccos(-1) returns π.

    [Description]: Confirms the lower boundary of the domain, where
    cos(π) == -1 so the inverse must return π.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arccos_negative_one
    """
    assert geo.arccos(-1) == pytest.approx(math.pi)


def test_arccos_one_half():
    """[Summary]: Verify that arccos(0.5) returns π/3.

    [Description]: Confirms a well-known exact value, checking the result
    against math.pi / 3 to validate the complementary-angle identity.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arccos_one_half
    """
    assert geo.arccos(0.5) == pytest.approx(math.pi / 3)


def test_arccos_complementary_identity():
    """[Summary]: Verify that arcsin(x) + arccos(x) equals π/2 for arbitrary x.

    [Description]: Confirms the fundamental complementary identity holds
    numerically for a mid-range value, cross-validating both functions.

    [Usage]: Typical usage example:

        pytest tests/test_trig_inverses.py -k test_arccos_complementary_identity
    """
    x = 0.7
    assert geo.arcsin(x) + geo.arccos(x) == pytest.approx(math.pi / 2)