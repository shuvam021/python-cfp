from abc import ABC, abstractmethod


class StockAccountABC(ABC):

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
