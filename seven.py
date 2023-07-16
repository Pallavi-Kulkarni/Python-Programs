# Write a Python function that takes a string s containing parentheses and returns True if s is well bracketed and False otherwise

s=input("Enter a string: ")
depth=0
for i in s:
    if i=='(':
        depth+=1
    elif i==')':
        depth-=1
if depth==0:
    print("True")
else:
    print("False")

