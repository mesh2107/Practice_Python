try:
    #a=123
    print("hello")
    print(a)
except:
    print("error")
else:
    print("all right")
finally:
    print("always")

x=int(input("enter age:"))
if x<18:
    raise Exception("not eligible")