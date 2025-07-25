user="abc"
passw="123"
number=int(input("enter: "))
while number!=1:
    number=int(input("RE enter number: "))

if number==1:
    print("DO LOGIN")
    username=input("enter username: ")
    password=input("enter password: ")
    if username==user and password==passw:
        print("login successful.....")
    while username!=user or password!=passw:
        if username!=user and password==passw:
            print("invalid username.")
        elif username==user and password!=passw:
            print("invalid password.")
        else:
            print("both are inavlid.")
        username=input("re enter username: ")
        password=input("re enter password: ")
