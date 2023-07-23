# Write a Python function that takes two lists and returns True if they have at least one common member.

def common(list1,list2):
    isCommon=False
    for i in list1:
        if i in list2:
            isCommon=True
    return isCommon


list1=[1,2,3,4,5]
list2=[4,9,0,6,7]
print(common(list1,list2))