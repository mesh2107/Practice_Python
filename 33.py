a=[1,2,3,4,5,6]
b=["aaa","bbb","ccc","ddd","eee","fff"]
price=[10,20,30,40,50,60]
total=0
num=int(input("enter number: "))
l1=len(a)

for i in range(0,6):
    if num==a[i]:
        print(i)
        break
print(b[i])
quantity=int(input("enter quantity: "))
total=(quantity*price[i])
print()
print("YOUR BILL")
print(b[i]," ",quantity," ",total)

