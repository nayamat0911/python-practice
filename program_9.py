marks=int(input("Enter Your Number:"))
if marks ==0 or marks==100:
    print("invalid number")
elif marks>=80 and marks<=99:
    print("A+")
elif marks>=70 and marks<=79:
    print("A")
elif marks>=60 and marks<=69:
    print("B+")
elif marks>=50 and marks<=59:
    print("B")
elif marks>=40 and marks<=49:
    print("C+")
elif marks>=33 and marks<=39:
    print("D+")
else:
    print("Fail")

