from .util import _vmo


def vitamin_c(quantity: "int|str"):
    """Round a vitamin C quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin C quantity.
    """
    return _vmo(quantity, 1, "mg")


vit_c = vitamin_c


def vitamin_e(quantity: "int|str"):
    """Round a vitamin E quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin E quantity.
    """
    return _vmo(quantity, 0.1, "mg")


vit_e = vitamin_e


def thiamine(quantity: "int|str"):
    """Round a thiamine/vitamin B12 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded thiamine/vitamin B12 quantity.
    """
    return _vmo(quantity, 0.1, "mg")


vitamin_b1 = vit_b1 = thiamine


def riboflavin(quantity: "int|str"):
    """Round a riboflavin/vitamin B2 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded riboflavin/vitamin B2 quantity.
    """
    return _vmo(quantity, 0.1, "mg")


vitamin_b2 = vit_b2 = riboflavin


def niacin(quantity: "int|str"):
    """Round a niacin/vitamin B3 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded niacin/vitamin B3 quantity.
    """
    return _vmo(quantity, 0.1, "mg")


vitamin_b3 = vit_b3 = niacin


def vitamin_b6(quantity: "int|str"):
    """Round a vitamin B6 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin B6 quantity.
    """
    return _vmo(quantity, 0.1, "mg")


vit_b6 = vitamin_b6


def pantothenic_acid(quantity: "int|str"):
    """Round a pantothenic acid/vitamin B5 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded pantothenic acid/vitamin B5 quantity.
    """
    return _vmo(quantity, 0.1, "mg")


panto_acid = vitamin_b5 = vit_b5 = pantothenic_acid


def vitamin_a(quantity: "int|str"):
    """Round a vitamin A quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin A quantity.
    """
    return _vmo(quantity, 10, "mcg")


vit_a = vitamin_a


def folate(quantity: "int|str"):
    """Round a folate/vitamin B9 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded folate/vitamin B9 quantity.
    """
    return _vmo(quantity, 5, "mcg")


vitamin_b9 = vit_b9 = folate


def vitamin_k(quantity: "int|str"):
    """Round a vitamin K quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin K quantity.
    """
    return _vmo(quantity, 1, "mcg")


vit_k = vitamin_k


def biotin(quantity: "int|str"):
    """Round a biotin/vitamin B7 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded biotin/vitamin B7 quantity.
    """
    return _vmo(quantity, 1, "mcg")


vitamin_b7 = vit_b7 = biotin


def vitamin_d(quantity: "int|str"):
    """Round a vitamin D quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin D quantity.
    """
    return _vmo(quantity, 0.1, "mcg")


vit_d = vitamin_d


def vitamin_b12(quantity: "int|str"):
    """Round a vitamin B12 quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded vitamin B12 quantity.
    """
    return _vmo(quantity, 10, "mcg")


vit_b12 = vitamin_b12
