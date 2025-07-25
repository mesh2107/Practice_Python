student1={}
student2={}
student3={}
student4={}
student5={}
yesno=input("do you want to enter data: ")
while yesno=="yes":
    student=int(input("enter data of which student: "))
    if student==1:
        key1 = input("enter keyword")
        value1 = input("enter " + key1 + ":")
        student1[key1] = (value1)
    elif student==2:
        key2 = input("enter keyword")
        value2 = input("enter " + key2 + ":")
        student2[key2] = (value2)
    elif student==3:
        key3 = input("enter keyword")
        value3 = input("enter " + key3 + ":")
        student3[key3] = (value3)
    elif student==4:
        key4 = input("enter keyword")
        value4 = input("enter " + key4 + ":")
        student4[key4] = (value4)
    elif student==5:
        key5 = input("enter keyword")
        value5 = input("enter " + key5 + ":")
        student5[key5] = (value5)
    yesno = input("do you want to enter data: ")

print(student1)
print(student2)
print(student3)
print(student4)
print(student5)



find=(input("enter roll no to find: "))
if find=="1" or find=="A":
    print(student1)
elif find=="2" or find=="B":
    print(student2)
elif find=="3" or find=="C":
    print(student3)
elif find=="4" or find=="D":
    print(student4)
elif find=="5" or find=="E":
    print(student5)
else:
    print("NO DATA")