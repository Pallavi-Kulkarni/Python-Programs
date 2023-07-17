# Print length of input string terminated with space

s=input("Enter the string: ")
count=0
for i in s:
    if i==" ":
        continue
    else:
        count+=1
print("The length of the string terminated with space is: ",count)