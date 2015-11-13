#
# Lecture lab 7 - part 3
#
# mypeople3.py
#

# import the sys module, which contains the path attribute that we want to modify
import sys

# Add the location of our python code, so python can find it
sys.path.append(r"..\mymodules")

# import the module we created, now that python knows where to find it
import person

def writePeople(peopleList):
    # create/overwrite the output file
    myFile = open(r".\mypeople.txt", "w")
    # iterate through the list of Person objects and write the
    # attributes for each to the file
    for p in peopleList:
        myFile.write(p.getName() + "\n")
        myFile.write(str(p.getAge()) + "\n")
    # close the file
    myFile.close()

# instantiate 3 objects of type Person
p1 = person.Person("Nathan Bailey", 56)
p2 = person.Person("Charla Patton", 53)
p3 = person.Person("Greg Smith", 55)

# create a list of Person objects
plist = [p1, p2, p3]

writePeople(plist)
