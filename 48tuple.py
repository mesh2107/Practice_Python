side=()
x=list(side)
length=int(input("enter length: "))
for i in range(0,length):
    name=input("enter name: ")
    x.append(name)
print(x)
y=tuple(x)
print(y)
temp=(length//3)
(A)=y[0:temp]
num=temp
num+=temp
(B)=y[temp:num]
(C)=y[num:]
print(A)
print(B)
print(C)
