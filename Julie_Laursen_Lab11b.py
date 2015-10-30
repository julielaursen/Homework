
QUIT_CHOICE = 6


#class Student holds the following data about a student: name, id, gpa, expected grade, FT or PT
class Student:

    def __init__(self, name, gpa, ID, expectedGrade, ftOrPt):
        self.name = name
        self.gpa = gpa
        self.ID = ID
        self.expectedGrade = expectedGrade
        self.ftOrPt = ftOrPt

    def printGPA(self, gpa):
        print(self.gpa)

    def changeGPA(self, gpa):
        print(self.gpa)
    
#create five student objects from this class
def main():
    students = []
    
    name = ["Joe", "Julie", "Pam", "Jane", "John"]
    gpa = [4.0, 4.0, 3.0, 2.0, 1.0]
    ID = [12345, 54321, 23456, 65432, 34567]
    ftOrPt = ["Pt", "Pt", "Ft", "Pt", "Ft"]
    expectedGrade = ["A", "B", "C", "D", "F"]

    student1 = Student(name, gpa, ID, expectedGrade, ftOrPt)
    students.append(gpa])
    student1.printGPA(gpa)
    



        #students.append(student1)
        #student1.printGPA()


   # student2 = Student(name, gpa, ID, ftOrPt, expectedGrade)
    #Student3 = Student(name, gpa, ID, ftOrPt, expectedGrade)
    #Student4 = Student(name, gpa, ID, ftOrPt, expectedGrade)
    #Student5 = Student(name, gpa, ID, ftOrPt, expectedGrade)


#create menu
    choice = 0

    while choice != QUIT_CHOICE:
        displayMenu()

        choice = input('Please enter your choice: ')
        if choice == 1:
            inputGPA = input("Please enter the GPA:" )
        elif choice == 2:
            inputStudentID = input("Please enter the student ID number")
        elif choice == 3:
            changeGPA = input("Input the GPA to change to: ")
        elif choice == 4:
            inputExpectedGrade = input("Please enter the expected grade: ")
        elif choice == 5:
            print("data")
        elif choice == 6:
            print("Exiting the program")
        else:
            print("Error, invalid selection")


def displayMenu():
    print('      MENU')
    print('1) Look up and print the student GPA')
    print('2) Add a new student to the class')
    print('3) Change the GPA of a student')
    print('4) Change the expected grade of a student')
    print('5) Print the data of all the students in a tabular format')
    print('6) Quit the Program')

   

main()
