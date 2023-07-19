# Python program to find average of palindrome numbers in a given list.
list=[141,232,126,333,464,123]
sum=0
count=0

for i in range(len(list)):
    rev=0
    x=list[i]
    while(x>0):
        rem=x%10
        rev=(rev*10)+rem
        x=x//10
    if(list[i]==rev):
        sum+=list[i]
        count+=1
print(count)
average=sum/count
print(average)

