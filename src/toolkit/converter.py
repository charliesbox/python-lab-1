from .constants import TEMPERATURE_UNITS, UNITS


def find_group(unit: str) -> str:
    if unit in TEMPERATURE_UNITS:
        return 'temperature'
    for group_name, group_units in UNITS.items():
        if unit in group_units:
            return group_name
    raise ValueError(f"Unknown measurement unit: {unit}")


def convert(value: str, unit_from: str, unit_to: str) -> float:
    try:
        number = float(value)
    except ValueError:
        raise ValueError(f"Invalid numeric value: {value}")

    unit_from = unit_from.lower()
    unit_to = unit_to.lower()

    group = find_group(unit_from)
    if group != find_group(unit_to):
        raise ValueError(f"Incompatible units: {unit_from} and {unit_to}")

    if group == 'temperature':
        to_kelvin = TEMPERATURE_UNITS[unit_from][0]
        from_kelvin = TEMPERATURE_UNITS[unit_to][1]
        kelvin = to_kelvin(number)

        if kelvin < 0:
            raise ValueError("Temperature is below absolute zero.")
        return from_kelvin(kelvin)

    units = UNITS[group]
    return number * units[unit_from] / units[unit_to]
