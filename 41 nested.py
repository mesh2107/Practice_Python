a=["aaa","bbb","ccc","ddd","eee","fff"]
b=[]
la=len(a)
lb=len(b)
while lb<5:
    val=input("enter: ")
    if val in a:
        a.remove(val)
        b.append(val)
    elif val not in a:
        b.append(val)
    la=len(a)
    lb=len(b)
    print(lb)
    print(b)
    print(a)