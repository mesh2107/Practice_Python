list=[]
length=len(list)

while length<10:
    name=input("enter name in list: ")
    if name in list:
        list.remove(name)
    else:
        list.append(name)
    length=len(list)
    print(list)
    print(length)

print(list)