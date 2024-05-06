n=int(input("Enter Number : "))
sum=0
for i in range(1,n+1):
    if(n%i==0):
       sum=sum+1
if(sum==2):
    print("Prime Number...")
else:
        print("Not Prime Number...")
