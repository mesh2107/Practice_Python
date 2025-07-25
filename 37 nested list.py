a=[[1,2,3],[4,5,6],[7,8,9]]
print(a[0][0])
print(a[0])
print(a[1])
print(a[2])

for i in range (0,3):
    for j in range (0,3):
        print(a[i][j],end="")
    print()

for i in range(0,3):
    for j in range(0,3):
        if 6==a[i][j]:
            print("no exist")