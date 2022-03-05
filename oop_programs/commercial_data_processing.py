import datetime
import json
from typing import List

from oop_programs.abstracts import StockAccountABC
from oop_programs.schemas import CompanyShares
from utils import LinkedList


class StockAccount(StockAccountABC):
    def __init__(self):
        self.company_shares: List[CompanyShares] = []

    def stock_append(self, data: CompanyShares) -> None:
        self.company_shares.append(data)

    def value_of(self) -> float:
        total = 0
        for i in self.company_shares:
            total += float(i.number_of_shares * i.price_per_share)
        return total

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
            st.number_of_shares += amount
            print(
                f"""{st.calculate_share_price(amount)} amount debited against stock: "{st.stock_symbol}" on {datetime.datetime.now()}""")
        else:
            print("already exists")

    def sell(self, amount: int, symbol: str) -> None:
        if self.stock_exists(symbol, amount):
            st = self.get_stock(symbol)
            st.number_of_shares -= amount
            print(
                f"""{st.calculate_share_price(amount)} amount credited against stock: "{st.stock_symbol}" on {datetime.datetime.now()}""")
        else:
            print("already exists")

    def save(self, filename: str) -> None:
        data = [i.to_dict() for i in self.company_shares]
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)

    def print_report(self) -> None:
        for i in self.company_shares:
            print(i)


if __name__ == '__main__':
    FILE = "assets/stock_account.json"
    share1 = CompanyShares(
        'something',
        2000,
        500,
        str(datetime.datetime.now().date())
    )
    share2 = CompanyShares(
        'something again',
        5000,
        200,
        str(datetime.datetime.now().date())
    )

    # # Q. 4
    # sa = StockAccount()
    # sa.stock_append(share1)
    # sa.stock_append(share2)
    # sa.buy(500, share1.stock_symbol)  # 500 amount
    # sa.buy(20, share2.stock_symbol)  # 20 amount
    # sa.sell(1020, share2.stock_symbol)  # 20 amount
    # sa.print_report()
    # print(sa.value_of())
    # sa.save(FILE)

    # # Q. 5
    # ll = LinkedList()
    # ll.add(share1)
    # ll.add(share2)
    # print("pre-remove", ll.print_ll())
    # ll.remove(share1)
    # print("post-remove", ll.print_ll())
    # TODO: Q 6
    # TODO: Q 7
