
import student
import pickle

#class Student holds the following data about a student: name, id, gpa, expected grade, FT or PT

    
#create five student objects from this class
def main():

    FILENAME = 'students.dat'
    
    students_dict = {'Joe' : [4.0, 12345, 'Pt', 'A'],
                     'Julie' : [3.5, 23456, 'Pt', 'B'],
                     'Pam' : [3.0, 34567, 'Ft', 'C'],
                     'Jane' : [2.0, 54321, 'Ft', 'D'],
                     'John' : [1.9, 65432, 'Ft', 'F']}
    output_file = open('students.dat', 'wb')
    pickle.dump(students_dict, output_file)
    output_file.close()

    myStudents = loadStudents(students_dict)
    
    
    
    end_of_file = False
    choice = 0
    while choice != 6:
        displayMenu()
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            look_up(myStudents)
        elif choice == 2:
            print("This will add a new student to the class.")
            addStudent(myStudents)
        #This passes validation but doesn't put the new user in the table
        elif choice == 3:
            changeGPA(myStudents)
        elif choice == 4:
            changeExpectedGrade = input("Please enter the expected grade: ")
        elif choice == 5:
            print("Displaying data for all students")
            inputfile = open('students.dat', 'rb')
            while not end_of_file:
                try:
                    students_dict = pickle.load(inputfile)
                    display_data(students_dict)
                except EOFError:
                    end_of_file = True
                    inputfile.close()
                return students_dict
        elif choice == 6:
            print("Exiting the program")
        else:
            print("Error, invalid selection")

    saveStudents(myStudents)

        

def loadStudents(students_dict):
    try:
        inputfile = open('students.dat', 'rb')
        students_dict = pickle.load(inputfile)
        inputfile.close()
    except EOFError:
        end_of_file = True
        inputfile.close()
    except IOError:
        students_dict = {} 
    return students_dict

def displayMenu():
    print('      MENU')
    print('1) Look up and print the student GPA')
    print('2) Add a new student to the class')
    print('3) Change the GPA of a student')
    print('4) Change the expected grade of a student')
    print('5) Print the data of all the students in a tabular format')
    print('6) Quit the Program')

def display_data(students_dict):
    print("Name | GPA | ID | FT/PT | Grade")
    print("-----------------------------------")
    print("Joe:  ", students_dict['Joe'])
    print("Julie:", students_dict['Julie'])
    print("Pam:  ", students_dict['Pam'])
    print("Jane: ", students_dict['Jane'])
    print("John: ", students_dict['John'])

def addStudent(myStudents):
    name = input("Name: ")
    ID = input("ID: ")
    gpa = input("GPA: ")
    ftOrPt = input("Full time or Part time? Enter ft for Full time. Enter pt for part time: ")
    expectedGrade = input("Expected Grade")
    entry = student.Student(gpa, name, ID, expectedGrade, ftOrPt)
    if name not in myStudents:
        myStudents[name] = entry
        print("The entry has been added")
    else:
        print("Student already exists")

def look_up(myStudents):
    studentName = input("What is the name of the student?: ")
    printStudentGpa = student.Student(gpa)
    printStudentGpa.printGPA(studentName)
    #print(myStudents.get(name, 'That name is not found.'))
    #returns full line, get it to just return field
    
def changeGPA(myStudents):
    name = input("Enter a name: ")
    if name in myStudents:
        gpa = input("Enter the new GPA: ")
        entry = student.Student(gpa, name, ID, expectedGrade, ftOrPt)
        myStudents[gpa] = entry
        print("The student's GPA has been updated")
    else:
        print("That name is not found")

def changeExpectedGrade(myStudents):
    name = input("Enter a name: ")
    if name in MyStudents:
        expectedGrade = input("Enter the new expected grade: ")
        entry = student.Student(gpa, name, ID, expectedGrade, ftOrPt)
        myStudents[expectedGrade] = entry
        print("The student's expected grade has been updated")
    else:
        print("That name is not found")

def saveStudents(myStudents):
    output_file = open(FILENAME, 'wb')
    pickle.dump(myStudents, output_file)
    output_file.close()
    


main()
