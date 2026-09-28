from collections.abc import Callable

UNITS: dict[str, dict[str, float]] = {
    'length' : {
        'mm': 0.001,
        'cm' : 0.01,
        'm' : 1,
        'km' : 1000
    },

    'weight' : {
        'g' : 0.001,
        'kg' : 1
    },
}

TEMPERATURE_UNITS: dict[str, tuple[Callable[[float], float], Callable[[float], float]]] = {
    'c': (lambda c: c + 273.15, lambda k: k - 273.15),
    'f': (lambda f: (f - 32) / 1.8 + 273.15, lambda k: (k - 273.15) * 1.8 + 32),
    'k': (lambda k: k, lambda k: k),
}
