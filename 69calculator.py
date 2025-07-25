operate=input("do u want to operate: ")
while operate=='yes':
    operator=input("enter operator: ")
    num1=int(input("enter number: "))

    num2=int(input("enter number: "))
    def sum():
        print(num1+num2)
    def sub():
        print(num1-num2)
    def mult():
        print(num1*num2)
    def div():
        print(num1/num2)


    if operator=='sum'or operator=='+':
        sum()
    elif operator =='sub'or operator=='-':
        sub()
    elif operator=='mult'or operator=='*':
        mult()
    elif operator=='div'or operator=='/':
        div()
    else:
        print("invalid operator")
    operate = input("do u want to operate: ")
