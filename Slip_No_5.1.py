'''
A) Write a Python script using class, which has two methods get_String and 
print_String. get_String accept a string from the user and print_String print the string in 
upper case. 
'''

class String:
    def get_string(self):
        self.s=input("Enter String : ")
    def print_string(self):
        print("Orignal String : ",self.s)
        print("Upper Case  String : ",self.s.upper())
        
    

ob=String()
ob.get_string()
ob.print_string()
