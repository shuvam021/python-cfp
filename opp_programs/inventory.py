import json
import os

"""Q 1, 2"""


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


class InventoryWrapper:
    file = '../assets/inventory.json'

    def __init__(self):
        self.records: list = []

    def insert(self):
        if not os.path.exists(self.file):
            raise FileNotFoundError

        with open(self.file) as f:
            data = json.load(f)
        for item in data:
            self.records.append(Inventory(**item))

    def print_records(self):
        print(json.dumps([i.to_dict for i in self.records], indent=4))


if __name__ == '__main__':
    iw = InventoryWrapper()
    iw.insert()
    iw.print_records()
