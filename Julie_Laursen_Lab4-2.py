#calculate income rates with sales, bonus, comission
def income(sales):
    if (sales > 1000000):
        bonus = 100000
        commission = .35
        salary = 2000 + sales + bonus + (sales * commission)

    elif(sales >= 500001 and sales <= 1000000):
        bonus = 5000
        commission = .28
        salary = 2000 + sales + bonus + (sales * commission)
 
    elif (sales >= 100001 and sales <= 500000):
        bonus = 1000
        commission = .15
        salary = 2000 + sales + bonus + (sales * commission)

    elif (sales >= 10000 and sales <= 100000):
        bonus = 0
        commission = .02
        salary = 2000 + sales + bonus + (sales * commission)

    else:
        bonus = 0
        commission = 0
        salary = 2000 + sales + bonus + (sales * commission)
        
    return (salary, bonus, commission)
    
#calculate income rates with sales and commission, no bonus
def calc_no_bonus(sales):
    bonus = 0
    if (sales > 1000000):
        commission = .35
        salary = 2000 + sales + (sales * commission)

    elif(sales >= 500001 and sales <= 1000000):
        commission = .28
        salary = 2000 + sales + (sales * commission)
 
    elif (sales >= 100001 and sales <= 500000):
        commission = .15
        salary = 2000 + sales + (sales * commission)

    elif (sales >= 10000 and sales <= 100000):
        commission = .02
        salary = 2000 + sales + (sales * commission)
    else:
        commission = 0
        salary = 2000 + sales + (sales * commission)
        
    return (salary, commission)

def main():
    name = str(input("What is your name? "))
    sales = float(input("Input your annual sales: "))
    vacation = int(input("How many vacation days have you taken? "))
    months = int(input("How many years have you been with the company? Please enter in number of months: "))
    base = 2000
    salary = 0
    bonus= 0
    commission = 0
    if (months < 3):
        salary = calc_no_bonus(sales)    
    else:
        salary, bonus, commission = income(sales)
        #For salespeople who have been with the company for more than 5 years and who have made sales greater than $100,000 an additional bonus of $1000 is added
        if (months > 60 and sales > 100000):
            salary = income(sales)
            
        
    #If a salesperson has taken more than 3 vacation days in a month, their pay gets reduced
    #by $200
    #if (vacation > 3):
     #   salary = income(sales) - 200 

    print("Your total salary is $", format(salary, ',.2f'), sep='')
    print("This consists of: \n your sales of $", format(sales, ',.2f'), sep='')
    print("your base of $", base)
    print("your bonus of $", bonus)
    print("your commission of ", format(sales * commission, ',.2f'), sep='')
    

main()

















