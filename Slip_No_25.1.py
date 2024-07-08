'''
A) Write a Python function that accepts a string and calculate the number of upper case 
letters and lower case letters. 
Sample String: 'The quick Brown Fox'
Expected Output: 
No. of Upper case characters: 3
No. of Lower case characters: 13
'''
def upper_lower():
    
    upper=0
    lower=0
    
    s=input("Enter String : ")
    for char in s:
        if(char.isupper()):
            upper+=1
        elif(char.islower()):
            lower+=1
    
    print("No. of Upper case characters : ",upper)
    print("No. of Lower case characters : ",lower)
    

upper_lower()