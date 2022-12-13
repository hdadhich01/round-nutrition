from .util import _vmo


def choline(quantity: "int|str") -> str:
    """Round a choline quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded choline quantity.
    """
    return _vmo(quantity, 10, "mg")
