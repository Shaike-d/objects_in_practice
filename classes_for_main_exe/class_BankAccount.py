class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.__balance = balance

    def deposit(self,num):
        self.__balance += num

    def withdraw(self,num):
        if num > self.__balance:
            raise ValueError("you dont have enough mani")
        self.__balance -= num
        
    def get_balance(self):
        return self.__balance

def answer_3():
    account = BankAccount("Dana", 100)
    account.deposit(50)
    try:
        account.withdraw(500)
    except ValueError as error:
        print("error:", error)
    print(account.get_balance())