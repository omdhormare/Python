n=int(input("Enter Number : "))
sum=0
n1=n
while(n>0):
    d=n%10
    sum=sum+(d*d*d)
    n=n//10
if(sum==n1):
    print("Armstrong Number...")
else:
    print("Not Armstrong Number..")
