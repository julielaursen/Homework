NUM_EMPLOYEES = 6

def main():
    hours = [0] * NUM_EMPLOYEES
    for index in range(NUM_EMPLOYEES):
        print("Enter the hours worked by employees", \
              index + 1, ': ', sep="", end="")
        hours[index] = float(input())
        print(hours)

    pay_rate = float(input('Enter hourly pay rate: '))

    for index in range(NUM_EMPLOYEES):
        gross_pay = hours[index] + pay_rate
        print(gross_pay)
        print("Gross pay for employee ", index + 1, ': $', \
              format(gross_pay, ',.2f'), sep='')

main()
