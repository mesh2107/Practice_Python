for a in range(1,6):
    for b in range(1,a+1):
        if a==b:
            print("0",end="")
        else:
            print("1",end="")
    print()
print()

for c in range(1,6):
    for d in range(1,c+1):
        if d==2 or d==4:
            print("0",end="")
        else:
            print("1",end="")
    print()
print()

for e in range(1,6):
    for f in range(1,e+1):
        if e%2!=0:
            print("0",end="")
        else:
            print("1",end="")
    print()
print()

for g in range(1,6):
    for h in range(1,g+1):
        if h==1:
            print("1",end="")
        if h%2==0:
            print("p",end="")
        if h==3:
            print("*",end="")
        if h==5:
            print("5",end="")
    print()
print()

for i in range(1,6):
    for j in range(1,i+1):
        print(i,end="")
    print()
print()

for i in range(1,6):
    for j in range(1,6):
        print(i,end="")
    print()
print()

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("0",end="")
        else:
            print("1",end="")
    print()
print()

for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("0",end="")
        else:
            print(" ",end="")
    print()
print()

for i in range(1,6):
    for j in range (1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("0",end="")
        elif i==3 and j==3:
            print("3",end="")
        else:
            print("2",end="")
    print()
print()

for i in range(1,6):
    for j in range(1,i+1):
        if(i+j)%2!=0:
            print("1",end="")
        else:
            print("0",end="")
    print()
print()

k=1
for i in range(1,5):
    for j in range(1,i+1):
        print(k,end="")
        k+=1
    print()
print()

for i in range(1,6):
    sum=0
    for j in range(1,i+1):
        sum+=j
    print(sum,end="")
    print()
print()

for i in range(1,6):
    sum=0
    for j in range(1,i+1):
        sum+=j
    for k in range(1,sum+1):
        print("*",end="")
    print()
print()

for i in range(1,4):
    for j in range(1,4):
        print(i,j,end="")
        print()
print()

for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print("1",end="")
        if j<i:
            print("2",end="")
        if i<j:
            print("0",end="")
    print()
print()

for i in range(1,6):
    for j in range(1,6):
        if i==j or i+j==6:
            print("*",end="")
        else:
            print("0",end="")
    print()
print()

