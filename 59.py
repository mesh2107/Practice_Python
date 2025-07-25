option=input("do you want to login or register: ")
count=0
original=[]
lo=len(original)
if option=="login" and lo==0:
    print("no data found please register first")
elif option=="register":
    while option=="register":
        user={}
        lu=len(user)
        print("please fillup below details:")
        count+=1
        roll=count
        name=input("Enter Name: ")
        email=input("Enter Email: ")
        mobile=input("Enter Mobile: ")
        pwrd=input("Enter Password")
        user['id']=roll
        user['name']=name
        user['email']=email
        user['mobile']=mobile
        user['password']=pwrd
        lu=len(user)

        original.append(user)
        lo=len(original)
        print(original)
        option=input("login or register: ")

        if option=="login":
            uname=input("Enter Username (email/mobile): ")
            ps=input("Enter Password: ")
            upl=0
            ul=0
            pl=0
            for i in range(0,lo):
                if (uname in original[i]['email'] or uname in original[i]['mobile']) and ps in original[i]['password']:
                    upl+=1
                    break
                if (uname not in original[i]['email'] or uname not in original[i]['mobile']) and ps in original[i]['password']:
                    ul+=1
                    break
                if (uname in original[i]['email'] or uname in original[i]['mobile']) and ps not in original[i]['password']:
                    pl+=1
                    break
            if upl>0:
                print("login su...")
            if ul>0:
                print("REenter username")
            if pl>0:
                print("Wrong ps")
            option = input("login or register: ")
else:
    print("invalid ")
