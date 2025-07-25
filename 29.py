comp=[]
civil=[]

l1=len(comp)
l2=len(civil)
for i in range(0,10):
    choice = input("enter branch: ")
    name = input("enter name: ")
    if choice == "comp" and l1 <= 4:
        comp.append(name)
        l1=len(comp)
    elif choice == "comp" and l1 >= 4:
        civil.append(name)
        l2=len(civil)
    elif choice == "civil" and l2 <= 4:
        civil.append(name)
        l2=len(civil)
    elif choice == "civil" and l2 >= 4:
        comp.append(name)
        l1=len(comp)
    elif choice!="comp" or choice!="civl":
        print("invalid branch")


print(l1)
print(l2)
print(comp)
print(civil)
