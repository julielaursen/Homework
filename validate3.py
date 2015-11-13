#dfine validation function		
def isValid():
    #validate the date
    monthValid = False
    dayValid = False
    sizeValid = False
    yearValid = False
   
    
    #set all validation to false to begin with and have user enter input
    while (monthValid == False) or (dayValid == False) or (sizeValid == False) or (yearValid == False):
        date = input("Please enter a date in the mm/dd/yy format: ")
        #if statement to convert - to /
        if date.find('-') != -1:
            a = date.split('-')
        elif date.find('/') != -1:
            a = date.split('/')
        #split month, day and year and set size of year to 2
        month = a[0]
        day = a[1]
        year = a[2]
        month = int(month)
        day = int(day)
        size = len(year)
        year = int(year)

        #create month list for validation statement
        monthList = ['None', 'Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        
        #set parameters outside range. if user enters anything false, will return specific statements and go back to while loop
        if (month > 12) or (month < 1):
            monthValid = False
            print("outside month range")
        else:
            monthValid = True
        if (day > 31) or (day < 1):
            dayValid = False
            print("outside day range")
        else:
            dayValid = True
        if (year != 13):
            yearValid = False
            print("outside year range")
        else:
            yearValid = True
        if (size != 2):
            sizeValid = False
            print("date must be in format yy:")
        else:
            sizeValid = True
    #if all validation statements are true, print longdate format
    else:
        year = "2013"
        print("Your date is: ",(monthList[month]), " ", day, ", " , year, sep="")

    
               
           
    
	
    
	
	
