import sys

#define quit choice and trys
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
    #run the for statement
    for choice in range(trys):
            #display the menu
            displayMenu()

    #Get user's choice
            choice = int(input('Enter your choice: '))
    #use if/elif to associate menu choice to function
            if choice == 1:
                miles(conversion_file)
                miles_list()
            elif choice == 2:
                fahrenheit(conversion_file)
                fahrenheit_list()
            elif choice == 3:
                gallons(conversion_file)
            elif choice == 4:
                pounds(conversion_file)
            elif choice == 5:
                inches(conversion_file)
            elif choice == QUIT_CHOICE:
                print('Exiting the program...')
                break
            else:
                print('Error: That is an invalid selection.')

def miles_list():
    print('Miles conversion chart:','\n')
    print('Miles\tKilometers')
    print('-----------------')
    miles_list = [['1, 1.6'],
                  ['10, 16'],
                  ['20, 32'],
                  ['30, 48'],
                  ['40, 64'],
                  ['50, 80'],
                  ['60, 96'],
                  ['70, 112'],
                  ['80, 238'],
                  ['90, 144'],
                  ['100, 160']]
    print(miles_list[0])
    print(miles_list[1])
    print(miles_list[2])
    print(miles_list[3])
    print(miles_list[4])
    print(miles_list[5])
    print(miles_list[6])
    print(miles_list[7])
    print(miles_list[8])
    print(miles_list[9])
    print(miles_list[10])

def fahrenheit_list():
    print('Fahrenheit conversion chart:','\n')
    print('F \tC')
    print('-------------------')
    fah_cel_list = [['-10, -23'],
                    ['0, -17'],
                    ['10, -12'],
                    ['20, -6'],
                    ['30, -1'],
                    ['40, 4'],
                    ['50, 10'],
                    ['60, 15'],
                    ['70, 21'],
                    ['80, 26'],
                    ['90, 32'],
                    ['100, 37']]
    print(fah_cel_list[0])
    print(fah_cel_list[1])
    print(fah_cel_list[2])
    print(fah_cel_list[3])
    print(fah_cel_list[4])
    print(fah_cel_list[5])
    print(fah_cel_list[6])
    print(fah_cel_list[7])
    print(fah_cel_list[8])
    print(fah_cel_list[9])
    print(fah_cel_list[10])
    print(fah_cel_list[11])
    
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
                   
        
#Define milesToKm function, write output of the function to a file called conversion_file                                         
def milesToKm(miles, conversion_file):
    miles_to_kilometers = float(miles * 1.6)                                                    #calculate miles to kilometers
    print (miles, "miles equals", miles_to_kilometers, "kilometers")
    conversion_file.write('Your input was:\n',)
    conversion_file.write(str(miles) + '')
    conversion_file.write(' miles\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(miles_to_kilometers))
    conversion_file.write(' kilometers\n\n')
 
#Define fahToCel function, write output of the function to a file called conversion_file
def fahToCel(fahrenheit, conversion_file):
    fahrenheit_to_celsius = float((fahrenheit - 32) * 5/9)                          #convert fahrenheit to celsius
    print (fahrenheit, "Fahrenheit is", fahrenheit_to_celsius, "Celsius")            #print the result of the calculation
    conversion_file.write('Your input was:\n',)
    conversion_file.write(str(fahrenheit) + '')
    conversion_file.write(' degrees fahrenheit\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(fahrenheit_to_celsius))
    conversion_file.write(' degrees celsius\n\n')
         
#Define galToLit function, write output of the function to a file called conversion_file
def galToLit(gallons, conversion_file):
    gallons_to_liters = float(gallons * 3.9)                                                    #convert gallons to liters
    print (gallons, "gallons equals", gallons_to_liters, "liters")
    conversion_file.write('Your input was:\n')
    conversion_file.write(str(gallons) + '')
    conversion_file.write(' gallons\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(gallons_to_liters))
    conversion_file.write(' liters\n\n')

#Define poundsToKg function, write output of the function to a file called conversion_file
def poundsToKg(pounds, conversion_file):   
    pounds_to_kilograms = float(pounds * .45)                                                   #convert pounds to kilograms
    print (pounds, "pounds equals", pounds_to_kilograms, "kilograms")    #print the result of the calculation
    conversion_file.write('Your input was:\n')
    conversion_file.write(str(pounds) + '')
    conversion_file.write(' pounds\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(pounds_to_kilograms))
    conversion_file.write(' kilograms\n\n')
                       
#Define inchesToCm function, write output of the function to a file called conversion_file
def inchesToCm(inches, conversion_file):
    inches_to_centimeters = float(inches * 2.54)                                                #convert inches to centimeters
    print (inches, "inches equals", inches_to_centimeters, "centimeters") #print the result of the calculation
    conversion_file.write('Your input was:\n')
    conversion_file.write(str(inches) + '')
    conversion_file.write(' inches\n')
    conversion_file.write('Your output was:\n')
    conversion_file.write(str(inches_to_centimeters))
    conversion_file.write(' centimeters\n\n')

#display menu choices  
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
