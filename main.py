from bank_account import BankAccount


def run_demo() -> None:
    account = BankAccount("Bartosz", 100)

    print("Created account:", account)

    print("\nDepositing £50...")
    account.deposit(50)
    print("Balance:", account.balance)

    print("\nWithdrawing £30...")
    account.withdraw(30)
    print("Balance:", account.balance)

    print("\nAttempting invalid withdrawal (too much)...")
    try:
        account.withdraw(1000)
    except ValueError as err:
        print("Error:", err)

    print("\nAttempting invalid deposit (negative)...")
    try:
        account.deposit(-10)
    except ValueError as err:
        print("Error:", err)

    print("\nFinal account state:", account)


if __name__ == "__main__":
    run_demo()