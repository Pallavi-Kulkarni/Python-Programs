# Program to count number of lines a file

fhand=open('sixtyonefile.txt','r')
count=0
for line in fhand:
    count+=1
print(count)
fhand.close()