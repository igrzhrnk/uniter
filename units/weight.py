class Weight:
    def __init__(self, amount: float, unit_name: str):
        self.amount = amount
        self.unit_name = unit_name
    
    
    def __weight_units(self, u: str) -> int:
        res = 0
        match u:
            case "g" | "gramm":
                res = 1
            case "kg" | "kilogram":
                res = 3
        
        return res


    def convert_to(self, unit_name: str):
        res = 0.0

        if self.__weight_units(unit_name) == self.__weight_units(self.unit_name):
            res = self.amount
        elif self.__weight_units(unit_name) < self.__weight_units(self.unit_name):
            res = self.amount * (10**self.__weight_units(self.unit_name))
        else:
            res = self.amount / (10**self.__weight_units(unit_name))

        return res