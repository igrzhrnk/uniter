class Kilometer:
    _name = "kilometer"
    _alias = "km"
    _amount = 1000

    def __init__(self, amount: float):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "km" | "kilometer":
                return self.amount
            case "m" | "meter":
                return self.amount * self._amount
            case "cm" | "cantimeter":
                return self.amount * self._amount * 100
            case "mm" | "millimeter":
                return self.amount * self._amount * 100 * 10


class Meter:
    _name = "meter"
    _alias = "m"
    _amount = 100

    def __init__(self, amount: float):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "km" | "kilometer":
                return self.amount / 1000
            case "m" | "meter":
                return self.amount
            case "cm" | "centimeter":
                return self.amount * 100
            case "mm" | "millimeter":
                return self.amount * 100 * 10


class Centimeter:
    _name = "centimeter"
    _alias = "cm"
    _amount = 100

    def __init__(self, amount: float):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "km" | "kilometer":
                return self.amount / (self._amount * 1000)
            case "m" | "meter":
                return self.amount / self._amount
            case "cm" | "centimeter":
                return self.amount
            case "mm" | "millimeter":
                return self.amount * 10


class Millimeter:
    _name = "millimeter"
    _alias = "mm"
    _amount = 10

    def __init__(self, amount: float):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "km" | "kilometer":
                return self.amount / (self._amount * 1000 * 100)
            case "m" | "meter":
                return self.amount / (self._amount * 100)
            case "cm" | "centimeter":
                return self.amount / self._amount
            case "mm" | "millimeter":
                return self.amount


def get_aliases() -> list:
    import inspect
    import sys

    aliases_list = {}

    for _, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        ai = obj.__class__.__getattribute__(obj, "_amount")
        aliases_list[(obj.__class__.__getattribute__(obj, "_alias"))] = ai

    al = sorted(aliases_list.items(), key=lambda a: a[1])

    return [a for a in dict(al).keys()]
