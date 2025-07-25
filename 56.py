student1={"roll no":"1",
          "name":"AAAA",
          "class":"english",
          "per":"34"}
student2={"roll no":"2",
          "name":"BBBB",
          "class":"hindi",
          "per":"45"}
student3={"roll no":"3",
          "name":"CCCC",
          "class":"maths",
          "per":"67"}
student4={"roll no":"4",
          "name":"DDDD",
          "class":"chemistry",
           "per":"78"}
student5={"roll no":"5",
          "name":"EEEE",
          "class":"phyics",
          "per":"89"}
nos=int(input("enter roll no to find: "))
if nos==1:
    print(student1)
elif nos==2:
    print(student2)
elif nos==3:
    print(student3)
elif nos==4:
    print(student4)
elif nos==5:
    print(student5)
else:
    print("NO DATA")