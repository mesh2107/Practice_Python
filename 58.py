yesnodata=input("do you want to enter data: ")
count=0
original=[]
while yesnodata=="yes":
    student={}
    count+=1
    student["rollno"]=count
    nam=input("enter name: ")
    per=input("enter percent: ")
    student["name"]=nam
    student["percent"]=per
    print(student)
    original.append(student)
    yesnodata=input("do you want to enter data: ")
print(original)
find=int(input("enter roll no to find "))
for i in range(0,count):
    if find==original[i]['rollno']:
        print("data match")
        print(original[i])
    