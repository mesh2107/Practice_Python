def hello(x):
    a=[]
    for i in range (0,5):
        name=input("enter name: ")
        a.append(name)
    print(a)
    if x in a:
        a.remove(x)
        print(a)
    else:
        a.append(x)
        print(a)
x=input("name to find: ")
hello(x)

