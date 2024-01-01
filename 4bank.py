class Bank:
    def __init__(self):
        # Dictionary to store customer accounts with account numbers as keys
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        """Create a new customer account with the given account number and initial balance."""
        if account_number in self.accounts:
            print("Account already exists with this account number.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account created successfully for account number {account_number} with an initial balance of ${initial_balance:.2f}.")

    def deposit(self, account_number, amount):
        """Deposit money into a customer account."""
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(f"${amount:.2f} deposited successfully into account number {account_number}. New balance: ${self.accounts[account_number]:.2f}.")
        else:
            print("Account not found.")

    def withdraw(self, account_number, amount):
        """Withdraw money from a customer account."""
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(f"${amount:.2f} withdrawn successfully from account number {account_number}. New balance: ${self.accounts[account_number]:.2f}.")
            else:
                print("Insufficient funds.")
        else:
            print("Account not found.")

    def check_balance(self, account_number):
        """Check the balance of a customer account."""
        if account_number in self.accounts:
            print(f"Balance for account number {account_number}: ${self.accounts[account_number]:.2f}.")
        else:
            print("Account not found.")

def main():
    bank = Bank()

    while True:
        print("\nBank Management System")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "4":
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)

        elif choice == "5":
            print("Exiting the Bank Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
