import random

def even_function():
    s = set()
    for i in range(0, 30):
        if i % 2 == 0:
            s.add(i)
    return s

def fibonacci():
    s = set()
    a = 1
    s.add(a)
    b = 1
    s.add(b)
    n = 27
    while(n):
        c = a + b
        s.add(c)
        a = b
        b = c
        n -= 1
    return s

# Main Program
X = even_function()
Y = fibonacci()
print("X: ", X)
print("Y: ", Y)
X1 = {8456, 5646 ,54}
print(X1)
X.update(X1)
print("X.update(X1): ", X)
X.remove(8456)
print("X.remove(8456): ", X)
X.discard(5646)
print("X.discard(5646): ", X)
# X2 = {213, 54, 4, 5, 3, 7}
X.union(Y)
print("X.union(Y): ", X)
X.intersection(Y)
print("X.intersection(Y): ", X)
X.intersection_update(Y)
print("X.intersection_update(Y): ", X)
X.difference(Y)
print("X.difference(Y): ", X)
X.difference_update(X1)
print("X.difference_update(X1): ", X)
X3 = {4, 3, 2, 1}
X.symmetric_difference(X3)
print("X.symmetric_difference(X3): ", X)
X.symmetric_difference_update(Y)
print("X.symmetric_difference_update(Y): ", X)
print(X)
print(Y)
print("all(Y): ", all(Y))
print("any(Y): ", any(Y))