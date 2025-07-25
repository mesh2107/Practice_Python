user="abc"
password="123"

a=int(input("enter your choice : "))


if a==1:
    print("please login with username and password ")
    uname=input("Enter username :")
    pwrd=input("Enter Password :")
    while uname!=user or pwrd!=password:


        if uname!=user and pwrd==password:
            print("invalid username")
        elif uname == user and pwrd != password:
            print("invalid password")
        else:
            print("invalid username and password")

        uname=input("Re-Enter username :")
        pwrd=input("Re-Enter Password :")

    if uname == user and pwrd == password:
        print("Login succ....")
else:
    print("thank you......")