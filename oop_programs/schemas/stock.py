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


