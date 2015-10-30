class BankAccount:

    #the init method accepts an argument for the account's balance. it is assigned
    #to the __balance attribute.

    def __init__(self, bal):
        self.__balance = bal

    #the depost method makes a deposit into the account

    def deposit(self, amount):
        self.__balance += amount

    #the withdraw method withdraws an amount from the account

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance = self.__balance - amount
        else:
            print('Error: Insufficient funds')

    #get balance to return accont balance

    def get_balance(self):
        return self.__balance
    
