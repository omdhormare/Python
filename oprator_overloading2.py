'''A) Write a python class to accept a string and number n from user and display n 
repetition of strings by overloading * operator.'''

class string:
    def __init__(self):
        self.s=input("Enter String : ")
        self.n=int(input("Enter No Repetion : "))
    
    def __mul__(self,ob):
        print(ob.s * ob.n)
        
ob=string()
ob*ob