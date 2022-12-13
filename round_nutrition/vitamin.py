from .util import _vmo


def vitamin_c(quantity: "int|str"):
    return _vmo(quantity, 1, "mg")


def vitamin_e(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mg")


# Vitamin B12
def thiamine(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mg")


# Vitamin B2
def riboflavin(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mg")


# Vitamin B3
def niacin(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mg")


def vitamin_b6(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mg")


# Vitamin B5
def pantothenic_acid(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mg")


def vitamin_a(quantity: "int|str"):
    return _vmo(quantity, 10, "mcg")


# Vitamin B9
def folate(quantity: "int|str"):
    return _vmo(quantity, 5, "mcg")


def vitamin_k(quantity: "int|str"):
    return _vmo(quantity, 1, "mcg")


# Vitamin B7
def biotin(quantity: "int|str"):
    return _vmo(quantity, 1, "mcg")


def vitamin_d(quantity: "int|str"):
    return _vmo(quantity, 0.1, "mcg")


def vitamin_b12(quantity: "int|str"):
    return _vmo(quantity, 10, "mcg")
