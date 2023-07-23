# "A list rotation consists of taking the last element and moving it to the front. For
#instance, if we rotate the list [1,2,3,4,5], we get [5,1,2,3,4]. If we rotate it again, we get
#[4,5,1,2,3]. Write a Python function rotatelist(ls,k) that takes a list ls and a positive
#integer k and returns the list ls after k rotations. If k is not positive, your function
#should return ls unchanged. Note that your function should not change ls itself, and
#should return the rotated list. Here are some examples to show how your function
#shouldwork."

def rotate(list,k):
    listtwo=list
    if k<0:
        return list
    for i in range(k):
        listone=[]
        listone.append(listtwo[-1])
        listone.extend(listtwo)
        listone.pop(5)
        listtwo=listone
    return listone

list=[1,2,3,4,5]
k=int(input("Enter the number of rotation: "))
print(rotate(list,k))