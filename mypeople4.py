#
# Lecture lab 7 - part 4
#
# mypeople4.py
#

# Output example:
# Name: Nathan Bailey
# , Age: 56
# Name: Charla Patton
# , Age: 53
# Name: Greg Smith
# , Age: 55

# import the sys module, which contains the path attribute that we want to modify
import sys

# Add the location of our python code, so python can find it
sys.path.append(r"..\mymodules")

# import the module we created, now that python knows where to find it
import person

def createPersonObject(myFile):
    name = myFile.readline()
    age = myFile.readline()
    p = person.Person(name, int(age))
    return p

def readPeople():
    myFile = open(r".\mypeople.txt", "r")
    # read the data from the file; create an object of type Person
    p1 = createPersonObject(myFile)
    p2 = createPersonObject(myFile)
    p3 = createPersonObject(myFile)
    # show the objects
    p1.printMe()
    p2.printMe()
    p3.printMe()
    # close the file
    myFile.close()

readPeople()
