class A:
    n=[]
    def putdata(self):
        for i in range(0,5):
            name=input("enter name: ")
            self.n.append(name)

    def printdata(self):
        print(self.n)


obj=A()
obj.putdata()
obj.printdata()