from .utilities import vmo


class Vitamin:
    def vitamin_c(self, quantity: "int|str"):
        return vmo(quantity, 1, "mg")

    def vitamin_e(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mg")

    # Vitamin B12
    def thiamine(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mg")

    # Vitamin B2
    def riboflavin(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mg")

    # Vitamin B3
    def niacin(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mg")

    def vitamin_b6(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mg")

    # Vitamin B5
    def pantothenic_acid(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mg")

    def vitamin_a(self, quantity: "int|str"):
        return vmo(quantity, 10, "mcg")

    # Vitamin B9
    def folate(self, quantity: "int|str"):
        return vmo(quantity, 5, "mcg")

    def vitamin_k(self, quantity: "int|str"):
        return vmo(quantity, 1, "mcg")

    # Vitamin B7
    def biotin(self, quantity: "int|str"):
        return vmo(quantity, 1, "mcg")

    def vitamin_d(self, quantity: "int|str"):
        return vmo(quantity, 0.1, "mcg")

    def vitamin_b12(self, quantity: "int|str"):
        return vmo(quantity, 10, "mcg")
