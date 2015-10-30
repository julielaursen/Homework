

import sys
     

def endProgram():
    print("Thank you for playing")
    
def main(): 
    if(validate day()):
        if validate_month():
            validate_year()

def validate_day():
    date = input("Please enter a date in the format mm/dd/yy: " )
    day = date[3:5]
    day = int(day)
    invalid = False
    if (day > 31) or (day < 1):
            invalid = True
            print("That day is invalid. Please re-enter a valid day.")
            break

    if(invalid):
        endProgram()
    else:
        main()

def validate_month():
    date = input("Please enter a date in the format mm/dd/yy: " )
    month = date[:2]
    month = int(month)
    invalid = False
    if (month > 12) or (month < 1):
        invalid = True
        print("That month is invalid. Please re-enter a valid month.")
        break
    
    if(invalid):
        endProgram()
    else:
        main()

def validate_year():
    date = input("Please enter a date in the format mm/dd/yy: " )
    year = date[6:]
    size = len(year)
    year = int(year)
    while (size == 2):
        if year != 13:
            invalid = True
            print("Year must be within 2013. Please re-enter a valid year.")
            break
    else:
        print("Please enter year in the format yy")

    if(invalid):
        endProgram()
    else:
        main()

    
main()
  
    #print string in long date format

 #   print("The year must be within 2013")
