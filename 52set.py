c={}
m={}
x=list(c)
y=list(m)
l1=len(x)
l2=len(y)
while l1<=5 and l2<=5:
    if l1==5 and l2==5:
        break
    choice=input("enter branch: ")
    name=input("enter name: ")
    if choice=="comp" and l1<5 :
       if name in x:
           name=input("re enter:")
           if name in x:
               print("try again")
           else:
               x.append(name)
       else:
           x.append(name)
    elif choice=="mech"and l2<5:
        if name in y:
            name = input("re enter:")
            if name in y:
                print("try again")
            else:
                y.append(name)
        else:
            y.append(name)
    elif l1==5 and l2<5:
        if name in y:
            name = input("re enter:")
            if name in y:
                print("try again")
            else:
                y.append(name)
        else:
            y.append(name)
    elif  l2==5 and l1<5:
        if name in x:
            name = input("re enter:")
            if name in x:
                print("try again")
            else:
                x.append(name)
        else:
            x.append(name)
    elif choice!="comp" and choice!="mech":
        print("NO BRANCH")
    l1=len(x)
    l2=len(y)
    print(x)
    print(y)

comp=set(x)
mech=set(y)
print(comp)
print(mech)

