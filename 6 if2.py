age=int(input("enter age: "))
if age>=18:
    print("person eligible to vote")
if age<18 and age>0:
    print("person not eligible to vote")
if age<0:
    print("invalid age.")
print()

number1=int(input("enter a number: "))
if number1>0:
    print("number is positive.")
else :
    print("number is negative.")
print()

year=int(input("enter year: "))
if year%100==0 and year%400==0:
    print("year is a leap year.")
elif year%100!=0 and year%4==0:
    print("year is leap year.")
else:
    print("year is not a leap year.")

