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



