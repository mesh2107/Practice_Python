user="abc"
passw="123"
number=int(input("enter: "))
if number==1:
    print(" DO LOGIN ")
    username=input("enter username: ")
    password=input("enter password: ")
    if username!=user and password==passw:
        print("invalid username.")
    elif username==user and password!=passw:
        print("invalid password.")
    elif username==user and password==passw:
        print("LOGIN SUCCESSFUL")
    else:
        print("re enter")

else:
    print(" NO LOGIN ")