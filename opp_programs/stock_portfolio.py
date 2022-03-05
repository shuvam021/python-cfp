import json

"""Q. 3"""


class Stock:
    def __init__(self, name, num_of_share, price):
        self.name: str = name
        self.num_of_share: int = int(num_of_share)
        self.price: float = float(price)

    @property
    def stock_total_price(self):
        return round(self.price * self.num_of_share, 2)

    @property
    def to_dict(self):
        return {
            "name": self.name,
            "num_of_share": self.num_of_share,
            "price": self.price,
            "stock_total_price": self.stock_total_price
        }


class StockPortfolio:
    def __init__(self):
        self.stock_list: list[dict] = []

    def add_stock(self, data: Stock) -> None:
        self.stock_list.append(data.to_dict)

    def report(self):
        print(json.dumps(self.stock_list, indent=4))


if __name__ == '__main__':
    sp = StockPortfolio()

    sp.add_stock(Stock('company A', 2000, 600))
    sp.add_stock(Stock('company B', 50000, 200))
    sp.add_stock(Stock('company c', 20000, 150))

    sp.report()
