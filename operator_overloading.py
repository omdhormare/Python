class demo:
    def __init__(self):
        self.a=int(input("Enter 1 No : "))
        self.b=int(input("Enter 2 No : "))
        
    def __add__(self,ob):
        print("Addtion : ",self.a + self.b)
        
ob=demo()
ob+ob