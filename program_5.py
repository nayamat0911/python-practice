mark=20
if mark>=40:
    print("pass")
else:
    print("fail")
print("end program")

num=int(input("enter your number"))
if num>=60 and num<=69:
    print("A+")
elif num>=50 and num<=59:
    print("B+")
elif num>=40 and num<=49:
    print("C+")
elif num>=30 and num<=39:
    print("D+")
else:
    print("Fail")

print("____________")
num2=int(input("enter your number:"))
num3=int(input("Enter last number: "))
if num2>num3:
    print(num2)
else:
    print(num3)
print("--------------------")
num4=float(input("enter even or odd number:"))
if num4%2==0:
    print("even")
else:
    print("Odd")