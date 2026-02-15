class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self.balance



class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        return (self.balance * self.interest_rate) / 100



class CurrentAccount(Account):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    
    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print("Withdrawal successful (Overdraft allowed if needed).")
        else:
            print("Overdraft limit exceeded.")



if __name__ == "__main__":
   
    print("----- Savings Account -----")
    sa = SavingsAccount(101, 10000, 5)
    sa.deposit(2000)
    sa.withdraw(3000)
    print("Current Balance:", sa.get_balance())
    print("Interest:", sa.calculate_interest())

    print("\n----- Current Account -----")
    ca = CurrentAccount(202, 5000, 2000)
    ca.deposit(1000)
    ca.withdraw(6500)  # Uses overdraft
    print("Current Balance:", ca.get_balance())
    ca.withdraw(3000)  # Exceeds overdraft
