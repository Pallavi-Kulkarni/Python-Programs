# Python Program to Read a File and Capitalize the First Letter of Every Word in the File

fhand=open('seventyfivefile.txt','r')
list=[]

for line in fhand:
    list=line.split(" ")
    for i in list:
        print(i.capitalize())

fhand.close()    
    

