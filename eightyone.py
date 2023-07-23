# Write a Python program to print all the even indexed elements

list=[2,3,4,1,7,8,9,6]

for index,value in enumerate(list):
    if index%2==0:
        print(index,value)