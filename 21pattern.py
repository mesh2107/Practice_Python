for i in range(1,6):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end="")
    print()
for i in range(4,0,-1):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,i+1):
        print(i,end="")
    print()

for i in range(1,6):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,(i+1)):
        print(j," ",end="")
    print()
print()

for i in range(1,6):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("0 ",end="")
    print()
for i in range(4,0,-1):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,i+1):
        print("0 ",end="")
    print()
print()

for i in range(0,10,+2):
    for j in range(0,(8-i)+2,+2):
        print(" ",end="")
    for j in range(0,i+2,+2):
        print(i,end="")
    print()
for i in range(8,-2,-2):
    for j in range(0,(8-i)+2,+2):
        print(" ",end="")
    for j in range(0,i+2,+2):
        print(i,end="")
    print()
print()

for i in range(5,0,-1):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,i+1):
        if i%2!=0:
            print("0 ",end="")
        else:
            print("1 ",end="")
    print()
for i in range(2,6):
    for j in range(1,(5-i)+1):
        print(" ",end="")
    for j in range(1,i+1):
        if i%2!=0:
            print("0 ",end="")
        else:
            print("1 ",end="")
    print()
print()

for i in range(1,6):
    for j in range(1,i+1):
        if i==j:
            print(" * ",end="")
        else:
            print(" ",end="")
    print()
for i in range(4,0,-1):
    for j in range(1,i+1):
        if i==j:
            print(" * ",end="")
        else:
            print(" ",end="")
    print()
print()

sum=0
for i in range(1,6):
    sum+=i
    for j in range(1,(15-sum)+1):
        print(" ",end="")
    for j in range(1,sum+1):
        print("*",end="")
    print()