from .utilities import vmo


class Vitamin:
    def vitamin_c(self, quantity: "int/str"):
        return vmo(quantity, 1)

    def vitamin_e(self, quantity: "int/str"):
        return vmo(quantity, 0.1)

    def thiamine(self, quantity: "int/str"):  # Vitamin B12
        return vmo(quantity, 0.1)

    def riboflavin(self, quantity: "int/str"):  # Vitamin B2
        return vmo(quantity, 0.1)

    def niacin(self, quantity: "int/str"):  # Vitamin B3
        return vmo(quantity, 0.1)

    def vitamin_b6(self, quantity: "int/str"):
        return vmo(quantity, 0.1)

    def pantothenic_acid(self, quantity: "int/str"):  # Vitamin B5
        return vmo(quantity, 0.1)

    def vitamin_a(self, quantity: "int/str"):
        return vmo(quantity, 10)

    def folate(self, quantity: "int/str"):  # Vitamin B9
        return vmo(quantity, 5)

    def vitamin_k(self, quantity: "int/str"):
        return vmo(quantity, 1)

    def biotin(self, quantity: "int/str"):  # Vitamin B7
        return vmo(quantity, 1)

    def vitamin_d(self, quantity: "int/str"):
        return vmo(quantity, 0.1)

    def vitamin_b12(self, quantity: "int/str"):
        return vmo(quantity, 10)
