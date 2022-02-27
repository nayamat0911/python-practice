mylist=["book","pen","apple"]
print(mylist)
mylist2=list()
print(mylist2)
item =mylist[-2]
print(item)
if "mango" in mylist:
    print("yes")
else:
    print("no")
mylist.append("mango")
print(len(mylist))
print(mylist)
mylist.insert(1,"banana")
print(mylist)
mylist.pop()
print(mylist)
mylist.remove("banana")
print(mylist)
mylist3=list(("doremon","shuchika","himo","panna","payra"))
print(mylist,type(mylist))

print(mylist3)

a=["sujika","kamala","hena","Rimu",
["book","pen",["banana","mango"],"apple"],
  "shunchan","Rimu"
]
print(a[1][2][1])
print(a[-2][-2][-1])
print(type(a[-2][-2][-1]))

print(a[1][1])
print(a[1:2])
s=a.append("kamal")
print(a)
a.extend(["hello","shimu","humayra"])
print(a)
a.insert(5,"bangladesh")
print(a)
a[5]="india"
print(a)
a[3][:3]=["keya",'manik',"gulzar"]
print(a)
a[3][3]="mango"
print(a*4)


for j in a:
    if type(j) is list:
        for k in j:
            print(k)
        print(j)
    else:print(j)
print(len(a[3][2]))
#
# print(a[3]*2)
# print(["hi"]*3)
# c=a.copy()
# print(c)
# e=a[3].copy()
# print(e)
#
# for d in a:
#     if type(d) is list:
#         g=d.copy()
#         print(d)
#     else:
#         print(d)
#
#
# print(len(a[3][2]))
# print("----")
#print(g)
print("------------")
k=["manik","hasan","jamal","khalek"]
print(a+k)
print('------a-----')
print(a)
print(a.index("Rimu"))
print(a.count("Rimu"))
a.reverse()
# print(a)
# a.sort()
B,C=[2,4,5,36,7,18,22,3,3,55,1],["Mahmudhasan","nayamat","jamakl"]
B.sort()
print(B)
C.sort()
print(C)
print(a)
D=[2,4,5,6,7,38,22,23,3,55,1]
print(max(B))
print(max(C))
print(min(B))
print(min(C))
print(sum(D))