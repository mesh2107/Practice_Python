class details:
    def putdata(self):
        file=[]
        roll=int(input("enter roll no: "))
        file.append(roll)
        name=input("enter name: ")
        file.append(name)
        print(file)
class result(details):
    def result(self):
        file2=[]
        sum=0
        for i in range(0,5):
            marks=int(input("enter marks of subject: "))
            sum+=marks
        file2.append(sum)
        print(file2)

obj=result()
obj.putdata()
obj.result()

