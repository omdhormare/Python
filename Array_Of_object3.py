class collage:
    def accept(c):
        c.cno=int(input("Enter Collage No : "))
    def dis(s):
        print("Collage No :",s.cno)
     
a=[]   
n=int(input("Enter limit : "))
for i in range(0,n):
    ob=collage()
    ob.accept()
    a.append(ob)

for i in range(0,n):
    a[i].dis()
