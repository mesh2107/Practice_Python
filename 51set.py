a={}
b=list(a)
l1=len(b)
print(l1)
while l1<5:
    newad=input("new admission: ")
    if newad=="yes":
        name=input("enter name : ")
        if name in b:
            name=input("re enter name: ")
            b.append(name)
        else:
            b.append(name)
    else:
        print("OKAY")
    l1=len(b)
    print(l1)
    print(b)
print(b)
admission=set(b)
print(admission)
