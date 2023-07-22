# Write a Python program print to first 10 lines and last 10 lines in a file

fhand=open('seventyfile.txt','r')
count=0
for line in fhand:
    count+=1
    if count<11 or count>20:
        print(line)
fhand.close()