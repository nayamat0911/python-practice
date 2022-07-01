a = "codinglough"
print(a, type(a))
b = 'codinglough'
print(b, type(b))

c = "bangladesh is good 'country' now"
print(c)

#multiline type
d = """
learn
    somthing 
everyday
"""
print(d, type(d))

#positive index
e = "hello bangladesh"
print(e[2])
print(len(e))
print(e[6])

#nagative index
print(e[-5])

# range or slice
print(e[3:9])
print(e[:9]) # from first to 9 index
print(e[3:]) # from 3 index to last index

# change
f= "I love bangladesh"
# f[3] = 'm'
# alternative way
print(f)
# f = f[:3] + "m"+f[4:]
print(f)

# delete
# del e[0]
print(e) # string method delete not support
print(e)

# loop
for i in f:
    print(i)

# length
# f = len(f)
# print("length of sentance = "+ f)

# membership
print("o" in f)
print("d" not in f)
print(e+", "+ f)

h = "bangladesh"
if "bangladeesh" != h:
    print("matched")
else:
    print("somthing wrong")

i = "abc"
j = "ABC"

print(i<j)
print(i>j)
k = "bangladesh"
l = 5
print(k+ "{}".format(l))
m = "{:->20} nayamat".format(k)
print(m)



