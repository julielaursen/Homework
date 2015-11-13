#The miles module has functions that perform the input and validation of the miles to be converted
#then milestoKM function calculates the miles to kilometers and returns the result

#define miles function
def miles():
    #ask user for number to convert
    miles = float(input("Please tell me how many miles you want converted to kilometers?: "))
    #set flag so if invalid is false then continue, else end program
    invalid = True
    #if miles is a valid value run milesToKm function
    if (miles > 0):
        milesToKm(miles)
        #set flag to false so invalid if block will not be called to end program
        invalid = False
    else:
        #ask user to re-enter 
        print("That value is invalid. Please re-enter the value")
        #set range of miles to two more entries
        for miles in range(2):
            #get input from user again
            miles = float(input("Please tell me how many miles you want converted to kilometers?: ")) #ask the user how many miles to convert
            #if miles is a valid number, rerun milesToKm program and set invalid to false so program doesn't exit and break
            #this way it will not repeat the for loop and ask again
            if (miles > 0):
                milesToKm(miles)
                invalid = False
                break
            #if miles is invalid, it will go through the range again and ask for input from the user
            else:
                print("That value is invalid. Please re-enter the value")
    #if statement calling invalid value. Invalid is set to true initially
    #If invalid isn't set to false by the correct number of entries, this will call the endProgram function
    if(invalid):
        endProgram()
        return False
    else:
        return True

#Define milesToKm function                                         
def milesToKm(miles):
    miles = float(miles * 1.6)
    return miles
    #supposed to be miles * km where km is 1.6
