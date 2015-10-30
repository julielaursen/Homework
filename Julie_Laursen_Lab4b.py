#calculate income rates with sales, bonus, comission
def income(sales):
    #calculate bonus and commission with sales > 1 million
    if (sales > 1000000):
        #assign bonus and commission rates
        bonus = 100000
        commission = .35
        #assign base rate, sales, commission and bonus to salary
        salary = 2000 + sales + bonus + (sales * commission)
    #calculate bonus and commission with sales betweeen 500,000 and 1 mil
    elif(sales >= 500001 and sales <= 1000000):
        bonus = 5000
        commission = .28
        #assign base rate, sales, commission and bonus to salary
        salary = 2000 + sales + bonus + (sales * commission)

    #calculate bonus and commission with sales between 100,000 and 500,000
    elif (sales >= 100001 and sales <= 500000):
        #assign bonus and commission rates
        bonus = 1000
        commission = .15
        #assign base rate, sales, commission and bonus to salary
        salary = 2000 + sales + bonus + (sales * commission)

    #calculate bonus and commission with sales between 10,000 and 100,000
    elif (sales >= 10000 and sales <= 100000):
        #assign bonus and commission rates
        commission = .02
        #assign base rate, sales, commission and bonus to salary
        salary = 2000 + sales + (sales * commission)

    #otherwise sales will be under 10k and no bonus or salary assigned
    else:
        #add base and sales to salary
        salary = 2000 + sales 
    #store the value of salary    
    return salary
    
#calculate income rates with sales and commission, no bonus
def calc_no_bonus(sales):
    bonus = 0
    #calculate bonus and commission with sales > 1 million
    if (sales > 1000000):
        #assign commission rates
        commission = .35
        #assign base rate, sales, and commission to salary
        salary = 2000 + sales + (sales * commission)
    #calculate bonus and commission with sales betweeen 500,000 and 1 mil
    elif(sales >= 500001 and sales <= 1000000):
        #assign commission rates
        commission = .28
        #assign base rate, sales, and commission to salary
        salary = 2000 + sales + (sales * commission)
    #calculate bonus and commission with sales between 100,000 and 500,000
    elif (sales >= 100001 and sales <= 500000):
        #assign commission rates
        commission = .15
        #assign base rate, sales, and commission to salary
        salary = 2000 + sales + (sales * commission)
    #calculate bonus and commission with sales between 10,000 and 100,000
    elif (sales >= 10000 and sales <= 100000):
        #assign commission rates
        commission = .02
        #assign base rate, sales, and commission to salary
        salary = 2000 + sales + (sales * commission)
    #otherwise sales will be under 10k and no bonus or salary assigned
    else:
        #assign base rate, sales, and commission to salary
        salary = 2000 + sales 
    #store the value of salary     
    return salary

#define main function
def main():
    #get variables name, sales, vacation and months from input 
    name = str(input("What is your name? "))
    sales = float(input("Input your annual sales: "))
    vacation = int(input("What is the greatest number of vacation days you've taken in a month? "))
    months = int(input("How many years have you been with the company? Please enter in number of months: "))
    #assign base to 2000
    base = 2000
    #set salary, bonus and cocmission so they can be called in main function
    salary = 0
    bonus= 0
    commission = 0
    #if number of months has been under 3 calculate salary without bonus
    if (months < 3):
        salary = calc_no_bonus(sales)
    #else calculate with bonus by calling income function
    else:
        salary = income(sales)
        #For salespeople who have been with the company for more than 5 years and who have made sales greater than $100,000 an additional bonus of $1000 is added
        if (months > 60 and sales > 100000):
            salary = income(sales) + 1000
            
        
    #If a salesperson has taken more than 3 vacation days in a month, their pay gets reduced
    #by $200
    if (vacation > 3):
        salary = income(sales) - 200 

    #print total salary
    print("Your total salary is $", format(salary, ',.2f'), sep='')
    #I would like to call the following, but I haven't figured out how to do it:
    #print("This consists of: \n your sales of $", format(sales, ',.2f'), sep='')
    #print("your base of $", base)
    #print("your bonus of $", bonus)
    #print("your commission of ", format(sales * commission, ',.2f'), sep='')
    
#call main function
main()

















