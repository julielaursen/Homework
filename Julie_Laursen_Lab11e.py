import student2

student_list = [
    student2.Student('Julie', 4.0, 23409, 'A', 'Ft'),
    student2.Student('Joe', 4.0, 45678, 'A', 'Ft'),
    student2.Student('Susie', 3.0, 52980, 'B', 'Pt'),
    student2.Student('Sarah', 2.0, 45893, 'C', 'Ft'),
    student2.Student('Sam', 1.0, 32409, 'F', 'Pt')
]


def displayMenu():
    print('      MENU')
    print('1) Look up and print the student GPA')
    print('2) Add a new student to the class')
    print('3) Change the GPA of a student')
    print('4) Change the expected grade of a student')
    print('5) Print the data of all the students in a tabular format')
    print('6) Quit the Program')

def lookupPrintGPA():
    Name = input("Name of the student: ")
    for x in student_list:
        if x.get_name() == Name:
            x.printGPA()

def addNewStudent():
        name = input("name: ")
        gpa = input("GPA: ")
        ID = input("ID: ")
        expectedGrade = input("Expected Grade: ")
        ftOrPt = input("Enter (FT) for full time or (PT) for part time: ")
        OneStudent = student2.Student(name, gpa, ID, expectedGrade, ftOrPt)
        student_list.append(OneStudent)

def changeGPA():
    Name = input("Name of the student: ")
    for x in student_list:
        if x.get_name() == Name:
            x.change_gpa()
            print("The grade has been changed to: ")
            x.printGPA()

def changeExpectedGrade():
    Name = input("Name of the student: ")
    for x in student_list:
        if x.get_name() == Name:
            x.change_expected_grade()
            print("The grade has been changed to: ")
            x.printExpectedGrade()

def printAllData():
    for x in student_list:
        print(x.get_name(), "\t", x.get_gpa(), "\t", x.get_ID(), "\t", x.get_expected_grade(), "\t", x.get_ftOrPt())
        
        
def main():
    

    end_of_file = False
    choice = 0
    while choice != 6:
        displayMenu()
        choice = int(input('Please enter your choice: '))
        if choice == 1:
            lookupPrintGPA()
        elif choice == 2:
            addNewStudent()
        elif choice == 3:
            changeGPA()
        elif choice == 4:
            changeExpectedGrade()
        elif choice == 5:
            printAllData()
        elif choice == 6:
            print("Exiting the program")
        else:
            print("Error, invalid selection")


main()



