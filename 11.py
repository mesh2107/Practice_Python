a=int(input("enter number: "))
b=int(input("enter number: "))
if a<b:
    while a<=b:
        if a%2==0 :
            print(a,"is even number.")
        else :
            print(a,"is odd number.")
        a+=1
else:
    while a>=b:
        if a%2==0:
            print(a,"is even number.")
        else:
            print(a,"is odd number.")
        a-=1