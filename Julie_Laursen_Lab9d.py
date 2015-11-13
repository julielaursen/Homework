import sys
     

def main():
    date = input("Please enter a date in the format mm/dd/yy: " )
    month = date[:2]
    month = int(month)
    day = date[3:5]
    day = int(day)
    year = date[6:]
    size = len(year)
    year = int(year)
    validate_date(date, month, day, year, size)
    

def validate_date(date, month, day, year, size):
    invalid = True
    while (size == 2):
        if (month > 12) or (month < 1):
            print("That month is invalid. Please re-enter a valid month.")
            invalid = True
            break
        if (day > 31) or (day < 1):
            print("That day is invalid. Please re-enter a valid day.")
            invalid = True
            break
        if year != 13:
            print("Year must be within 2013. Please re-enter a valid year.")
            invalid = True
            break
    else:
        print("Please enter year in the format yy")

    while(invalid):
        main()
    else:
        endProgram()


def endProgram():
    print("Thank you for playing")
    
    
main()
  
    #print string in long date format
 #   print("The year must be within 2013")

