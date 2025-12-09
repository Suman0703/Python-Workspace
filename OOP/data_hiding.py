# Data Hiding means keeping the data of a class safe and protected from direct access.

class BankAccount:
    def __init__(self, name, balance):
        self.name = name          # public variable
        self._type = "Savings"    # protected variable
        self.__balance = balance  # private variable → data hiding

    # Getter method → safe access
    def get_balance(self):
        return self.__balance

    # Setter method → safe modify
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    # Setter method → safe modify
    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount


# Using the Class
acc = BankAccount("Suman", 1000)

print(acc.name)      # public → allowed
print(acc._type)     # protected → allowed but not recommended

print(acc.get_balance())  # private → accessed through method

# modifying private data safely
acc.deposit(500)
print(acc.get_balance())

acc.withdraw(200)
print(acc.get_balance())

# direct access to private variable → ERROR
print(acc.__balance)    # Not allowed (Data Hiding)
