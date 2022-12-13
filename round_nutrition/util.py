from re import match


def parse_quantity(quantity):
    if quantity is None:
        return 0, ""
    elif type(quantity) in [int, float]:
        return quantity, ""
    quantity, found = quantity.strip(), match(r"\d+(\.\d+)?", quantity)
    if not found:
        raise ValueError(
            "A quantity can contain only the value, or both the value and unit"
        )
    parsed = found.group()
    unit = quantity[len(parsed) :].strip() if not quantity.isdigit() else ""
    value = float(parsed) if "." in parsed else int(parsed)
    return value, unit


def round_increment(value, increment):
    min_ = value // increment * increment
    max_ = min_ + increment
    res = max_ if (max_ - value) <= (value - min_) else min_
    return res if res % 1.0 else int(res)


# # https://stackoverflow.com/a/61212047/14767766
# def find_first_meaningful_decimal(x):
#   candidate = 0
#   MAX_DECIMAL = 10
#   EPSILON = 1 / 10 ** MAX_DECIMAL
#   while round(x, candidate) < EPSILON:
#       candidate += 1
#       if candidate > MAX_DECIMAL:
#           raise Exception(f"Number is too small: {s}")
#   if int(x * 10 ** (candidate + 1)) == 5:
#       candidate += 1
#   return candidate


# def round_increment(value, increment):
#   correction = 1e-5 if value > 0 else -1e-5
#   result = round(value / increment + correction) * increment
#   return round(result, find_first_meaningful_decimal(increment))


def _fat(quantity):
    value, unit = parse_quantity(quantity)
    unit = "g" if unit.strip() == "" else unit
    if value < 0.5:
        return f"0{unit}"
    elif value < 5:
        return f"{round_increment(value, 0.5)}{unit}"
    return f"{round_increment(value, 1)}{unit}"


def _carb(quantity, minimal):
    value, unit = parse_quantity(quantity)
    unit = "g" if unit.strip() == "" else unit
    if value < 0.5:
        return f"0{unit}"
    elif value < 1:
        return f"<1{unit}" if minimal else f"less than 1{unit}"
    return f"{round_increment(value, 1)}{unit}"


def _sod_pot(quantity):
    value, unit = parse_quantity(quantity)
    unit = "mg" if unit.strip() == "" else unit
    if value < 5:
        return f"0{unit}"
    elif value < 140:
        return f"{round_increment(value, 5)}{unit}"
    return f"{round_increment(value, 10)}{unit}"


def _vmo(quantity, increment, default_unit):
    value, unit = parse_quantity(quantity)
    unit = "mcg" if unit.strip() == "" else default_unit
    return f"{round_increment(value, increment)}{unit}"
