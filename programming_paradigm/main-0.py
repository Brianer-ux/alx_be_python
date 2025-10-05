# main-0.py
import sys
from bank_account import BankAccount

def format_amount(amount: float) -> str:
    """Return a user-friendly money string (no decimals for whole numbers)."""
    if float(amount).is_integer():
        return f"${int(amount)}"
    return f"${amount:.2f}"

def main():
    # Change the starting balance here if you want other tests
    account = BankAccount(100)  # Example starting balance

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # parse "command:amount" (amount optional for display)
    parts = sys.argv[1].split(':', 1)
    command = parts[0]
    amount = None
    if len(parts) == 2 and parts[1] != '':
        try:
            amount = float(parts[1])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)

    if command == "deposit" and amount is not None:
        try:
            account.deposit(amount)
            print(f"Deposited: {format_amount(amount)}")
        except ValueError as e:
            print(e)
    elif command == "withdraw" and amount is not None:
        try:
            if account.withdraw(amount):
                print(f"Withdrew: {format_amount(amount)}")
            else:
                print("Insufficient funds.")
        except ValueError as e:
            print(e)
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")
        print("Usage: python main-0.py <command>:<amount>  (commands: deposit, withdraw, display)")

if __name__ == "__main__":
    main()
