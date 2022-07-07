from re import match


def parse_quantity(quantity):
    if quantity is None:
        return 0
    elif type(quantity) in [int, float]:
        return quantity
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


class Main:
    def calories(self, quantity: "int/str") -> str:
        value, unit = parse_quantity(quantity)
        if value is None or value < 5:
            return f"0{unit}"
        elif value <= 50:
            return f"{round_increment(value, 5)}{unit}"
        return f"{round_increment(value, 10)}{unit}"

    def __fat(self, quantity):
        value, unit = parse_quantity(quantity)
        unit = " g" if unit.strip() == "" else unit
        if value < 0.5:
            return f"0{unit}"
        elif value < 5:
            return f"{round_increment(value, 0.5)}{unit}"
        return f"{round_increment(value, 1)}{unit}"

    def tot_fat(self, quantity: "int/str") -> str:
        return self.__fat(quantity)

    def sat_fat(self, quantity: "int/str") -> str:
        return self.__fat(quantity)

    def trans_fat(self, quantity: "int/str") -> str:
        return self.__fat(quantity)

    def poly_fat(self, quantity: "int/str") -> str:
        return self.__fat(quantity)

    def mono_fat(self, quantity: "int/str") -> str:
        return self.__fat(quantity)

    def cholesterol(self, quantity: "int/str", minimal: bool = False) -> str:
        value, unit = parse_quantity(quantity)
        unit = " mg" if unit.strip() == "" else unit
        if value < 2:
            return f"0{unit}"
        elif value < 5:
            result = f"{round_increment(value, 1)}{unit}"
            return result if minimal else f"less than{result}"
        return f"{round_increment(value, 5)}{unit}"

    def __sp(self, quantity):
        value, unit = parse_quantity(quantity)
        unit = " mg" if unit.strip() == "" else unit
        if value < 5:
            return f"0{unit}"
        elif value < 140:
            return f"{round_increment(value, 5)}{unit}"
        return f"{round_increment(value, 10)}{unit}"

    def sodium(self, quantity: "int/str") -> str:
        return self.__sp(quantity)

    def potassium(self, quantity: "int/str") -> str:
        return self.__sp(quantity)

    def __carb(self, quantity, minimal):
        value, unit = parse_quantity(quantity)
        if value < 0.5:
            return f"0{unit}"
        elif value < 1:
            return f"<1{unit}" if minimal else f"less than 1{unit}"
        return f"{round_increment(value, 1)}{unit}"

    def tot_carb(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def dietary_fiber(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def soluble_fiber(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def insoluble_fiber(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def tot_sugars(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def added_sugars(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def sugar_alcohol(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def other_carb(self, quantity: "int/str", minimal: bool = False) -> str:
        return self.__carb(quantity, minimal)

    def protein(self, quantity: "int/str", minimal: bool = False) -> str:
        value, unit = parse_quantity(quantity)
        unit = " g" if unit.strip() == "" else unit
        if value < 0.5:
            return f"0{unit}"
        elif value < 1:
            return f"1{unit}" if minimal else f"less than 1{unit}"
        return f"{round_increment(value, 1)}{unit}"


def vmo(quantity, increment):
    value, unit = parse_quantity(quantity)
    unit = " mcg" if unit.strip() == "" else unit
    return f"{round_increment(value, increment)}{unit}"
