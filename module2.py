import listmodule
l=len(listmodule.list)
while l<5:
    name=input("enter name: ")
    listmodule.list.append(name)
    l=len(listmodule.list)

print(listmodule.list)


while l>0:
    find=input("enter to find: ")
    if find in listmodule.list:
        print("already")
        break
    elif find not in listmodule.list:
        listmodule.list.append(find)
print(listmodule.list)
