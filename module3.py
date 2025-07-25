import listmodule
a=list(listmodule.admission)
new=input("new admission: ")
roll=0
while new=='yes':
    roll+=1
    data=[]
    l=len(data)
    name=input("enter name: ")
    if name not in a:
        data.append(name)
        data.append(roll)
        a.append(data)
    elif name in a:
        print("already")
    new = input("new admission: ")

print(a)
