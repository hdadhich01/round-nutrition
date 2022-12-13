from .util import _vmo


def calcium(quantity: "int|str") -> str:
    return _vmo(quantity, 10, "mg")


def potassium(quantity: "int|str") -> str:
    return _vmo(quantity, 10, "mg")


def phosphorus(quantity: "int|str") -> str:
    return _vmo(quantity, 10, "mg")


def magnesium(quantity: "int|str") -> str:
    return _vmo(quantity, 5, "mg")


def iron(quantity: "int|str") -> str:
    return _vmo(quantity, 0.1, "mg")


def zinc(quantity: "int|str") -> str:
    return _vmo(quantity, 0.1, "mg")


def copper(quantity: "int|str") -> str:
    return _vmo(quantity, 0.1, "mg")


def manganese(quantity: "int|str") -> str:
    return _vmo(quantity, 0.1, "mg")


def iodine(quantity: "int|str") -> str:
    return _vmo(quantity, 1, "mcg")


def selenium(quantity: "int|str") -> str:
    return _vmo(quantity, 1, "mcg")


def chromium(quantity: "int|str") -> str:
    return _vmo(quantity, 1, "mcg")


def molybdenum(quantity: "int|str") -> str:
    return _vmo(quantity, 1, "mcg")
