a=["aaa","bbb","ccc","ddd","eee"]
b=[1,3,5,4,2]
lb=len(b)
c=[]

for i in range(0,5):
    min=b[i] #min = 1
    for j in range(i+1,5):
        if min>b[j]:
            min=b[j]
            b.insert(i,min)
    c.append(min)

print(c)


