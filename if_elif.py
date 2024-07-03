name=input("Enter Name : ")
s1=int(input("Enter 1 subject Mark : "))
s2=int(input("Enter 2 subject Mark : "))
s3=int(input("Enter 3 subject Mark : "))
s4=int(input("Enter 4 subject Mark : "))
s5=int(input("Enter 5 subject Mark : "))
s6=int(input("Enter 6 subject Mark : "))

per=float(s1+s2+s3+s4+s5+s6)/6
print("Student Name : ",name)
print("Pecentage : ",per)

#find A garde
if(per>=90):
    print("O")
elif(per>=85):
    print("A+")
elif(per>=60):
    print("A")
elif(per>=50):
    print("B")
elif(per>=40):
    print("Pass")
else:
    print("Fail")


