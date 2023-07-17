# Find Smallest in list

mylist=[4,7,3,8,2]
small=mylist[0]
for i in mylist:
    if i<small:
        small=i
print("The smallest number is: ",small)