''''
A) Write a Python program to compute element-wise sum of given tuples.
Original lists: (1, 2, 3, 4) (3, 5, 2, 1) (2, 2, 3, 1)
Element-wise sum of the said tuples: (6, 9, 8, 6)
'''

t=(1, 2, 3, 4)
t1=(3, 5, 2, 1)
t2=(2, 2, 3, 1)

print(t,t1,t2)

ans=tuple(map(sum, zip(t, t1, t2)))

print(ans)