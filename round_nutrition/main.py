from .utilities import round_increment, parse_quantity


class Main:
    def calories(self, quantity: "int/str") -> str:
        value, unit = parse_quantity(quantity)
        if value is None or value < 5:
            return f"0{unit}"
        elif value <= 50:
            return f"{round_increment(value, 5)}{unit}"
        return f"{round_increment(value, 10)}{unit}"

    def _fat(self, quantity):
        value, unit = parse_quantity(quantity)
        unit = " g" if unit.strip() == "" else unit
        if value < 0.5:
            return f"0{unit}"
        elif value < 5:
            return f"{round_increment(value, 0.5)}{unit}"
        return f"{round_increment(value, 1)}{unit}"

    def tot_fat(self, quantity: "int/str") -> str:
        return self._fat(quantity)

    def sat_fat(self, quantity: "int/str") -> str:
        return self._fat(quantity)

    def trans_fat(self, quantity: "int/str") -> str:
        return self._fat(quantity)

    def poly_fat(self, quantity: "int/str") -> str:
        return self._fat(quantity)

    def mono_fat(self, quantity: "int/str") -> str:
        return self._fat(quantity)

    def cholesterol(self, quantity: "int/str", minimal: bool = False) -> str:
        value, unit = parse_quantity(quantity)
        unit = " mg" if unit.strip() == "" else unit
        if value < 2:
            return f"0{unit}"
        elif value < 5:
            result = f"{round_increment(value, 1)}{unit}"
            return result if minimal else f"less than{result}"
        return f"{round_increment(value, 5)}{unit}"

    def _sp(self, quantity):
        value, unit = parse_quantity(quantity)
        unit = " mg" if unit.strip() == "" else unit
        if value < 5:
            return f"0{unit}"
        elif value < 140:
            return f"{round_increment(value, 5)}{unit}"
        return f"{round_increment(value, 10)}{unit}"

    def sodium(self, quantity: "int/str") -> str:
        return self._sp(quantity)

    def potassium(self, quantity: "int/str") -> str:
        return self._sp(quantity)

    def _carb(self, quantity, minimal):
        value, unit = parse_quantity(quantity)
        if value < 0.5:
            return f"0{unit}"
        elif value < 1:
            return f"<1{unit}" if minimal else f"less than 1{unit}"
        return f"{round_increment(value, 1)}{unit}"

    def tot_carb(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def dietary_fiber(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def soluble_fiber(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def insoluble_fiber(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def tot_sugars(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def added_sugars(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def sugar_alcohol(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def other_carb(self, quantity: "int/str", minimal: bool = False) -> str:
        return self._carb(quantity, minimal)

    def protein(self, quantity: "int/str", minimal: bool = False) -> str:
        value, unit = parse_quantity(quantity)
        unit = " g" if unit.strip() == "" else unit
        if value < 0.5:
            return f"0{unit}"
        elif value < 1:
            return f"1{unit}" if minimal else f"less than 1{unit}"
        return f"{round_increment(value, 1)}{unit}"
