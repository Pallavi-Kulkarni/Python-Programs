# Write a python program to print last n lines from file

linecount=0
list=[]
fhand=open('sixtyonefile.txt','r')
n=int(input("Enter the number of last lines to be printed: "))

for line in fhand:
    linecount+=1
    list.append(line)
print(linecount)

for line in range(linecount-n,linecount):
    print(list[line])   

fhand.close()