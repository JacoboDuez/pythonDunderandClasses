class Calculator:
    def __init__(self,a,b):
        self.a =  a
        self.b =  b
    def Add(self,a,b):
        return a + b

    def Substract(self,a,b):
        return a-b

    def Multiply(a,b):
        return a*b

    def Divide(self,a,b):
        if b==0:
            return "Error: Division by zero"
        return a/b
    def __str__(self):
        return f"Calculator with values defined as  a= {self.a} and b =  {self.b}"

class Counter:
    def __init__(self):
        self.count = 0
    def __increase__(self,value):
        self.count +=value
    def __decrease__(self):
        self.count-=1
    def __reset__(self):
        self.count = 0
    def __getCount__(self):
        return self.count
    def __add__(self,other):
        if isinstance(other,Counter):
            self.count = self.count  + other.count
    def __sub__(self,other):
        if isinstance(other,Counter):
            self.count -=other.count
        else:
            raise Exception("Unsupported operand type for subtraction")
    def __mul__(self,other):
        if isinstance(other,Counter):
            self.count *= other.count
        else:
            raise Exception("Unsupported operand type for multiplication")

    
    def __sub__(self,other):
        if isinstance(other,Counter):
            self.count = self.count - other.count
        else:
            raise Exception("Unsupported operand type for subtraction")

    def __str__(self):
        return  f"the value of the counter is {self.count}"
    


print(__name__)

    
if __name__ == "__main__":
    valueA =  90
    valueB =  9
    calculatorInstance =  Calculator(valueA,valueB)
    myCounter1 =  Counter()
    myCounter2 =  Counter()

    myCounter1.__increase__(30)
    myCounter2.__increase__(21)
    print(myCounter1.__getCount__())

    print(myCounter1 + myCounter2)

    print(calculatorInstance.Add(valueA,valueB))
    print(calculatorInstance.Substract(valueA,valueB))
    print(type(calculatorInstance.Multiply(valueA,valueB)))
    print(calculatorInstance.Multiply(valueA,valueB))
    print(calculatorInstance.Divide(valueA,valueB))
    









