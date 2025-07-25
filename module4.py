import listmodule
data1=[]
data2=[]
data3=[]
choice1=input("do u want to enter new student: ")
while choice1=='yes':
    roll=int(input("enter roll: "))
    name=input("enter name:")
    data1.append(roll)
    data1.append(name)
    data2.append(roll)
    data2.append(name)
    data3.append(roll)
    data3.append(name)
    listmodule.student.append(data1)
    listmodule.result.append(data2)
    listmodule.attend.append(data3)
    choice2=input("do u want to enter further data: ")
    while choice2=='yes':
        what=input("what data u want to enter: ")
        if what=='r':
            marks=int(input("enter marks: "))
            data2.append(marks)
            listmodule.result.append(data2)
        elif what=='a':
            days=input("enter days: ")
            data3.append(days)
            listmodule.attend.append(data3)
        choice2 = input("do u want to enter further data: ")
    choice1 = input("do u want to enter new student: ")



print(listmodule.student)
print(listmodule.result)
print(listmodule.attend)