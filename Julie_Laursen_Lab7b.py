#define total Grades for the for statement
totalGrades = 12 

#define main function
def main():
    #open a file called grades.txt for writing to
    grade_file = open('grades.txt', 'w')

    #for statement to get name and average. 
    for choice in range(totalGrades):
        name = input("Please enter the student's name: ")
        average = int(input("Please enter the student's average grade: "))
        #if average is valid, write name and average to grade file and close it
        if (average > 0 and average < 101): 
            grade_file.write("\n The student's name is: ")
            grade_file.write(name)
            grade_file.write("\n The student's average is: ")
            grade_file.write(str(average) + "")
        else:
            print("That is an invalid grade. Try again")
    grade_file.close()

    #try/except clause to open grades.txt and read it to the screen.
    #if FileNotFoundError, print except statement
    try:
        read_file = open('grades.txt', 'r')
        file_contents = read_file.read()
        read_file.close()
        print(file_contents)
    except FileNotFoundError:
        print("The grades file does not exist")

#call main    
main()


