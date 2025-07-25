a=int(input("enter no :"))
b=int(input("enter no: "))
sum=0
if a<b:
    while a<=b:
        print(a)
        if a%2!=0:
            sum+=a
        a+=1
    print("addition is ",sum)
    while sum>=1:
        if sum%2==0:
            c=1
            while c<=10:
                print(sum," ",c,"",sum*c)
                c+=1
        sum-=1
else:
    while a>=b:
        print(a)
        if a%2!=0:
            sum+=a
        a-=1
    print("addition is ",sum)
    while sum>=1:
        if sum%2==0:
            c=1
            while c<=10:
                print(sum," ",c," ",sum*c)
                c+=1
        sum-=1