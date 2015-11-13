import sys

#Define end program
def endProgram():
    print("This program has ended. Goodbye.")
    
#Define the main function that will call all other functions
def main():
    if(miles()):
        if fahrenheit():
            if gallons():
                if pounds():
                    inches()
    
def miles():
    miles = int(input("Please tell me how many miles you want converted to kilometers?: "))
    invalid = True
    if (miles > 0):
        milesToKm(miles)
        invalid = False
    else:
        print("That value is invalid.")
        
    if(invalid):
        endProgram()
        return False
    else:
        return True
                
def fahrenheit():
    fahrenheit = int(input("Please tell me the temperature in fahrenheit: "))
    invalid = True
    if (fahrenheit < 1000):
        fahToCel(fahrenheit)
        invalid = False
    else:
        print("That value is invalid.")
        
    if(invalid):
        endProgram()
        return False
    else:
        return True

def gallons():
    gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #ask the user how many gallons to convert
    invalid = True
    #if gallons is greater than 0 do the following:
    if (gallons > 0):
        galToLit(gallons)              #call galToLit function
        invalid = False
    else:
        print("That value is invalid.")
    if(invalid):
        endProgram()
        return False
    else:
        return True
    
    
def pounds():
    pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
    invalid = True
        #if pounds is greater than 0 do the following:
    if (pounds > 0):
        poundsToKg(pounds)             #call poundsToKg function
        invalid = False
    else:
        print("That value is invalid.")
    if(invalid):
        endProgram()
        return False
    else:
        return True

def inches():
    inches = float(input("Please tell me how many inches you want converted to centimeters"))
    invalid = True
    if (inches > 0):
        inchesToCm(inches)
        invalid = False
    else:
        print("That value is invalid.")
    if(invalid):
        endProgram()
        return False
    else:
        return True
                   
        
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

#Call the main function
main()
