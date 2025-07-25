comp=[]
civil=[]

l1=len(comp)
l2=len(civil)

print(l1)
print(l2)
while l1<=5 and l2<=5:
    if l1==5 and l2==5:
        break
    choice=input("enter branch : ")
    name=input("enter name :")
    if choice=="comp" and l1<5:
        comp.append(name)

    elif choice=="civil" and l2<5:
        civil.append(name)

    elif l1==5 and l2<5:
        civil.append(name)
    elif l2==5 and l1<5:
        comp.append(name)
    else:
        print("invalid data")
    l1 = len(comp)
    l2 = len(civil)

    print(l1)
    print(l2)

print(comp)
print(civil)

