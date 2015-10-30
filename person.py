#
# class Person
#

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
    def setName(self, value):
        self.__name = value
    def setAge(self, value):
        self.__age = value
    def printMe(self):
        print("Name: %s, Age: %d" % (self.getName(), self.getAge()))
