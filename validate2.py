		

    
def isValid(date):
    #validate the date
    for x in date:
        month = date[:2]
        day = date[3:5]
        year = date[6:]

    month = int(month)
    day = int(day)
    size = len(year)
    year = int(year)

    correct_day = False
    correct_month = False
    correct_year = False
    correct_size =False

    #book says for x in date, but its using .isupper et
    if correct_size and correct_day and correct_month and correct_year:
        print("Call isvalid")
        isValid = True
        print("That date is valid")
    else:
        isValid = False
        print("If else invalid")
        
    while isValid == False:
        print("size")
        if (month > 12) or (month < 1):
            correct_month = False
            print("The correct month is", correct_month)
            break
        if (day > 32) or (day < 1):
            correct_day = False
            print("The correct day is", correct_day)
            break
        if (year != 13):
            correct_year = False
            print("The correct year is", correct_year)
            break
        if (size != 2):
            correct_size = False
            print(correct_size)
            break
    else:
        correct_date = True
        correct_month = True
        correct_year = True
        correct_day = 
        isValid = True
        return isValid
        
    
    print("Validation statement")        
    
	
    
	
	
