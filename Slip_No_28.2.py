'''
B) Write a Python program to accept two lists and merge the two lists into list of tuple.

'''



list1=[10,20,30,40,50]
list2=[1000,2000,3000,4000,5000]

list3=(list(zip(list1,list2)))
print(list3)