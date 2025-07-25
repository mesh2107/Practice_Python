class A:
    def fun1(self):
        a=10
        b=56
        print(a+b)
    def fun2(self):
        a=10
        b=67
        return(a+b)
    def fun3(self,c,d):
        print(c*d)

    def fun4(self,e,f):
        return(e*f)

obj=A()
obj.fun1()
print(obj.fun2())
c=int(input("enter: "))
d=int(input("enter: "))
obj.fun3(c,d)
e=int(input("enter: "))
f=int(input("enter: "))
print(obj.fun4(e,f))
