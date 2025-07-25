a=int(input("enter number: "))
b=int(input("enter number: "))
count=0
if a<b:
    for i in range(a+1,b):
        print(i)
        count+=1
else:
    for i in range(a-1
            ,b,-1):
        print(i)
        count+=1
print("count=",count)