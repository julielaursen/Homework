#
# Lecture lab 7 - part 2
#
# mypeople2.py
#

# import the sys module, which contains the path attribute that we want to modify
import sys

# Add the location of our python code, so python can find it
sys.path.append(r"..\mymodules")

# import the module we created, now that python knows where to find it
import person

# instantiate an object of type Person and call printMe
p = person.Person("Nathan Bailey", 56)

p.printMe()
