# Design a python program to generate the “Grades: S,A,B,C,D,F” for the given marks obtained and maximum marks by the user.

def findGrade(mo,mm):
    marks=(mo/mm)*100
    if marks>=90:
        print("The Grade is S")
    elif marks>=70 and marks<90:
        print("The Grade is A")
    elif marks>=50 and marks<70:
        print("The Grade is B")
    elif marks>=40 and marks<50:
        print("The Grade is C")
    elif marks>=30 and marks<40:
        print("The Grade is D")
    else:
        print("The Grade is F")
mm=int(input("Enter the maximum marks: "))
mo=int(input("Enter the obtained marks: "))
findGrade(mo,mm)
        



