import list71
class A:
    def getdata(self):
        self.roll=input("enter roll no: ")
        self.name=input("enter name:")
        self.mob=input("enter mobile: ")
    def putdata(self):
        list71.details.append(self.roll)
        list71.details.append(self.name)
        list71.details.append(self.mob)
class B(A):
    def getresult(self):
        self.total=int(input("enter total: "))
        self.per=int(input("enter percentage: "))
    def putresult(self):
        list71.result.append(self.total)
        list71.result.append(self.per)
obj=B()
obj.getdata()
obj.putdata()
obj.getresult()
obj.putresult()
print(list71.details)
print(list71.result)