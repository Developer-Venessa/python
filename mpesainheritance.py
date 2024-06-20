class Account:
    def __init__(self,account_holder,balance):
        self.account_holder=account_holder
        self.balance=balance
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"{amount} deposited successfully.New balance is {self.balance}")
        else:
            print("Amount should be grater than zero")
    def withdraw(self,amount):

        if amount>self.balance:
            print("insufficient funds")
        else:
            self.balance -= amount
            print(f"{amount} withdrawn successfully.New balance is {self.balance}")
    def __str__(self):
        return f"Account holder:{self.account_holder}"

class SavingsAccount(Account):
    def __init__(self,account_holder,balance,interest_rate):
        super().__init__(account_holder,balance)
        self.interest_rate=interest_rate
    def add_interest(self):
        interest=self.balance*self.interest_rate/100
        self.balance+=interest
        print(f"interest added successfully.New balance is {self.balance}")
    def __str__(self):
        return ("savings Account holder:"
                f"{self.account_holder}\nBalance: {self.balance},"f"interest rate :{self.interest_rate}")
   # objects
mydetails=Account('Venessa Ayango',2000)
mydetails.deposit(100)
mydetails.withdraw(200)
print(mydetails)


savings=SavingsAccount('Damaris Etaba',8000,5)
savings.deposit(1000)
savings.withdraw(200)
savings.add_interest()
print(savings)