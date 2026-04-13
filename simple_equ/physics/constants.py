# Physics constants for unit conversions

# Conversion factors (base unit: meters)
METERS_TO_FEET = 3.280839895
METERS_TO_INCHES = 39.3700787

# Unit aliases for common abbreviations
UNIT_ALIASES = {
    'm': 'meters',
    'meter': 'meters',
    'ft': 'feet',
    'foot': 'feet',
    'in': 'inches',
    'inch': 'inches',
}

# Conversion factors dictionary (from: {to: factor})
CONVERSION_FACTORS = {
    'meters': {
        'feet': METERS_TO_FEET,
        'inches': METERS_TO_INCHES,
    },
    'feet': {
        'meters': 1 / METERS_TO_FEET,
        'inches': 12,  # 1 foot = 12 inches
    },
    'inches': {
        'meters': 1 / METERS_TO_INCHES,
        'feet': 1 / 12,
    },
}
