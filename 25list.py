fruit=["apple","strawberry","kiwi","mango","cherry","melon"]
b=input("enter name: ")
fruit.append(b)

c=input("enter another name: ")
fruit.insert(2,c)

for i in range(0,8):
    print(fruit[i])

#slicing
print(fruit[2:5])
print(fruit[2:])
print(fruit[:4]