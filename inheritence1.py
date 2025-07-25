class a:
    def add(self):
        a=10
        b=90
        print(a+b)
class b(a):
    def sub(self):
        a=90
        b=80
        print(a-b)

obj=b()
obj.sub()
obj.add()