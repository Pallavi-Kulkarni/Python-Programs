# Design a Python program to find the average of best two marks out of three marks taken as input

def avg(m1,m2,m3):
    if m1<m2 and m1<m3:
        m=(m2+m3)/2
    elif m2<m1 and m2<m3:
        m=(m1+m3)/2
    else:
        m=(m1+m2)/2
    return m

m1=int(input("Enter the first marks: "))
m2=int(input("Enter the second marks: "))
m3=int(input("Enter the third marks: "))

print("The average of two best marks is: ",avg(m1,m2,m3))

