class Student:

    def __init__(self, name, gpa, ID, expectedGrade, ftOrPt):
        self.name = name
        self.gpa = gpa
        self.ID = ID
        self.expectedGrade = expectedGrade
        self.ftOrPt = ftOrPt

    def get_name(self):
        return self.name

    def print_name(self):
        print(self.name)

    def get_gpa(self):
        return self.gpa

    def printGPA(self):
        print(self.gpa)

    def change_gpa(self):
        self.gpa = input("Please enter the new GPA: ")

    def get_ID(self):
        return self.ID

    def print_ID(self):
        print(self.ID)

    def get_expected_grade(self):
        return self.expectedGrade

    def printExpectedGrade(self):
        print(self.expectedGrade)

    def change_expected_grade(self):
        self.expectedGrade = str(input("Please enter the new expected grade: "))

    def get_ftOrPt(self):
        return self.ftOrPt

    def print_ftOrPt(self):
        print(self.ftOrPt)
    '''
    def __str__(self):
        return ("Name: " + self.name +
            "Student ID: " + self.ID +
            "\GPA: " + self.gpa +
            "\nStudent Expected Grade: " + self.expectedGrade +
            "\nStudent Time: " + self.ftOrPt)                                    
'''







    

