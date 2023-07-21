# Program to count number of characters and first 20 characters

fhand=open('sixtyonefile.txt','r')
charcount=0
for line in fhand:
    print(line)
    print(len(line))
    charcount+=len(line)
    first=0    
    for i in line:
        first+=1
        if(first==21):
            break               
        print(i,end=" ")
    print("\n")
        
print(charcount)


# hello how are you?
# is everything is good
# missing you from long time
# would like to meet you once...
# And yeahh 


