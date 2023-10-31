class Kilogram:
    _name = "kilogram"
    _alias = "kg"
    _amount = 1000

    def __init__(self, amount: float):
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

    def __init__(self, amount: float):
        self.amount = amount

    def convert_to(self, unit_name: str):
        match unit_name:
            case "g" | "gramm":
                return self.amount
            case "kg" | "kilogram":
                return self.amount / self._amount
