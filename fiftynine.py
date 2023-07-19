# Write a Python function wellbracketed(s) that takes a string s containing parentheses 
# and returns True if s is well bracketed and False otherwise

def check(s):
    count=0
    for i in s:
        if i=='(':
            count+=1
        if i==')':
            count-=1
    if count==0:
        return True
    else:
        return False


s=input("Enter the string: ")
print(check(s))