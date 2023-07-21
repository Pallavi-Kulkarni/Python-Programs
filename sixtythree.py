# Write a Python program to read a file line by line and store it into a list.
list=[]
fhand=open('sixtyonefile.txt','r')
for line in fhand:
    list.append(line)
print(list)
fhand.close()