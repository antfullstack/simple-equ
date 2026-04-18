import pytest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT))
from simple_equ.physics import temperature_converter


class TestTemperatureConverterGeneric:
    """Test suite for the generic temperature_converter function."""

    @pytest.mark.parametrize(
        "value,from_unit,to_unit,expected",
        [
            # Celsius to Fahrenheit
            (0, "C", "F", 32.0),
            (100, "C", "F", 212.0),
            (-40, "C", "F", -40.0),
            (25, "C", "F", 77.0),
            (37, "C", "F", 98.6),
            # Fahrenheit to Celsius
            (32, "F", "C", 0.0),
            (212, "F", "C", 100.0),
            (-40, "F", "C", -40.0),
            (98.6, "F", "C", 37.0),
            # Celsius to Kelvin
            (0, "C", "K", 273.15),
            (25, "C", "K", 298.15),
            (-273.15, "C", "K", 0.0),
            (100, "C", "K", 373.15),
            # Kelvin to Celsius
            (273.15, "K", "C", 0.0),
            (298.15, "K", "C", 25.0),
            (373.15, "K", "C", 100.0),
            (0, "K", "C", -273.15),
            # Fahrenheit to Kelvin
            (32, "F", "K", 273.15),
            (212, "F", "K", 373.15),
            (-459.67, "F", "K", 0.0),
            # Kelvin to Fahrenheit
            (273.15, "K", "F", 32.0),
            (373.15, "K", "F", 212.0),
            (0, "K", "F", -459.67),
            # Same unit conversions
            (25, "C", "C", 25.0),
            (77, "F", "F", 77.0),
            (298.15, "K", "K", 298.15),
        ],
    )
    def test_temperature_converter(value, from_unit, to_unit, expected):
        """[Summary]: Verify temperature conversions between all unit combinations.

        [Description]: Tests all valid conversion paths (C→F, C→K, F→C, F→K, K→C, K→F)
        using well-known reference points including freezing point of water, boiling point,
        body temperature, absolute zero, and same-unit conversions.
        """
        result = temperature_converter(value, from_unit, to_unit)
        assert result == pytest.approx(expected, rel=1e-9)

    @pytest.mark.parametrize(
        "value,from_unit,to_unit",
        [
            (25, "X", "C"),
            (25, "C", "X"),
            (25, "celsius", "fahrenheit"),
        ],
    )
    def test_temperature_converter_invalid_units(value, from_unit, to_unit):
        """[Summary]: Verify that invalid units raise ValueError.

        [Description]: Tests that the function properly validates input units and
        raises ValueError for unsupported unit names.
        """
        with pytest.raises(ValueError):
            temperature_converter(value, from_unit, to_unit)

    def test_temperature_converter_case_insensitive(self):
        """[Summary]: Verify that unit parameters are case-insensitive.

        [Description]: Tests that the converter accepts units in both uppercase
        and lowercase (c, f, k variations).
        """
        assert temperature_converter(0, "c", "f") == pytest.approx(32.0, rel=1e-9)
        assert temperature_converter(0, "C", "f") == pytest.approx(32.0, rel=1e-9)
        assert temperature_converter(0, "c", "F") == pytest.approx(32.0, rel=1e-9)

    def test_temperature_converter_negative_values(self):
        """[Summary]: Verify conversions work correctly with negative temperatures.

        [Description]: Tests that the converter properly handles negative temperature
        values across different unit systems.
        """
        assert temperature_converter(-10, "C", "F") == pytest.approx(14.0, rel=1e-9)
        assert temperature_converter(-20, "C", "K") == pytest.approx(253.15, rel=1e-9)


class TestSpecificConverters:
    """Test suite for convenience converter functions."""

    def test_celsius_to_fahrenheit(self):
        """[Summary]: Verify celsius_to_fahrenheit conversion function.

        [Description]: Tests the dedicated Celsius to Fahrenheit converter using
        well-known reference points.
        """
        from simple_equ.physics import celsius_to_fahrenheit
        assert celsius_to_fahrenheit(0) == pytest.approx(32.0, rel=1e-9)
        assert celsius_to_fahrenheit(100) == pytest.approx(212.0, rel=1e-9)
        assert celsius_to_fahrenheit(25) == pytest.approx(77.0, rel=1e-9)

    def test_fahrenheit_to_celsius(self):
        """[Summary]: Verify fahrenheit_to_celsius conversion function.

        [Description]: Tests the dedicated Fahrenheit to Celsius converter using
        well-known reference points.
        """
        from simple_equ.physics import fahrenheit_to_celsius
        assert fahrenheit_to_celsius(32) == pytest.approx(0.0, rel=1e-9)
        assert fahrenheit_to_celsius(212) == pytest.approx(100.0, rel=1e-9)
        assert fahrenheit_to_celsius(98.6) == pytest.approx(37.0, rel=1e-9)

    def test_celsius_to_kelvin(self):
        """[Summary]: Verify celsius_to_kelvin conversion function.

        [Description]: Tests the dedicated Celsius to Kelvin converter using
        well-known reference points.
        """
        from simple_equ.physics import celsius_to_kelvin
        assert celsius_to_kelvin(0) == pytest.approx(273.15, rel=1e-9)
        assert celsius_to_kelvin(25) == pytest.approx(298.15, rel=1e-9)
        assert celsius_to_kelvin(-273.15) == pytest.approx(0.0, rel=1e-9)

    def test_kelvin_to_celsius(self):
        """[Summary]: Verify kelvin_to_celsius conversion function.

        [Description]: Tests the dedicated Kelvin to Celsius converter using
        well-known reference points.
        """
        from simple_equ.physics import kelvin_to_celsius
        assert kelvin_to_celsius(273.15) == pytest.approx(0.0, rel=1e-9)
        assert kelvin_to_celsius(298.15) == pytest.approx(25.0, rel=1e-9)
        assert kelvin_to_celsius(373.15) == pytest.approx(100.0, rel=1e-9)

    def test_fahrenheit_to_kelvin(self):
        """[Summary]: Verify fahrenheit_to_kelvin conversion function.

        [Description]: Tests the dedicated Fahrenheit to Kelvin converter using
        well-known reference points.
        """
        from simple_equ.physics import fahrenheit_to_kelvin
        assert fahrenheit_to_kelvin(32) == pytest.approx(273.15, rel=1e-9)
        assert fahrenheit_to_kelvin(212) == pytest.approx(373.15, rel=1e-9)

    def test_kelvin_to_fahrenheit(self):
        """[Summary]: Verify kelvin_to_fahrenheit conversion function.

        [Description]: Tests the dedicated Kelvin to Fahrenheit converter using
        well-known reference points.
        """
        from simple_equ.physics import kelvin_to_fahrenheit
        assert kelvin_to_fahrenheit(273.15) == pytest.approx(32.0, rel=1e-9)
        assert kelvin_to_fahrenheit(373.15) == pytest.approx(212.0, rel=1e-9)
        assert kelvin_to_fahrenheit(0) == pytest.approx(-459.67, rel=1e-9)
