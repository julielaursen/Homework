
#Define end program
def endProgram():
    print("This program has ended. Goodbye.")
    
#Repeat the function statements with pounds    
def inputPounds():
    count = 0
    pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
    invalid = True
        #if pounds is greater than 0 do the following:
    if (pounds > 0):
        poundsToKg(pounds)             #call poundsToKg function
        invalid = False
        count = count + 1
    else:
        print("That value is invalid. Please re-enter the value")
        for num in range(2):
            count = count + 1
            pounds = float(input("Please tell me how many pounds you want converted to kilograms: "))   #ask the user how many pounds to convert
            if (pounds > 0):
                poundsToKg(pounds)
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

    #Define poundsToKg function
def poundsToKg(pounds):   
    pounds_to_kilograms = float(pounds * .45)                                                   #convert pounds to kilograms
    print (pounds, "pounds equals", pounds_to_kilograms, "kilograms")  
