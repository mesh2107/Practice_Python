a=[]
for i in range(0,5):
    n=input("enter name in list: ")
    a.append(n)
print(a)
name=input("enter the name you want to remove: ")
if name in a:
    a.remove(name)
else:
    a.append(name)
print(a)