from re import match


def parse_quantity(quantity):
    if quantity is None:
        return 0, ""
    elif type(quantity) in [int, float]:
        return quantity, ""
    quantity = quantity.strip()
    parsed = match(r"\d+(\.\d+)?", quantity).group()
    unit = quantity[len(parsed) :].strip() if not quantity.isdigit() else ""
    value = float(parsed) if "." in parsed else int(parsed)
    return value, f" {unit}"


def round_increment(value, increment):
    minimum = value // increment * increment
    maximum = minimum + increment
    res = maximum if (maximum - value) <= (value - minimum) else minimum
    return res if res % 1.0 else int(res)


# # https://stackoverflow.com/a/61212047/14767766
# def find_first_meaningful_decimal(x):
#   candidate = 0
#   MAX_DECIMAL = 10
#   EPSILON = 1 / 10 ** MAX_DECIMAL
#   while round(x, candidate) < EPSILON:
#       candidate += 1
#       if candidate > MAX_DECIMAL:
#           raise Exception('Number is too small: {}'.format(x))
#   if int(x * 10 ** (candidate + 1)) == 5:
#       candidate += 1
#   return candidate


# def round_increment(value, increment):
#   correction = 1e-5 if x > 0 else -1e-5
#   result = round(value / increment + correction) * increment
#   return round(result, find_first_meaningful_decimal(increment))


def vmo(quantity, increment):
    value, unit = parse_quantity(quantity)
    unit = " mcg" if unit.strip() == "" else unit
    return f"{round_increment(value, increment)}{unit}"
