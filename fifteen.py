# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

s="Hello World"
mylist=[]
mylist.append(s[len(s)-1])

for i in range(len(s)-1):
    if(i==9):
        break
    mylist.append(s[i+1])
mylist.append(s[0])

new=str(mylist)
print(new)

