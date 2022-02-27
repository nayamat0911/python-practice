def massage(a,b):
    return a*a+2*a*b+b*b
print(massage(2,3))

x=(lambda a,b:a*a+2*a*b+b*b)(2,3)
print(x)

print((lambda a,b:a*a+2*a*b+b*b)(2,3))
x=(lambda a:a*a*a)(2)
print(x)

