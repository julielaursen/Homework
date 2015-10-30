
def endProgram():
    print("This program has ended. Goodbye.")

def inputGallons():
    count = 0
    gallons = float(input("Please tell me how many gallons you want converted to liters: "))    #ask the user how many gallons to convert
    invalid = True
    #if gallons is greater than 0 do the following:
    if (gallons > 0):
        galToLit(gallons) #call galToLit function
        invalid = False
        count = count + 1
    else:
        print("That value is invalid. Please re-enter the value")
        for num in range(2):
            count = count + 1
            gallons = float(input("Please tell me how many gallons you want converted to liters: "))
            if (gallons > 0):
                galToLit(gallons)
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

#Define galToLit function
def galToLit(gallons):
    gallons_to_liters = float(gallons * 3.9)                                                    #convert gallons to liters
    print (gallons, "gallons equals", gallons_to_liters, "liters")                              #print the result of the calculation
