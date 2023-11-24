class Kilogram:
    _name = "kilogram"
    _alias = "kg"
    _amount = 1000

    def __init__(self, amount: float | int):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "kg" | "kilogram":
                return self.amount
            case "g" | "gramm":
                return self.amount * self._amount


class Gramm:
    _name = "gramm"
    _alias = "g"
    _amount = 1000

    def __init__(self, amount: float | int):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "g" | "gramm":
                return self.amount
            case "kg" | "kilogram":
                return self.amount / self._amount


def get_aliases() -> list:
    import inspect
    import sys

    aliases_list = {}

    for _, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass):
        am = obj.__class__.__getattribute__(obj, "_amount")
        aliases_list[(obj.__class__.__getattribute__(obj, "_alias"))] = am

    al = sorted(aliases_list.items(), key=lambda a: a[1])

    return [a for a in dict(al).keys()]
