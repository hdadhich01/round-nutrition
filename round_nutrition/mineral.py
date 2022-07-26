from .utilities import vmo


class Mineral:
    def calcium(self, quantity: "int|str") -> str:
        return vmo(quantity, 10, "mg")

    def potassium(self, quantity: "int|str") -> str:
        return vmo(quantity, 10, "mg")

    def phosphorus(self, quantity: "int|str") -> str:
        return vmo(quantity, 10, "mg")

    def magnesium(self, quantity: "int|str") -> str:
        return vmo(quantity, 5, "mg")

    def iron(self, quantity: "int|str") -> str:
        return vmo(quantity, 0.1, "mg")

    def zinc(self, quantity: "int|str") -> str:
        return vmo(quantity, 0.1, "mg")

    def copper(self, quantity: "int|str") -> str:
        return vmo(quantity, 0.1, "mg")

    def manganese(self, quantity: "int|str") -> str:
        return vmo(quantity, 0.1, "mg")

    def iodine(self, quantity: "int|str") -> str:
        return vmo(quantity, 1, "mcg")

    def selenium(self, quantity: "int|str") -> str:
        return vmo(quantity, 1, "mcg")

    def chromium(self, quantity: "int|str") -> str:
        return vmo(quantity, 1, "mcg")

    def molybdenum(self, quantity: "int|str") -> str:
        return vmo(quantity, 1, "mcg")
