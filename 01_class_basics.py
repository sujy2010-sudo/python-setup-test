class BankAccount:
    """Bank account class"""

    def __init__(self, account_number: str, account_holder: str, initial_balance: float):
        # TODO: Initialize attributes
        self._account_number =account_number
        self._account_holder=account_holder
        self._initial_balance =initial_balance

    def deposit(self, amount: float):
        # TODO: Implement deposit with validation
        self._amount=amount

    def withdraw(self, amount: float) -> bool:
        # TODO: Implement withdraw with validation
        # Return True if successful, False otherwise
        self._amount=amount

    def get_balance(self) -> float:
        # TODO: Return balance
        return self._initial_balance

    def get_account_number(self) -> str:
        # TODO: Return account number
        return self._account_number

    def __str__(self) -> str:
        # TODO: Return string representation
        return (f"account_number is '{self._account_number}'account_holder is '{self._account_holder}' initial_balance is  '{self._initial_balance}'")

# Test your class:
account = BankAccount("ACC001", "John Doe", 1000)
print(account)
account.deposit(500)
print(f"Balance: ${account.get_balance():,.2f}")
account.withdraw(300)
print(f"Balance: ${account.get_balance():,.2f}")
account.withdraw(2000)  # Should fail
