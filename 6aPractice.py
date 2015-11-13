import sys
import callmiles

#Define the main function that will call all other functions
def main():
    miles = 0
    #use nested ifs to call the next function if the function being called is used and not set to invalid
    if callmiles.inputMiles():
        print('Miles is', callmiles.milesToKm(miles))

main()
