check=input("which num do u want to check: ")
num=int(input("enter num: "))
if check=='a':
    x = num
    y = num
    sum = 0
    count = 0
    while y > 0:
        y = y // 10
        count += 1
    d = count
    while num > 0:
        b = num % 10
        sum = sum + (pow(b, d))
        num = num // 10
    if (x == sum):
        print("armstrong no")
    else:
        print("not armstrong")

elif check=='p':
    z=num
    s=0
    while num>0:
        e=num%10
        s=(s*10)+e
        num=num//10
    if z==s:
        print("palindrome")
    else:
        print("not palindrome")
elif check=='both':
    if check=='both':
        x = num
        y = num
        sum = 0
        count = 0
        while y > 0:
            y = y // 10
            count += 1
        d = count
        while num > 0:
            b = num % 10
            sum = sum + (pow(b, d))
            num = num // 10
        if (x == sum):
            print("armstrong no")
        else:
            print("not armstrong")
    if check=='both':
        z = num
        s = 0
        while num > 0:
            e = num % 10
            s = (s * 10) + e
            num = num // 10
        if z == s:
            print("palindrome")
        else:
            print("not palindrome")



