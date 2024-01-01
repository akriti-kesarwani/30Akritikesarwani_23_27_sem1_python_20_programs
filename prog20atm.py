class Account:
    def __init__(self, account_number, pin, balance=1000):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        return self.balance

    def withdraw_cash(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return amount
        else:
            return "Insufficient funds or invalid amount"

    def __str__(self):
        return f"Account Number: {self.account_number}, Balance: ${self.balance}"


class Transaction:
    @staticmethod
    def perform_transaction(user, pin, action, amount=None):
        if user.pin == pin:
            if action == "balance":
                return user.check_balance()
            elif action == "withdraw" and amount is not None:
                return user.withdraw_cash(amount)
            else:
                return "Invalid action or amount"
        else:
            return "Invalid PIN"


class User:
    def __init__(self, name, account):
        self.name = name
        self.account = account

    def __str__(self):
        return f"User: {self.name}\n{self.account}"


def main():
    # Take user input for name
    user_name = input("Enter your name: ")

    # Create an account
    account1 = Account(account_number="123456789", pin="1234", balance=1000)

    # Create a user
    user1 = User(name=user_name, account=account1)

    print(f"\n{user1}\n")

    # Take user input for PIN verification
    pin_attempt = input("Enter your PIN: ")

    # Perform transactions
    if Transaction.perform_transaction(user1.account, pin_attempt, "balance") == "Invalid PIN":
        print("Invalid PIN. Exiting.")
    else:
        while True:
            print("\n1. Check Balance\n2. Withdraw Cash\n3. Exit")
            choice = input("Enter your choice (1/2/3): ")

            if choice == "1":
                print("Checking balance:", Transaction.perform_transaction(user1.account, pin_attempt, "balance"))
            elif choice == "2":
                amount = float(input("Enter the amount to withdraw: "))
                result = Transaction.perform_transaction(user1.account, pin_attempt, "withdraw", amount)
                print(result if isinstance(result, str) else f"Withdrew ${result}. New balance: ${user1.account.balance}")
            elif choice == "3":
                print("Exiting. Thank you!")
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
