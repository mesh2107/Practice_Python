data1={"name":"meshwa",
       "roll no":"12",
       "per":"90.5"
       }
print(data1)#print whole data


print(data1["per"])#print specific data

a=data1.keys()#print keys
print(a)

data1["std1"]=12#add or change

a=data1.keys()
print(a)

b=data1.values()#print values
print(b)

data1["std1"]=10#change data
data1["per"]=75
print(data1)




