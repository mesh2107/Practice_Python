num1=int(input("enter number: "))
opr=input("enter operator: ")
while opr!="=":
    num2=int(input("enter 2nd number: "))
    if opr=="+":
        print(num1+num2)
    elif opr=="-":
        print(num1-num2)
    elif opr=='*':
        print(num1*num2)
    elif opr=='/':
        print(num1/num2)


