#define main function
def main():
    #set assignment statement to start the program
    keep_going = 'y'
    #set count and total to 0
    count = 0
    total = 0
    #ask user for input that will kick off the while loop
    start = input("This program will return a grade point average for each entry and average the entry \n Would you like to start? Enter y for yes: " )
    if (start == 'y'):
        while keep_going == 'y':
            #ask for input from user for grade in integer format
            grade = int(input("Please enter a grade:  "))
            if (grade > 100 or grade < 0):
                print("That is an invalid number. Please retry.")
            else:
                #keep a count of grades entered
                count += 1
                #call convert_grade function
                convert_grade(grade)
                #add numbered grade to total
                total = total + grade
                #divide sum of grades by number of grades for average
                average = total / count
                #see if the user wants to enter another one
            keep_going = input('Do you want to calculate another grade? (Enter y for yes or n for no): ')
    else:
        #if assignment statement was not met, end program
        print("You did not enter 'y'. Please re-run this program or exit.")
    print("The number of grades entered:", count)

    #as long as user has entered one grade, print the average
    if(count > 0):
            print("The class average is", average)
   
        
def convert_grade(grade):
#convert numeric grade to letter grade        
    if (grade >= 90 and grade <= 100):
        #assign formerly int value of grade to a number
        grade = 'A'
        print("This grade is: ", grade)
        #issue a comment on the letter grade earned
        print("Great job!")
    elif (grade >= 80):
        #assign formerly int value of grade to a number
        grade = 'B'
        print("This grade is: ", grade)
        #issue a comment on the letter grade earned
        print("Good job!")
    elif (grade >= 70):
        #assign formerly int value of grade to a number
        grade = 'C'
        print("This grade is: ", grade)
        #issue a comment on the letter grade earned
        print("You are passing")
    elif (grade >= 60):
        #assign formerly int value of grade to a number
        grade = 'D'
        print("This grade is: ", grade)
        #issue a comment on the letter grade earned
        print("You are close to failing")
    else:
        #assign formerly int value of grade to a number
        grade = 'F'
        print("This grade is: ", grade)
        #issue a comment on the letter grade earned
        print("You are currently failing")

    

#define endProgram function
def endProgram():
    print("Goodbye!")

#call main function
main()
