from abc import ABC, abstractmethod
import datetime
from typing import List

"""Q. 4"""
# TODO: Q.4 incomplete


class StockAccountABC(ABC):

    @abstractmethod
    def stock_account(self, filename: str) -> None:
        """create a new account from file"""
        pass

    @abstractmethod
    def value_of(self) -> float:
        """total value of account"""
        pass

    @abstractmethod
    def buy(self, amount: int, symbol: str) -> None:
        """add share of stock to account"""
        pass

    @abstractmethod
    def sell(self, amount: int, symbol: str) -> None:
        """subtract share of stock to account"""
        pass

    @abstractmethod
    def save(self, filename: str) -> None:
        """save account to file"""
        pass

    @abstractmethod
    def print_report(self) -> None:
        """print a dedicated report of stocks and value"""
        pass


class CompanyShares:
    def __init__(self, stock_symbol, number_of_shares, price_per_share, dt):
        self.stock_symbol: str = stock_symbol
        self.number_of_shares: int = int(number_of_shares)
        self.price_per_share: int = int(price_per_share)
        self.date: datetime = dt

    def calculate_share_price(self, no_of_share: int):
        return no_of_share * self.price_per_share

    def __repr__(self):
        return f"CompanyShares({self.stock_symbol}, {self.number_of_shares}, {self.date})"


class StockAccount(StockAccountABC):
    def __init__(self):
        self.company_shares: List[CompanyShares] = []

    def stock_append(self, data: CompanyShares) -> None:
        self.company_shares.append(data)

    def stock_account(self, filename: str) -> None:
        pass

    def value_of(self) -> float:
        pass

    def stock_exists(self, symbol: str, amount: int) -> bool:
        if symbol in [i.stock_symbol for i in self.company_shares if i.number_of_shares > 0]:
            return True
        return False

    def get_stock(self, symbol: str):
        for i in self.company_shares:
            if i.stock_symbol == symbol:
                return i
        return None

    def buy(self, amount: int, symbol: str) -> None:
        if self.stock_exists(symbol, amount):
            st = self.get_stock(symbol)
            st.number_of_shares -= amount
            print(f"""{st.calculate_share_price(amount)} amount debited against stock: "{st.stock_symbol}" on {datetime.datetime.now()}""")
        else:
            print("already exists")

    def sell(self, amount: int, symbol: str) -> None:
        pass

    def save(self, filename: str) -> None:
        pass

    def print_report(self) -> None:
        print(self.company_shares)


if __name__ == '__main__':
    sa = StockAccount()
    sa.stock_append(CompanyShares('something', 2000, 500, datetime.datetime.now().date()))
    sa.buy(500, "something")  # 500 amount

    print()
    sa.print_report()
