#Define the main function that will call all other functions
def main():
    miles = float(input("Please tell me how many miles you want converted to kilometers?: ")) #ask the user how many miles to convert
    if (miles > 0):
        milesToKm(miles)            #call milesToKm function
        fahrenheit = float(input("Please tell me the temperature in fahrenheit: "))     #ask the user what temp in F to convert
        if (fahrenheit < 1000):
            fahToCel(fahrenheit)              #call fahToCel function
            gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #ask the user how many gallons to convert
            if (gallons > 0):
                galToLit(gallons)              #call galToLit function
                pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
                if (pounds > 0):
                    poundsToKg(pounds)             #call poundsToKg function
                    inches = float(input("Please tell me how many inches you want converted to centimeters: ")) #ask the user how many inches to convert
                    if (inches > 0):
                        inchesToCm(inches)             #call inchesToCm function
    else:
        print("That value is invalid. Please rerun the program.")
        endProgram()
        
        
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

#Define end program
def endProgram():
    print("This program has ended. Goodbye.")
#Call the main function
main()
