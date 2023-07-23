# Write a Python function that takes two sorted lists and return merged List.

def merge(list1,list2):
    return list1+list2


list1=[6,1,5,4,3]
list2=[2,10,7,4,11]
list1.sort()
list2.sort()
print(merge(list1,list2))
