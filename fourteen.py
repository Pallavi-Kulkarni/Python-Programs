# Write a Python program to remove the characters which have odd index values of a given string.

s="Hello World"
mylist=[]

for count,value in enumerate(s):
    if count%2==0:
        mylist.append(value)
print(mylist)

# 0 1 2 3 4 5 6 7 8 9 10
# H E L L O   W O R L D
# Result: H L 0 W R D