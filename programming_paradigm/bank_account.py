# bank_account.py
"""Simple BankAccount class demonstrating basic OOP and encapsulation."""

from typing import Union

class BankAccount:
    """A minimal bank account class."""

    def __init__(self, initial_balance: Union[int, float] = 0.0):
        """Initialize the account with an optional starting balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        # underscore indicates 'private' attribute (encapsulation)
        self._account_balance = float(initial_balance)

    def deposit(self, amount: Union[int, float]) -> None:
        """Add amount to the account. Raises ValueError for non-positive amounts."""
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self._account_balance += float(amount)

    def withdraw(self, amount: Union[int, float]) -> bool:
        """
        Attempt to withdraw amount.
        Returns True if successful, False if insufficient funds.
        Raises ValueError for non-positive amounts.
        """
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        amount = float(amount)
        if amount <= self._account_balance:
            self._account_balance -= amount
            return True
        return False

    def display_balance(self) -> None:
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self._account_balance:.2f}")
