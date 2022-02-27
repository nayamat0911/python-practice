def student(*details):
    print(details)

student(101, "anis","nayamat",3.55)
student(102, "kamal","nayamat",3.55)
student(103, "manik","nayamat",3.55)

def add(*numbers):
    sum=0
    for num in numbers:
        sum=sum+num
    print(sum)

add(10,20)
add(10,20,50)
add(10,20,50,60)
add(10,20,50,60,80)
print("---------------")
def studentDetalis(**detailss):
    print(detailss)

studentDetalis(id=102, name="anis")