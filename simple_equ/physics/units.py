#This file will be used for unit conversions

from . import constants


def distance_converter(value, from_unit: str, to_unit: str):
    """[Summary]: Convert distance between supported units.

    [Description]: Converts a distance value from one unit to another using
    predefined conversion factors. Supports meters, feet, and inches with
    common abbreviations. Returns the value unchanged if units are the same.
    Raises ValueError for invalid units or negative values.

    [Usage]: Typical usage example:

        result = distance_converter(10, 'meters', 'feet')
        print(result)  # Output: 32.80839895
    """
    # Input validation
    if not isinstance(value, (int, float)):
        raise TypeError("Value must be a number (int or float).")
    if value < 0:
        raise ValueError("Distance cannot be negative.")

    # Normalize units using aliases
    from_unit_normalized = constants.UNIT_ALIASES.get(from_unit.lower(), from_unit.lower())
    to_unit_normalized = constants.UNIT_ALIASES.get(to_unit.lower(), to_unit.lower())

    # Check for same units first
    if from_unit_normalized == to_unit_normalized:
        return value

    # Check if units are supported
    if from_unit_normalized not in constants.CONVERSION_FACTORS:
        raise ValueError(f"Unsupported 'from' unit: '{from_unit}'. "
                         f"Supported units: {list(constants.CONVERSION_FACTORS.keys())}")
    if to_unit_normalized not in constants.CONVERSION_FACTORS[from_unit_normalized]:
        raise ValueError(f"Unsupported conversion from '{from_unit}' to '{to_unit}'. "
                         f"Supported conversions from {from_unit_normalized}: "
                         f"{list(constants.CONVERSION_FACTORS[from_unit_normalized].keys())}")

    # Perform conversion
    factor = constants.CONVERSION_FACTORS[from_unit_normalized][to_unit_normalized]
    return value * factor
    