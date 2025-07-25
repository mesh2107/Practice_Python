side=()
x=list(side)
for i in range(0,10):
    name=input("enter name: ")
    x.append(name)
print(x)
y=tuple(x)
print(y)
(A)=y[0:3]
(B)=y[3:6]
(C)=y[6:10]
print(A)
print(B)
print(C)