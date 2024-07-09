                        #There Are Three Inheritance in python:
                        #      1)Single inheritance
                        #     2)Multiple Inheritance
                        #      2)Multilevel Inheritance 
                        
class Base:
    def Accept(self):
        self.a=int(input("Enter 1 Number : "))
        self.b=int(input("Enter 2 Number : "))
        
class Derived(Base):
      def Display(self):
          print("Addtion : ",self.a+self.b)
        
    
ob=Derived()
ob.Accept()
ob.Display()