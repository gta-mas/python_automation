#classes= user defined blueprints, prototypes
#classes include methods (functions in CLASS), class variables, instance variables, constructors (called when object are created within class)...

class Calculator:
    n = 100 #class variable

    def __init__(self, a, b): #default constructor
        self.a = a #instance variable
        self.b = b
        print("Default constructor of an object")

    def get_data(self):
        print("Method in class")

    def summ(self):
        return self.a + self.b + Calculator.n   #for class variables we can use both self. or "Claas name".


obj = Calculator(2, 3)
obj.get_data()
print(obj.summ())

obj1 = Calculator(4, 5)
obj1.get_data()
print(obj1.summ())


