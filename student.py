class Student:

    def __init__(self, gpa, name, ID, expectedGrade, ftOrPt):
        self.__gpa = gpa
        self.__name = name
        self.__ID = ID
        self.__expectedGrade = expectedGrade
        self.__ftOrPt = ftOrPt

    def get_name(self):
        return self.__name

    def get_gpa(self):
        return self.__gpa

    def printGPA(self):
        print(self.__gpa)

    def changeGPA(self):
        print(self.__gpa)

'''
    def __str__(self):
        return "Name: " + self.__name + \
               "\nGpa: " + self.__gpa + \
               "\nID: " + self.__id + \
               "\nExpected Grade: " + self__expectedGrade + \
               "\nFull Time or Part Time: " + self.__ftOrPt
'''    
all_the_students = []
  

def LookupPrintGPA():
    Name = input("Name of the student: ")
    for x in Students:
        if x.get_name() == Name:
            x.printGPA()

def AddNewStudent():
    for choice in range(5):
        name = input("name: ")
        print(name)
        gpa = input("GPA: ")
        ID = input("ID")
        expectedGrade = input("Expected Grade: ")
        ftOrPt = input("Enter (FT) for full time or (PT) for part time")
        OneStudent = Student(gpa, name, ID, expectedGrade, ftOrPt)
        print(OneStudent)
        #return OneStudent
        #all_the_students.append(OneStudent)

AddNewStudent()



#mynewstudent = AddNewStudent()
#all_the_students.append(mynewstudent)



    

