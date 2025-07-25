a=[1,2,3,4,5,6]
b=["aaa","bbb","ccc","ddd","eee","fff"]
price=[10,20,30,40,50,60]
avl=[10,10,10,10,10,10]
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
upd=(avl[i]-quantity)
avl.pop(i)
avl.insert(i,upd)
print(avl)
print()
print("YOUR BILL")
print(b[i]," ",quantity," ",total)