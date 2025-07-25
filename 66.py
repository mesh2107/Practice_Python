class A:
    n=[]
    l=5
    def get(self):
        if(self.l<=5):
            for i in range(0,self.l):
                name=input("enter name: ")
                self.n.append(name)
        else:
            self.n.append(self.name2)

    def put(self):
        print(self.n)
    def validate(self):
        self.name2=input("enter name: ")
        if self.name2 in self.n:
            print("already exist")
        else:
            self.l+=1
            self.get()
        print(self.n)

obj=A()
obj.get()
obj.put()
obj.validate()