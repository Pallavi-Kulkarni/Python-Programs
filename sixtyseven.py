# Write a program to read n number of lines from the keyboard and to write them onto a file

fhand=open('sixtysevenfile.txt','w')

n=int(input("Enter the number of lines: "))
for line in range(n):
    line=input("Enter the line.....")
    fhand.write(line+'\n')
fhand.close()