class A:
    a=100
obj=A()
print(obj.a)


class add:
    def funct1(self):
        a=10
        b=80
        print(a+b)
obj2=add()
obj2.funct1()

class B:
    def add(self,c, d):
        print(c + d)
obj3=B()
obj3.add(75,10)

class C:
    def mult(self):
        e = 80
        f = 6
        return (e * f)
obj4=C()
print(obj4.mult())
