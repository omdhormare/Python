class string:
    def __init__(self):
        self.s=input("Enter String : ")
        
    def __add__(self,ob1):
        self.c = ob1.s + self.s
        print("Addtion String : ",self.c)
        
ob=string()
ob1=string()
ob+ob1