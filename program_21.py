#STACK AND QUEUE
book=[]
book.append("learn C")
book.append("Learn C++")
print(book)
book.append("Leran Python")
print(book)
book.pop()
print(book)
book.pop()
print(book)
book.pop()
if not book:
    print("no boks here")


from collections import deque
bank=deque(["X","Y","Z","A"])
print(bank)
bank.popleft()
print(bank)
bank.popleft()
print(bank)
bank.popleft()
bank.popleft()
if not bank:
    print("no person left")