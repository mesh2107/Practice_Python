class A:
    def funct1(self,value1):
        print(self.value)
        print(value1)
obj1=A()
obj1.value=input("Enter Value : ")
v=input("Enter : ")
obj1.funct1(v)