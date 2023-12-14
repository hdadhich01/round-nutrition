from .util import _carb, _fat, _sod_pot, parse_quantity, round_increment


def calories(quantity: "int|str") -> str:
    """Round a calories quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded calories quantity.
    """
    value, unit = parse_quantity(quantity)
    if value is None or value < 5:
        return f"0{unit}"
    elif value <= 50:
        return f"{round_increment(value, 5)}{unit}"
    return f"{round_increment(value, 10)}{unit}"


def total_fat(quantity: "int|str") -> str:
    """Round a total fat quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded total quantity.
    """
    return _fat(quantity)


tot_fat = total_fat


def sat_fat(quantity: "int|str") -> str:
    """Round a saturated fat quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded saturated quantity.
    """
    return _fat(quantity)


def trans_fat(quantity: "int|str") -> str:
    """Round a trans-unsaturated fat quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded trans-unsaturated quantity.
    """
    return _fat(quantity)


def poly_fat(quantity: "int|str") -> str:
    """Round a polyunsaturated fat quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded monounsaturated quantity.
    """
    return _fat(quantity)


def mono_fat(quantity: "int|str") -> str:
    """Round a monounsaturated fat quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded monounsaturated quantity.
    """
    return _fat(quantity)


def cholesterol(quantity: "int|str", minimal: bool = False) -> str:
    """Round a cholesterol quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded cholesterol quantity.
    """
    value, unit = parse_quantity(quantity)
    unit = "mg" if unit.strip() == "" else unit
    if value < 2:
        return f"0{unit}"
    elif value < 5:
        return f"<5{unit}" if minimal else f"less than 5{unit}"
    return f"{round_increment(value, 5)}{unit}"


def sodium(quantity: "int|str") -> str:
    """Round a sodium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded sodium quantity.
    """
    return _sod_pot(quantity)


def potassium(quantity: "int|str") -> str:
    """Round a potassium quantity.

    Args:
        quantity (int|str): The quantity to be rounded.

    Returns:
        str: The rounded potassium quantity.
    """
    return _sod_pot(quantity)


def total_carb(quantity: "int|str", minimal: bool = False) -> str:
    """Round a total carbohydrate quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded total carbohydrate quantity.
    """
    return _carb(quantity, minimal)


tot_carb = total_carb


def dietary_fiber(quantity: "int|str", minimal: bool = False) -> str:
    """Round a dietary fiber quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded dietary fiber quantity.
    """
    return _carb(quantity, minimal)


diet_fiber = dietary_fiber


def soluble_fiber(quantity: "int|str", minimal: bool = False) -> str:
    """Round a soluble fiber quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded soluble fiber quantity.
    """
    return _carb(quantity, minimal)


sol_fiber = soluble_fiber


def insoluble_fiber(quantity: "int|str", minimal: bool = False) -> str:
    """Round an insoluble fiber quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded insoluble fiber quantity.
    """
    return _carb(quantity, minimal)


insol_fiber = insoluble_fiber


def total_sugars(quantity: "int|str", minimal: bool = False) -> str:
    """Round a total sugars quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded total sugars quantity.
    """
    return _carb(quantity, minimal)


tot_sugars = total_sugars


def added_sugars(quantity: "int|str", minimal: bool = False) -> str:
    """Round an added sugars quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded added sugars quantity.
    """
    return _carb(quantity, minimal)


add_sugars = added_sugars


def sugar_alcohol(quantity: "int|str", minimal: bool = False) -> str:
    """Round a sugar alcohol quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded sugar alcohol quantity.
    """
    return _carb(quantity, minimal)


sugar_alc = sugar_alcohol


def other_carb(quantity: "int|str", minimal: bool = False) -> str:
    """Round an other carbohydrate quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded other carbohydrate quantity.
    """
    return _carb(quantity, minimal)


def protein(quantity: "int|str", minimal: bool = False) -> str:
    """Round a protein quantity.

    Args:
        quantity (int|str): The quantity to be rounded.
        minimal (bool, optional): Indicate whether to return in minimal format. Defaults to False.

    Returns:
        str: The rounded protein quantity.
    """
    value, unit = parse_quantity(quantity)
    unit = "g" if unit.strip() == "" else unit
    if value < 0.5:
        return f"0{unit}"
    elif value < 1:
        return f"1{unit}" if minimal else f"less than 1{unit}"
    return f"{round_increment(value, 1)}{unit}"
