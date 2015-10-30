import sys

QUIT_CHOICE = 6
trys = 10

#Define end program
def endProgram():
    print("This program has ended. Goodbye.")

    
#Define the main function that will call all other functions
def main():
    #the choice variable controls the loop and holds the menu choice
    choice = 0
    conversion_file = open('conversions.txt', 'w')

    for choice in range(trys):
            #display the menu
            displayMenu()

    #Get user's choice
            choice = int(input('Enter your choice: '))
    #use nested ifs to call the next function if the function being called is used and not set to invalid
            if choice == 1:
                miles(conversion_file)
            elif choice == 2:
                fahrenheit(conversion_file)
            elif choice == 3:
                gallons(conversion_file)
            elif choice == 4:
                pounds(conversion_file)
            elif choice == 5:
                inches(conversion_file)
            elif choice == QUIT_CHOICE:
                print('Exiting the program...')
            else:
                print('Error: invalid selection.')
    
def miles(conversion_file):
    #ask user for number to convert
    miles = float(input("Please tell me how many miles you want converted to kilometers?: "))
    #if miles is a valid value run milesToKm function
    if (miles > 0):
        milesToKm(miles, conversion_file)
    else:
        print("You cannot use 0 or a negative number as input")
        

#Repeat the function statements but using fahrenheit instead of miles and set invalid value to over 1000            
def fahrenheit(conversion_file):
    fahrenheit = float(input("Please tell me the temperature in fahrenheit: "))
    if (fahrenheit < 1000):
        fahToCel(fahrenheit, conversion_file)
    else:
        print("The value must be under 1000")

#Repeat the function statements with gallons
def gallons(conversion_file):
    gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #ask the user how many gallons to convert
    #if gallons is greater than 0 do the following:
    if (gallons > 0):
        galToLit(gallons, conversion_file) #call galToLit function
    else:
        print("You cannot use 0 or a negative number as input")

#Repeat the function statements with pounds    
def pounds(conversion_file):
    pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
        #if pounds is greater than 0 do the following:
    if (pounds > 0):
        poundsToKg(pounds, conversion_file)             #call poundsToKg function
    else:
        print("You cannot use 0 or a negative number as input")
    

#Repeat the function statements with inches
def inches(conversion_file):
    inches = float(input("Please tell me how many inches you want converted to centimeters: "))
    if (inches > 0):
        inchesToCm(inches, conversion_file)
    else:
        print("You cannot use 0 or a negative number as input")
                   
        
#Define milesToKm function                                         
def milesToKm(miles, conversion_file):
    miles_to_kilometers = float(miles * 1.6)                                                    #calculate miles to kilometers
    print (miles, "miles equals", miles_to_kilometers, "kilometers")
    conversion_file.write('Your input was:\n',)
    conversion_file.write(str(miles) + '')
    conversion_file.write(' miles\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(miles_to_kilometers))
    conversion_file.write(' kilometers\n\n')
 
#Define fahToCel function
def fahToCel(fahrenheit, conversion_file):
    fahrenheit_to_celsius = float((fahrenheit - 32) * 5/9)                          #convert fahrenheit to celsius
    print (fahrenheit, "Fahrenheit is", fahrenheit_to_celsius, "Celsius")            #print the result of the calculation
    conversion_file.write('Your input was:\n',)
    conversion_file.write(str(fahrenheit) + '')
    conversion_file.write(' degrees fahrenheit\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(fahrenheit_to_celsius))
    conversion_file.write(' degrees celsius\n\n')
         
#Define galToLit function
def galToLit(gallons, conversion_file):
    gallons_to_liters = float(gallons * 3.9)                                                    #convert gallons to liters
    print (gallons, "gallons equals", gallons_to_liters, "liters")
    conversion_file.write('Your input was:\n')
    conversion_file.write(str(gallons) + '')
    conversion_file.write(' gallons\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(gallons_to_liters))
    conversion_file.write(' liters\n\n')

#Define poundsToKg function
def poundsToKg(pounds, conversion_file):   
    pounds_to_kilograms = float(pounds * .45)                                                   #convert pounds to kilograms
    print (pounds, "pounds equals", pounds_to_kilograms, "kilograms")    #print the result of the calculation
    conversion_file.write('Your input was:\n')
    conversion_file.write(str(pounds) + '')
    conversion_file.write(' pounds\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(pounds_to_kilograms))
    conversion_file.write(' kilograms\n\n')
                       
#Define inchesToCm function
def inchesToCm(inches, conversion_file):
    inches_to_centimeters = float(inches * 2.54)                                                #convert inches to centimeters
    print (inches, "inches equals", inches_to_centimeters, "centimeters") #print the result of the calculation
    conversion_file.write('Your input was:\n')
    conversion_file.write(str(inches) + '')
    conversion_file.write(' inches\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(inches_to_centimeters))
    conversion_file.write(' centimeters\n\n')
    
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
