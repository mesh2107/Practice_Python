data1={}

yesno=input("do you want to add keyword:")
while yesno=="yes":
    key=input("enter keyword")
    value=input("enter"+key+":")
    data1[key]=(value)
    yesno = input("do you want to add keyword:")

print(data1)