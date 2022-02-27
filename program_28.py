try:
    list1=[0,20,30,40,0]
    result=list1[0]/list1[2]
    print(result)
    print("done")
except ZeroDivisionError:
    print("dividing by zero is not prossible")
except IndexError:
    print("index error")
print("sucessfull")


