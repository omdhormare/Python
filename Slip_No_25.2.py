#B) Write a Python script to Create a Class which Performs Basic Calculator Operations.

class operation:
    def __init__(self):
            self.a=int(input("Enter Number 1 : "))
            self.b=int(input("Enter Number 2 : "))
           
            
    def Calculator(self):
          print("\nAddtion : ",self.a+self.b)
          print("Subtraction : ",self.a-self.b)
          print("Multiplication : ",self.a*self.b)
          print("Division : ",self.a/self.b)
    
ob=operation()
ob.Calculator()