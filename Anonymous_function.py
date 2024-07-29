# Write an anonymous function to find area of square and rectangle
area=lambda s:s*s
rec=lambda l,w : l*w

s=int(input("Enter Side : "))
l=int(input("Enter Length : "))
w=int(input("Enter width : "))

print("Area of Square : ",area(s))
print("Area of Rectangle : ",rec(l,w))