class Inventory:
    def __init__(self, name, weight, price_per_kg):
        self.name: str = name
        self.weight: float = float(weight)
        self.price_per_kg: float = float(price_per_kg)

    @property
    def total_price(self):
        return round(self.weight * self.price_per_kg, 2)

    @property
    def to_dict(self):
        return {
            'name': self.name,
            'weight': self.weight,
            'price_per_kg': self.price_per_kg,
            'total_price': self.total_price
        }

    def __repr__(self):
        return f"Inventory({self.name}, {self.weight}, {self.price_per_kg})"


