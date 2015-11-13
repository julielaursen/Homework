import bankaccount

def main():
    #get the starting balance.
    start_bal = float(input('enter your starting balance: '))

    #create a bankaccount object
    savings = bankaccount.BankAccount(start_bal)

    #deposit the user's payheck
    pay = float(input("How muh were you paid this week? "))
    print("I will deposit that into your account")
    savings.deposit(pay)

    #display your balance
    print("Your acount balance is $", \
          format(savings.get_balance(), ',.2f'),
          sep = '')

    #get amout to withdraw
    cash = float(input("How much do you want to widthraw? "))
    print("I will withdraw that from your acount.")
    savings.withdraw(cash)

    #display the balance
    print("Your account balance is $", \
          format(savings.get_balance(), ',.2f'),
          sep='')

main()
