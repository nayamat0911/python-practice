a=("nayamt","shinshun","nayamat","fahad",2,4,5,33,44,23)
print(a)
b= tuple(("doremn","hasan",["Mr","Mrs","Miss"],"kamal",("akash","batash","chad"),33,12,56))
# print(b)
# c ="demon","manij",3,4,66
#
# print(c)
# print(type(c))
# e=("jamal")
# print(e)
# e=("jamal",)
# print(e)
# print(type(e))
# b= ("doremn","hasan",("akash","swrovk","hasan"),"amal",33,12,56)
# f= ("doremn","hasan",["akash","swrovk","hasan"],"amal",33,12,56)
# g= ["doremn","hasan",("akash","swrovk","hasan"),"amal",33,12,56]
# print(b)
# print(f)
# print(g)
# print(b[2][2])
# print(b[-2])
# print(b[-5][-2])
# print(b[-3:-1])
#
# h=list(b)
# print(h)
# h.append("200")
# h.append(303)
# print(h)
#
# print(h)
# k=tuple(h)
# print(k)
#print(b)
for i in b:
    if type(i) is list:
        for j in i:
            print(j)
    elif type(i) is tuple:
        for j in i:
            print(j)
    else:
        print(i)
    print(i)

if "kamal" in b:
    print("found")
else:
    print("not found")

#repitation
print(b*2)
#concatination
print(a+b)
print(len(b))
print(len(b[2]))
c=(3,5,44,55,5,21,45,54)
d=("bangla","english","tamil","hindi","Bangladesh")
print(max(c))
print(max(d))
print(min(c))
print(min(d))
print(sum(c))
print(d.index("Bangladesh"))
print(sorted(c))
print(sorted(d))

print(c.count(5))
print(d.count("bangla"))

