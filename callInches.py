

#Define end program
def endProgram():
    print("This program has ended. Goodbye.")
    

#Repeat the function statements with inches
def inputInches():
    count = 0
    inches = float(input("Please tell me how many inches you want converted to centimeters"))
    invalid = True
    if (inches > 0):
        inchesToCm(inches)
        invalid = False
        count = count + 1
    else:
        print("That value is invalid. Please re-enter the value.")
        for num in range(2):
            count = count + 1
            inches = float(input("Please tell me how many inches you want converted to centimeters: ")) #ask the user how many inches to convert
            if (inches > 0):
                inchesToCm(inches)
                invalid = False
                break
            else:
                count = count + 1
                while (count < 3):
                    print("That value is invalid. Please re-enter the value.")
                    break
                else:
                    print("That value is invalid")
            
    if(invalid):
        endProgram()
        return False
    else:
        return True
 




#Define inchesToCm function
def inchesToCm(inches):
    inches_to_centimeters = float(inches * 2.54)                                                #convert inches to centimeters
    print (inches, "inches equals", inches_to_centimeters, "centimeters") #print the result of the calculation
