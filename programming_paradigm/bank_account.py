"""bank_account.py

Defines a BankAccount class that encapsulates basic banking operations:
- deposit(amount)
- withdraw(amount)
- display_balance()
"""

class BankAccount:
    """A simple BankAccount class demonstrating encapsulation and basic operations."""

    def __init__(self, initial_balance: float = 0.0):
        """
        Initialize a new BankAccount.

        Parameters:
        - initial_balance (float): optional starting balance, defaults to 0.0

        The balance is stored in a "private" attribute __balance to encourage encapsulation.
        """
        # Use a private attribute name (name mangling) to discourage direct external access.
        self.__balance = float(initial_balance)

    def deposit(self, amount: float) -> None:
        """
        Deposit amount into the account.

        Raises:
        - ValueError: if amount is negative or not a number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Deposit amount must be a number.")
        amount = float(amount)
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount.")
        self.__balance += amount

    def withdraw(self, amount: float) -> bool:
        """
        Withdraw amount from the account if sufficient funds exist.

        Returns:
        - True if withdrawal succeeded (balance decreased).
        - False if insufficient funds (balance unchanged).

        Raises:
        - ValueError: if amount is negative or not a number.
        """
        if not isinstance(amount, (int, float)):
            raise ValueError("Withdrawal amount must be a number.")
        amount = float(amount)
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount.")

        if amount <= self.__balance:
            self.__balance -= amount
            return True
        else:
            return False

    def display_balance(self) -> None:
        """
        Print the current balance in a user-friendly format.
        """
        # Format with two decimal places for readability
        print(f"Current Balance: ${self.__balance:.2f}")

    # Optional: a safe accessor if external code needs to read the balance (keeps write access internal)
    def get_balance(self) -> float:
        """Return the current balance as a float (read-only accessor)."""
        return float(self.__balance)

