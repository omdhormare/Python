#6(2,3,1)=6 perfect Number
n=int(input("Enter Number : "))
sum=0
for i in range(1,n):
    if(n%i==0):
        sum=sum+i
if(sum==n):
    print("Perfect Number....")
else:
        print("Not Perfect Number...")
