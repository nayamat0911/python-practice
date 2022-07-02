# capitalize
print("Capitalize")

a = "doremon is my favarite carton"
print(a)

print(a.capitalize())

# title

print(a.title())
print("upper")
print(a.upper())

# casefolde for all caracter lower case
print(a.casefold())
# lower
print(a.lower())

# casefold is more power from lower
b = "abc"

# join
print("*".join(a))

print(b.join(a))
print(a.find("is"))
print(a.find("ok"))
print(a.find("e"))
print(a.rfind("is"))
print(b.center(30))
print(b.center(30,"*"))
# ljusr
# rjust
print(b.ljust(20))
print(b.rjust(20))
#count
print(a.count("r"))
c = "3333333dcbnewsiiiijjjj    "
print(c.strip())
print(c.lstrip("3ij"))
print(c.rstrip("3ij"))

print(a.split())
print(a.split(), type(a))

# splite line
e = "Bangladesh Is A My \n Beautifull My Country"

print(e)
print(e.partition("my"))
print(e.rpartition("my"))

print(e.swapcase())
print(e.endswith("y"))
print(e.startswith("my"))
# zfile
f = "bangladesh"
print(f.zfill(20))
print(f.rjust(20))
# replace
print(e.replace("bangladesh","tom and jary"))

print(e.islower())
print(e.istitle())
k ="999"
print(k.isnumeric())

print(k.isdigit())

print("decimal")
print(k.isdecimal())
l = "            "
print(l.isspace())
