class BankAccount:
    def __init__(self, account_number, balance=0.0):
        """Initialize the bank account with an account number and balance."""
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance is ${self.balance:.2f}.")
        else:
            print("Invalid deposit amount. Please enter a positive number.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. New balance is ${self.balance:.2f}.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount. Please enter a positive number.")

    def check_balance(self):
        """Check and display the current balance."""
        print(f"Your current balance is: ${self.balance:.2f}")

# Create a bank account object with an example account number and initial balance
account = BankAccount(account_number="11", balance=100.0)

def main():
    """Main function to interact with the bank account."""
    print("Welcome to the Bank Account Management System!")
    
    while True:
        # Ask the user to enter their account number
        user_account_number = input("What is your account number? ")

        if user_account_number == account.account_number:
            print("Account verified!")

            while True:
                # Display menu options
                print("\nWhat would you like to do?")
                print("1. Check Balance")
                print("2. Deposit")
                print("3. Withdraw")
                print("4. Exit")

                user_choice = input("Enter the number of your choice: ")

                if user_choice == '1':
                    account.check_balance()

                elif user_choice == '2':
                    try:
                        amount = float(input("Enter the amount to deposit: "))
                        account.deposit(amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                elif user_choice == '3':
                    try:
                        amount = float(input("Enter the amount to withdraw: "))
                        account.withdraw(amount)
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                elif user_choice == '4':
                    print("Thank you for using the Bank Account Management System. Goodbye!")
                    break

                else:
                    print("Invalid choice. Please try again.")

            # Break out of the main loop after exiting the inner loop
            break
        else:
            print("Incorrect account number. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
