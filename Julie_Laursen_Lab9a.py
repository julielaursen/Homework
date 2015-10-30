import sys

#Define end program
def endProgram():
    print("This program has ended. Goodbye.")
    
#Define the main function that will call all other functions
def main():
    name =  input("Please enter your name: ")
    email = input("Please enter your email address: ")

    if(miles(name)):
        if fahrenheit(name):
            if gallons(name):
                if pounds(name):
                    inches(name)

    position = email.find('@')

    while position != -1:
        return position 
    else:
        print("That email address is invalid. Please include the '@' sign")
        email = input("Please enter your email address: ")    
    

    
def miles(name):
    miles = int(input("Please tell me how many miles you want converted to kilometers?: "))
    invalid = True
    if (miles > 0):
        milesToKm(miles, name)
        invalid = False
    else:
        print("That value is invalid.")
        
    if(invalid):
        endProgram()
        return False
    else:
        return True
                
def fahrenheit(name):
    fahrenheit = int(input("Please tell me the temperature in fahrenheit: "))
    invalid = True
    if (fahrenheit < 1000):
        fahToCel(fahrenheit, name)
        invalid = False
    else:
        print("That value is invalid.")
        
    if(invalid):
        endProgram()
        return False
    else:
        return True

def gallons(name):
    gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #ask the user how many gallons to convert
    invalid = True
    #if gallons is greater than 0 do the following:
    if (gallons > 0):
        galToLit(gallons, name)              #call galToLit function
        invalid = False
    else:
        print("That value is invalid.")
    if(invalid):
        endProgram()
        return False
    else:
        return True
    
    
def pounds(name):
    pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
    invalid = True
        #if pounds is greater than 0 do the following:
    if (pounds > 0):
        poundsToKg(pounds, name)             #call poundsToKg function
        invalid = False
    else:
        print("That value is invalid.")
    if(invalid):
        endProgram()
        return False
    else:
        return True

def inches(name):
    inches = float(input("Please tell me how many inches you want converted to centimeters"))
    invalid = True
    if (inches > 0):
        inchesToCm(inches, name)
        invalid = False
    else:
        print("That value is invalid.")
    if(invalid):
        endProgram()
        return False
    else:
        return True
                   
        
#Define milesToKm function                                         
def milesToKm(miles, name):
    miles_to_kilometers = float(miles * 1.6)                                                    #calculate miles to kilometers
    print (name + ",", miles, "miles equals", miles_to_kilometers, "kilometers")                            #print the result of the calculation

#Define fahToCel function
def fahToCel(fahrenheit, name):
    fahrenheit_to_celsius = float((fahrenheit - 32) * 5/9)                          #convert fahrenheit to celsius
    print (name + ",", fahrenheit, "Fahrenheit is", fahrenheit_to_celsius, "Celsius")            #print the result of the calculation

#Define galToLit function
def galToLit(gallons, name):
    gallons_to_liters = float(gallons * 3.9)                                                    #convert gallons to liters
    print (name + ",", gallons, "gallons equals", gallons_to_liters, "liters")                              #print the result of the calculation

#Define poundsToKg function
def poundsToKg(pounds, name):   
    pounds_to_kilograms = float(pounds * .45)                                                   #convert pounds to kilograms
    print (name + ",", pounds, "pounds equals", pounds_to_kilograms, "kilograms")                           #print the result of the calculation

#Define inchesToCm function
def inchesToCm(inches, name):
    inches_to_centimeters = float(inches * 2.54)                                                #convert inches to centimeters
    print (name + ",", inches, "inches equals", inches_to_centimeters, "centimeters") #print the result of the calculation

#Call the main function
main()
