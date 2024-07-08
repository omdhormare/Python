'''
Write a Python script to sort (ascending and descending) a dictionary by key and 
value
'''

d={
    "Roll_no" : 11,
    "name" : "om",
    "per" : 92,
    
    "Roll_no" : 1,
    "name" : "omkar",
    "per" : 10
}
asc=dict(sorted(d.items()))
print(asc)


dsc=dict(sorted(d.items(),reverse=True))
print(dsc)