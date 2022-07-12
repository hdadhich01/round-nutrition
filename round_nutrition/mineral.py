from .utilities import vmo


class Mineral:
    def calcium(self, quantity: "int/str") -> str:
        return vmo(quantity, 10)

    def potassium(self, quantity: "int/str") -> str:
        return vmo(quantity, 10)

    def phosphorus(self, quantity: "int/str") -> str:
        return vmo(quantity, 10)

    def magnesium(self, quantity: "int/str") -> str:
        return vmo(quantity, 5)

    def iron(self, quantity: "int/str") -> str:
        return vmo(quantity, 0.1)

    def zinc(self, quantity: "int/str") -> str:
        return vmo(quantity, 0.1)

    def copper(self, quantity: "int/str") -> str:
        return vmo(quantity, 0.1)

    def manganese(self, quantity: "int/str") -> str:
        return vmo(quantity, 0.1)

    def iodine(self, quantity: "int/str") -> str:
        return vmo(quantity, 1)

    def selenium(self, quantity: "int/str") -> str:
        return vmo(quantity, 1)

    def chromium(self, quantity: "int/str") -> str:
        return vmo(quantity, 1)

    def molybdenum(self, quantity: "int/str") -> str:
        return vmo(quantity, 1)
