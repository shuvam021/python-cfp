import json
from oop_programs.schemas import Stock


class StockPortfolio:
    def __init__(self):
        self.stock_list: list[dict] = []

    def add_stock(self, data: Stock) -> None:
        self.stock_list.append(data.to_dict)

    def report(self):
        print(json.dumps(self.stock_list, indent=4))


if __name__ == '__main__':
    """Q. 3"""

    sp = StockPortfolio()

    sp.add_stock(Stock('company A', 2000, 600))
    sp.add_stock(Stock('company B', 50000, 200))
    sp.add_stock(Stock('company c', 20000, 150))

    sp.report()
