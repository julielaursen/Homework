#define main function
def main():
    #gather weight from user input
    weight = float(input("Please enter the weight of the package "))
    #call function calculate with parameter weight
    calculate(weight)    

#define function calculate
def calculate(weight):
    #assign rate to 0
    rate = 0.00

    #if weight > 10 set rate variable to 1.10 and print outcome
    if(weight > 10):
        rate = 1.10
        print("Shipping charges are $", format(rate, '.2f'))
    elif(weight > 6 and weight <= 10):
        rate = 3.70
        print("Shipping charges are $", format(rate, '.2f'))
    elif(weight > 2 and weight <= 6):
        rate = 2.20
        print("Shipping charges are $", format(rate, '.2f'))
    else:#(weight <= 2):
        rate = 3.80
        print("Shipping charges are $", format(rate, '.2f'))

#call main function
main()


