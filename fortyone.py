# Sum of a only 5 even numbers entered by user (break and continue)

sum=0
count=0
while True:
    n=int(input("Enter the number: "))
    count+=1   
    if n%2==0:
        sum+=n
    else:
        continue
    if count==5:
        break
print(sum)
