from .util import _vmo


def choline(quantity: "int|str") -> str:
    return _vmo(quantity, 10, "mg")
