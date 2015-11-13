import sys

QUIT_CHOICE = 6

#Define end program
def endProgram():
    print("This program has ended. Goodbye.")

    
#Define the main function that will call all other functions
def main():
    #the choice variable controls the loop and holds the menu choice
    choice = 0

    while choice != QUIT_CHOICE:
        #display the menu
        displayMenu()

    #Get user's choice
        choice = int(input('Enter your choice: '))
    #use nested ifs to call the next function if the function being called is used and not set to invalid
        if choice == 1:
            miles()
        elif choice == 2:
            fahrenheit()
        elif choice == 3:
            gallons()
        elif choice == 4:
            pounds()
        elif choice == 5:
            inches()
        elif choice == QUIT_CHOICE:
            print('Exiting the program...')
        else:
            print('Error: invalid selection.')
    
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

#Repeat the function statements but using fahrenheit instead of miles and set invalid value to over 1000            
def fahrenheit():
    fahrenheit = float(input("Please tell me the temperature in fahrenheit: "))
    invalid = True
    if (fahrenheit < 1000):
        fahToCel(fahrenheit)
        invalid = False
    else:
        print("That value is invalid. Please re-enter the value")
        for num in range(2):
            fahrenheit = float(input("Please tell me the temperature in fahrenheit: ")) 
            if (fahrenheit < 1000):
                fahToCel(fahrenheit)
                invalid = False
                break
        else:
            print("That value is invalid. Please re-enter the value")
    if(invalid):
        endProgram()
        return False
    else:
        return True

#Repeat the function statements with gallons
def gallons():
    gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #ask the user how many gallons to convert
    invalid = True
    #if gallons is greater than 0 do the following:
    if (gallons > 0):
        galToLit(gallons) #call galToLit function
        invalid = False
    else:
        print("That value is invalid. Please re-enter the value")
        for num in range(2):
            gallons = float(input("Please tell me how many gallons you want converted to liters: "))
            if (gallons > 0):
                galToLit(gallons)
                invalid = False
                break
        else:
            print("That value is invalid. Please re-enter the value")
    if(invalid):
        endProgram()
        return False
    else:
        return True

#Repeat the function statements with pounds    
def pounds():
    pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
    invalid = True
        #if pounds is greater than 0 do the following:
    if (pounds > 0):
        poundsToKg(pounds)             #call poundsToKg function
        invalid = False
    else:
        for num in range(2):
            pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
            if (pounds > 0):
                poundsToKg(pounds)
                invalid = False
                break
        else:
            print("That value is invalid. Please re-enter the value")
    if(invalid):
        endProgram()
        return False
    else:
        return True

#Repeat the function statements with inches
def inches():
    inches = float(input("Please tell me how many inches you want converted to centimeters: "))
    if (inches > 0):
        inchesToCm(inches)
    else:
        for num in range(2):
            inches = float(input("Please tell me how many inches you want converted to centimeters: ")) #ask the user how many inches to convert
            if (inches > 0):
                inchesToCm(inches)
                break
        else:
            print("That value is invalid. Please rerun the program.")
                   
        
#Define milesToKm function                                         
def milesToKm(miles):
    miles_to_kilometers = float(miles * 1.6)                                                    #calculate miles to kilometers
    print (miles, "miles equals", miles_to_kilometers, "kilometers")                            #print the result of the calculation

#Define fahToCel function
def fahToCel(fahrenheit):
    fahrenheit_to_celsius = float((fahrenheit - 32) * 5/9)                          #convert fahrenheit to celsius
    print (fahrenheit, "Fahrenheit is", fahrenheit_to_celsius, "Celsius")            #print the result of the calculation

#Define galToLit function
def galToLit(gallons):
    gallons_to_liters = float(gallons * 3.9)                                                    #convert gallons to liters
    print (gallons, "gallons equals", gallons_to_liters, "liters")                              #print the result of the calculation

#Define poundsToKg function
def poundsToKg(pounds):   
    pounds_to_kilograms = float(pounds * .45)                                                   #convert pounds to kilograms
    print (pounds, "pounds equals", pounds_to_kilograms, "kilograms")                           #print the result of the calculation

#Define inchesToCm function
def inchesToCm(inches):
    inches_to_centimeters = float(inches * 2.54)                                                #convert inches to centimeters
    print (inches, "inches equals", inches_to_centimeters, "centimeters") #print the result of the calculation

def displayMenu():
    print('      MENU')
    print('1) Miles to Kilometers')
    print('2) Fahrenheit to Celsius')
    print('3) Gallons to Liters')
    print('4) Pounds to Kilograms')
    print('5) Inches to Centimeters')
    print('6) QUIT_CHOICE')


#Call the main function
main()
