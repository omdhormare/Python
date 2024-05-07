n=int(input("Enter Number : "))
sum=0
n1=n
while(n>0):
    d=n%10
    sum=d+(sum*10)
    n=n//10

if(n1==sum):
    print("Palindrom Number...")
else:
    print("Not palindrom...")
