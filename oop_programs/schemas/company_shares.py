import datetime


class CompanyShares:
    def __init__(self, stock_symbol, number_of_shares, price_per_share, dt):
        self.stock_symbol: str = stock_symbol
        self.number_of_shares: int = int(number_of_shares)
        self.price_per_share: int = int(price_per_share)
        self.date: str = dt

    def calculate_share_price(self, no_of_share: int):
        return no_of_share * self.price_per_share

    def to_dict(self):
        return {
            "stock_symbol": self.stock_symbol,
            "number_of_shares": self.number_of_shares,
            "price_per_share": self.price_per_share,
            "date": self.date
        }

    def __repr__(self):
        return f"CompanyShares(stock symbol={self.stock_symbol}, no. of shares={self.number_of_shares}, date={self.date})"
