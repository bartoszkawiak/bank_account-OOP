from __future__ import annotations


class BankAccount:
    """
    A simple bank account model to demonstrate:
    - Encapsulation (private attributes)
    - Validation via properties
    - Exception handling
    - Clear, testable methods
    """

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance  # uses the property setter

    @property
    def owner(self) -> str:
        return self._owner

    @owner.setter
    def owner(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError("Owner must be a string.")
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("Owner cannot be empty.")
        self._owner = cleaned

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        if not isinstance(value, (int, float)):
            raise TypeError("Balance must be a number.")
        if value < 0:
            raise ValueError("Balance cannot be negative.")
        self._balance = float(value)

    def deposit(self, amount: float) -> float:
        amount = self._validate_amount(amount)
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        amount = self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Insufficient funds.")
        self._balance -= amount
        return self._balance

    def _validate_amount(self, amount: float) -> float:
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number.")
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Amount must be greater than 0.")
        return amount

    def __repr__(self) -> str:
        return f"BankAccount(owner='{self.owner}', balance={self.balance:.2f})"