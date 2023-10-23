from abc import ABC, abstractmethod
from user import User
from carrier import Carrier


class Cash:
    def __init__(self, account: int):
        self.account = account
        self.balance = 0


class ICashRepo(ABC):
    @abstractmethod
    def increase(self, cash: Cash, value: float) -> bool:
        pass

    @abstractmethod
    def decrease(self, cash: Cash, value: float) -> bool:
        pass


class CashRepository(ICashRepo):
    def __init__(self):
        self.repo = [Cash]

    def add_cash(self, cash: Cash) -> bool:
        if self.repo.append(cash):
            return True
        return False

    def increase(self, cash: Cash, value: float) -> bool:
        pass

    def decrease(self, cash: Cash, value: float) -> bool:
        pass


class CashProvider:
    def __init__(self):
        self.cash_repo = CashRepository()

    def check_balance(self, user: User, value: float) -> bool:
        for cash in self.cash_repo.repo:
            if cash.account == user.account:
                return cash.balance >= value
        return False

    def decrease_money(self, user: User | Carrier, value: float) -> bool:
        for cash in self.cash_repo.repo:
            if cash.account == user.account:
                cash.balance -= value
                return True
        return False

    def increase_money(self, carrier: Carrier | User, value: float) -> bool:
        for cash in self.cash_repo.repo:
            if cash.account == carrier.account:
                cash.balance += value
                return True
        return False
