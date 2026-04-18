"""Temperature conversion utilities.

This module provides functions to convert between different temperature scales:
Celsius (C), Fahrenheit (F), and Kelvin (K).
"""


def temperature_converter(value: float, from_unit: str, to_unit: str) -> float:
    """[Summary]: Convert temperature between different units.

    [Description]: Converts a temperature value from one unit to another.
    Supports Celsius (C), Fahrenheit (F), and Kelvin (K). The function uses
    Kelvin as an intermediate conversion standard to ensure accuracy for all
    conversion paths.

    [Usage]: Typical usage examples:

        # Convert Celsius to Fahrenheit
        result = temperature_converter(0, "C", "F")
        print(result)  # Output: 32.0

        # Convert Celsius to Kelvin
        result = temperature_converter(25, "C", "K")
        print(result)  # Output: 298.15

        # Convert Fahrenheit to Celsius
        result = temperature_converter(98.6, "F", "C")
        print(result)  # Output: 37.0

        # Convert Kelvin to Fahrenheit
        result = temperature_converter(273.15, "K", "F")
        print(result)  # Output: 32.0
    """
    # Validate input units
    valid_units = {"C", "F", "K"}
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit not in valid_units:
        raise ValueError(f"Invalid from_unit: {from_unit}. Must be one of {valid_units}")
    if to_unit not in valid_units:
        raise ValueError(f"Invalid to_unit: {to_unit}. Must be one of {valid_units}")

    # If units are the same, return the value unchanged
    if from_unit == to_unit:
        return value

    # Step 1: Convert to Kelvin (intermediate standard)
    if from_unit == "C":
        kelvin = value + 273.15
    elif from_unit == "F":
        kelvin = (value - 32) * 5 / 9 + 273.15
    else:  # from_unit == "K"
        kelvin = value

    # Step 2: Convert from Kelvin to target unit
    if to_unit == "C":
        return kelvin - 273.15
    elif to_unit == "F":
        return (kelvin - 273.15) * 9 / 5 + 32
    else:  # to_unit == "K"
        return kelvin


def celsius_to_fahrenheit(celsius: float) -> float:
    """[Summary]: Convert temperature from Celsius to Fahrenheit.

    [Description]: Converts a temperature value from Celsius scale to Fahrenheit
    scale using the standard conversion formula.

    [Usage]: Typical usage example:

        result = celsius_to_fahrenheit(0)
        print(result)  # Output: 32.0
    """
    return temperature_converter(celsius, "C", "F")


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    """[Summary]: Convert temperature from Fahrenheit to Celsius.

    [Description]: Converts a temperature value from Fahrenheit scale to Celsius
    scale using the standard conversion formula.

    [Usage]: Typical usage example:

        result = fahrenheit_to_celsius(32)
        print(result)  # Output: 0.0
    """
    return temperature_converter(fahrenheit, "F", "C")


def celsius_to_kelvin(celsius: float) -> float:
    """[Summary]: Convert temperature from Celsius to Kelvin.

    [Description]: Converts a temperature value from Celsius scale to Kelvin
    scale using the standard conversion formula.

    [Usage]: Typical usage example:

        result = celsius_to_kelvin(0)
        print(result)  # Output: 273.15
    """
    return temperature_converter(celsius, "C", "K")


def kelvin_to_celsius(kelvin: float) -> float:
    """[Summary]: Convert temperature from Kelvin to Celsius.

    [Description]: Converts a temperature value from Kelvin scale to Celsius
    scale using the standard conversion formula.

    [Usage]: Typical usage example:

        result = kelvin_to_celsius(273.15)
        print(result)  # Output: 0.0
    """
    return temperature_converter(kelvin, "K", "C")


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    """[Summary]: Convert temperature from Fahrenheit to Kelvin.

    [Description]: Converts a temperature value from Fahrenheit scale to Kelvin
    scale using the standard conversion formula.

    [Usage]: Typical usage example:

        result = fahrenheit_to_kelvin(32)
        print(result)  # Output: 273.15
    """
    return temperature_converter(fahrenheit, "F", "K")


def kelvin_to_fahrenheit(kelvin: float) -> float:
    """[Summary]: Convert temperature from Kelvin to Fahrenheit.

    [Description]: Converts a temperature value from Kelvin scale to Fahrenheit
    scale using the standard conversion formula.

    [Usage]: Typical usage example:

        result = kelvin_to_fahrenheit(273.15)
        print(result)  # Output: 32.0
    """
    return temperature_converter(kelvin, "K", "F")
