import sys
import callmiles
import callFah
import callGallons
import callPounds
import callInches


#Define the main function that will call all other functions
def main():
    miles = 0
    #use nested ifs to call the next function if the function being called is used and not set to invalid
    if(callmiles.inputMiles()):
        if(callFah.inputFahrenheit()):
            if(callGallons.inputGallons()):
                if(callPounds.inputPounds()):
                    callInches.inputInches()
    
#Call the main function
main()
