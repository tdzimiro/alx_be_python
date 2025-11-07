# main-0.py
# Command-line interface to interact with BankAccount.
# Usage examples:
#   python main-0.py deposit:50
#   python main-0.py withdraw:20
#   python main-0.py display

import sys
from bank_account import BankAccount

def main():
    # Create an account with an example starting balance of 100.0
    account = BankAccount(100.0)

    # If no command provided, print usage and exit
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # The first CLI argument after the script name
    entry = sys.argv[1]

    # Split the entry into command and optional parameter using ':' as the separator
    command, *params = entry.split(':')
    amount = None

    # If a parameter (amount) was provided, try converting to float with error handling
    if params and params[0] != "":
        try:
            amount = float(params[0])
        except ValueError:
            print("Invalid amount. Please provide a numeric value.")
            sys.exit(1)

    # Execute the requested command
    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: ${amount:.2f}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(f"Error: {e}")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Use: deposit:<amount>, withdraw:<amount>, or display")

if __name__ == "__main__":
    main()

