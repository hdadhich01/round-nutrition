from .util import _vmo


def calcium(quantity: "int|str") -> str:
    """Round a calcium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded calcium quantity.
    """
    return _vmo(quantity, 10, "mg")


def potassium(quantity: "int|str") -> str:
    """Round a potassium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded potassium quantity.
    """
    return _vmo(quantity, 10, "mg")


def phosphorus(quantity: "int|str") -> str:
    """Round a phosphorus quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded phosphorus quantity.
    """
    return _vmo(quantity, 10, "mg")


def magnesium(quantity: "int|str") -> str:
    """Round a magnesium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded magnesium quantity.
    """
    return _vmo(quantity, 5, "mg")


def iron(quantity: "int|str") -> str:
    """Round an iron quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded iron quantity.
    """
    return _vmo(quantity, 0.1, "mg")


def zinc(quantity: "int|str") -> str:
    """Round a zinc quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded zinc quantity.
    """
    return _vmo(quantity, 0.1, "mg")


def copper(quantity: "int|str") -> str:
    """Round a copper quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded copper quantity.
    """
    return _vmo(quantity, 0.1, "mg")


def manganese(quantity: "int|str") -> str:
    """Round a manganese quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded manganese quantity.
    """
    return _vmo(quantity, 0.1, "mg")


def iodine(quantity: "int|str") -> str:
    """Round a iodine quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded iodine quantity.
    """
    return _vmo(quantity, 1, "mcg")


def selenium(quantity: "int|str") -> str:
    """Round a selenium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded selenium quantity.
    """
    return _vmo(quantity, 1, "mcg")


def chromium(quantity: "int|str") -> str:
    """Round a chromium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded chromium quantity.
    """
    return _vmo(quantity, 1, "mcg")


def molybdenum(quantity: "int|str") -> str:
    """Round a molybdenum quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded molybdenum quantity.
    """
    return _vmo(quantity, 1, "mcg")
