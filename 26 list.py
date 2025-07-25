series=[]

for i in range(0,10):
   name=input("enter names: ")
   series.append(name)

find=input("enter name to find: ")
if find in series:
    print("data matched")
