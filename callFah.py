

def endProgram():
    print("This program has ended. Goodbye.")

#Repeat the function statements but using fahrenheit instead of miles and set invalid value to over 1000            
def inputFahrenheit():
    count = 0
    fahrenheit = float(input("Please tell me the temperature in fahrenheit: "))
    invalid = True
    if (fahrenheit < 1000):
        fahToCel(fahrenheit)
        invalid = False
        count = count + 1
    else:
        print("That value is invalid. Please re-enter the value")
        for num in range(2):
            count = count + 1
            fahrenheit = float(input("Please tell me the temperature in fahrenheit: ")) 
            if (fahrenheit < 1000):
                fahToCel(fahrenheit)
                invalid = False
                break
            else:
                count = count + 1
                while (count < 3):
                    print("That value is invalid. Please re-enter the value")
                    break
                else:
                    print("That value is invalid")
    if(invalid):
        endProgram()
        return False
    else:
        return True

    #Define fahToCel function
def fahToCel(fahrenheit):
    fahrenheit_to_celsius = float((fahrenheit - 32) * 5/9)                          #convert fahrenheit to celsius
    print (fahrenheit, "Fahrenheit is", fahrenheit_to_celsius, "Celsius") 
