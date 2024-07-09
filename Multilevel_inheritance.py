                                 #Multilevel Inheritance
                                 
#Accept Student information and display information and calculate total mark and percentage
#Accept:(rno,name,Address)
#Display
#Accept_mark: (m1,m2,m3,m4,m5,m6)
#Display Mark with percentage

class student:
    def AcceptS(self):
        self.rno=int(input("Enter Roll No : "))
        self.name=input("Enter Name : ")
        self.address=input("Enter Address : ")
        
    def displayS(self):
        print("Student Roll No : ",self.rno)
        print("Student Name : ",self.name)
        print("Student Address: ",self.address)
        
class collage(student):
        def AcceptC(self):
         self.cno=int(input("Enter Collage No : "))
         self.cname=input("Enter Collage Name : ")
         self.caddress=input("Enter Collage Address : ")
        
        def displayC(self):
         print("Collage No : ",self.cno)
         print("Collage Name : ",self.cname)
         print("Collage Address: ",self.caddress)
        
class result(collage):
    def AcceptR(self):
        self.s1=int(input("Enter OOSE Mark : "))
        self.s2=int(input("Enter Pythone Mark : "))
        self.s3=int(input("Enter Java Mark : "))
        self.s4=int(input("Enter CS Mark : "))
        self.s5=int(input("Enter project Mark : "))
        self.s6=int(input("Enter Practicle Mark : "))
        
    def cal(self):
        self.total=self.s1+self.s2+self.s3+self.s4+self.s5+self.s6
        self.per=self.total/6
        print("Total Marks : ",self.total)
        print("Percentage : ",self.per)
    
ob=result()
ob.AcceptS()
ob.AcceptC()
ob.AcceptR()

print("\nPrint All information...\n")
ob.displayS()
ob.displayC()
ob.cal()
