                                    #Multiple inheritance

class A:
    def __init__(self):
        print("I am Class A...")

class B:
    def __init__(self):
        print("I am Class B...") 

class C(A,B):
    def __init__(self):
        print("I am Class C...")
        A.__init__(self) 
        B.__init__(self)
        

ob=C()
