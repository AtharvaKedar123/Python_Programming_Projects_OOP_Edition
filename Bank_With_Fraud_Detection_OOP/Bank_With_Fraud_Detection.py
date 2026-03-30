class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} deposited ₹{amount}. Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > 50000:
            print("⚠ Fraud Alert: Large transaction detected")

        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. Balance: ₹{self.balance}")


class SavingsAccount(Account):
    def __init__(self, name, balance=0, limit=3):
        super().__init__(name, balance)
        self.limit = limit
        self.withdrawals = 0

    def withdraw(self, amount):
        if self.withdrawals >= self.limit:
            print("Withdrawal limit reached")
            return

        if amount > 50000:
            print("⚠ Fraud Alert: Large transaction detected")

        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            self.withdrawals += 1
            print(f"{self.name} withdrew ₹{amount}. Balance: ₹{self.balance}")


class CurrentAccount(Account):
    def __init__(self, name, balance=0, overdraft=20000):
        super().__init__(name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > 50000:
            print("⚠ Fraud Alert: Large transaction detected")

        if amount > self.balance + self.overdraft:
            print("Overdraft limit exceeded")
        else:
            self.balance -= amount
            print(f"{self.name} withdrew ₹{amount}. Balance: ₹{self.balance}")


if __name__ == "__main__":
    acc1 = SavingsAccount("Atharva", 60000)
    acc2 = CurrentAccount("Business", 20000)

    acc1.deposit(10000)
    acc1.withdraw(20000)
    acc1.withdraw(20000)
    acc1.withdraw(10000)
    acc1.withdraw(5000)

    print()

    acc2.deposit(5000)
    acc2.withdraw(30000)
    acc2.withdraw(50000)