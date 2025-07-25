meritlist=[[11,34],[21,45],[31,67],[41,89]]
rollno=int(input("enter roll no: "))
count=0
t=0
for i in range(0,4):
    for j in range(0,2):
        if rollno==meritlist[i][j]:
            t=i
            count+=1
            break
if count==1:
    print("percentage: ", meritlist[t][1])
    print("rank: ", t + 1)
else:
    print("NO Rollno ")

