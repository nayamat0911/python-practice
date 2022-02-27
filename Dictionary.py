a={
    "dis":"name",
    "name":"nayamt",
    "age":34,
    40:"name",
    41:"age",
    42:43
}
print(type(a))
print(a)
#constractor
b=dict({
    "dis":"name",
    "name":"nayamt",
    "age":34,
    40:"name",
    41:"age",
    42:43
})
print(b)
c=dict(
    carton="carton1",
    carton2="carton2",
    carton3="carton3"
)
print(c)
#pair
d=dict([
    ("carton","nayamt"),
    ("age",34),
    ("aksah","batash")
])
print(d)
#nestted dictionary
e={
    "dis":"name",
    "name":["name",345,"kay"],
    "age":34,
    40:("kamal","manik","jamal"),
    41:"age",
    42:{
        "one":1,
        "two":2,
        "three":3
    },
    "carton":"carton4"
}
print(e)
# #accessing value
# print(e[42])
# print(e["carton"])
# print(e[42]["one"])
# print(e[40][2])
# #get method
# print(e.get(42))
# print(e.get(4))
# #add method
# e["tanim"]="mina"
# print(e)
# #add nested index
# e[42]["four"]=4
# print(e)
#changed value
# e["carton"]="mithu"
# print(e)
#delate
# del e[41]
# print(e)
# e.pop(40)
# print(e)
# e[42].pop("four")
# print(e)
# e.popitem()
# print(e)
# e.popitem()
# print(e)
# f=e[42].copy()
# print(f)
for j in e:
    print(j)
for i in e.values():
    print(i)
print("--------")
for i,k in e.items():
    print(i,"=",k)
print(a.keys())
print(a.values())
print(a.items())

h={
    "name":"Nayamat Ullah",
    'email':"nayamay@gmail.com"
}
e.update(h)
print(e)
g=(
    "name","email","phone"
)
e=dict.fromkeys(g)
print(e)

for i in e:
    if i=="name":
        e["name"] = "Marjuk"
    elif i=="email":
        e["email"]="naym@gmail.com"
    elif i=="phone":
        e["phone"]="9230243"
print(e)
 