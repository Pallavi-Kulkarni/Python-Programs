# Print sum of numbers and number of elements
n=int(input("Enter the number of elements: "))
print("The number of elements is: ",n)
sum=0
for i in range(n):
    a=int(input("Enter the number: "))
    sum+=a
print("The sum of elements is: ",sum)