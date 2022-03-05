import json
import os
from oop_programs.schemas import Inventory


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
    """
    Q 1
    Q 2
    """
    iw = InventoryWrapper()
    iw.insert()
    iw.print_records()
