# Classes are nothing but user defined blueprint or prototype
# Example if you want to develop calculator application you have to develop
# these functionalities in it (Sum , Multiplication , Addition , Constant )
# Class will have methods, class variables, instance variables, constructor etc
# Functions used in class are called as methods
# constructor is a method which automatically gets called when object is created for any class.
# default constructor: The default constructor is a simple constructor which doesn’t accept any arguments.
# Its definition has only one argument which is a reference to the instance being constructed.
# parameterized constructor: constructor with parameters is known as parameterized constructor.
# The parameterized constructor takes its first argument as a reference to the instance being constructed known as self
# and the rest of the arguments are provided by the programmer.


# ----------------------------------------------------------------------------------- #

class Calculator:
    num = 100  # class variables -- the variables you defined immediately in your class are "class variables"

    # if we don't call any constructor then default constructor should be called
    # self keyword is mandatory when you declare method inside the class
    # in python constructor name should be __init__

    def __init__(self, a, b):
        self.firstNumber = a  # here a & b are instance variables
        self.secondNumber = b
        print("I am get called automatically when object is created")

    def getData(self):
        print(" I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(2, 3)  # Syntax to create objects in python
obj.getData()
print(obj.Summation())

obj1 = Calculator(4, 5)  # Syntax to create objects in python
obj1.getData()
print(obj1.Summation())

print("****************************************************************************************************")


class car:

    def __init__(self, model, color):
        self.model = model
        self.color = color

    def show(self):
        print("Model is", self.model)
        print("Color is", self.color)


Audi = car("A8", "Red")
Tesla = car("Model s plaid", "Black")

Audi.show()
Tesla.show()

print("****************************************************************************************************")


class GreatPeople:
    def __init__(self, place, work):
        self.place1 = place
        self.work1 = work

    def country(self):
        print(" country is ", self.place1)
        print(" work done in", self.work1)


Elon_Musk = GreatPeople("USA", "Technology")
Ratan_TaTa = GreatPeople("INDIA", "Automobile")
Naval_Ravikant = GreatPeople("USA-INDIA", "Entrepreneur")

Elon_Musk.country()
Ratan_TaTa.country()
Naval_Ravikant.country()

print("****************************************************************************************************")


class ClassProfession:
    def __init__(self, InstanceArgument, InstanceArgument2, InstanceArgument3):

        self.InstanceVariable = InstanceArgument
        self.InstanceVariable2 = InstanceArgument2
        self.InstanceVariable3 = InstanceArgument3

    def MethodArtist(self):
        print("the name of Professional is", self.InstanceVariable)
        print("the Professional is", self.InstanceVariable)
        print("the Professional is from", self.InstanceVariable2)


Obj_Coldplay = ClassProfession("Coldplay","Singer", "United Kingdom")
Obj_Piyush_Bansal = ClassProfession("Piyush Bansal", "Businessman", "India")
Obj_Narendra_Modi = ClassProfession("Narendra Modi", "Politician", "India")

Obj_Coldplay.MethodArtist()
Obj_Piyush_Bansal.MethodArtist()
Obj_Narendra_Modi.MethodArtist()

