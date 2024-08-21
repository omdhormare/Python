class emp:
    def accept(self):
        self.eno=int(input("Enter Emp No : "))
        self.name=input("Enter Emp Name : ")
        self.salary=int(input("Enter Salary : "))
    def dis(self):
        print("\nEmp No : ",self.eno)
        print("Emp Name : ",self.name)
        print("Emp salary : ",self.salary)
        
a=[]
n=int(input("Enter Limit : "))
for i in range(0,n):
    ob=emp()
    ob.accept()
    a.append(ob)

for i in range(0,n):
    a[i].dis()