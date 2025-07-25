a=int(input("enter number: "))
b=int(input("enter number: "))
c=int(input("enter number to find: "))
e=0
if a<b:
    while a<=b:
        print(a)
        if a==c:
            e+=1
            break
        a+=1
    if e==1:
        print("value match")
        d=1
        while d <= 10:
            print(c, " ", d, " ", c * d)
            d += 1
    else:
        print("try again")
else:
    while a>=b:
        print(a)
        if a==c:
            e+=1
            break
        a-=1
    if e == 1:
        print("value match")
        d=1
        while d <= 10:
            print(c, " ", d, " ", c * d)
            d+= 1
    else:
        print("try again")

