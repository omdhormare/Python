'''
A) Write a Python program to accept n numbers in list and remove duplicates from a list.
'''

list1=[]

n=int(input("Enter Limit : "))

for i in range(0,n):
    num=int(input("Enter Numbers : "))
    list1.append(num)

print("Orignal List : ",list(list1))
print("Remove duplicates Number  : ",list(set(list1)))