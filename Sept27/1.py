import random

def odd_function():
    s = random.randrange(0,30)
    if s % 2 == 0:
        odd_function()
    else:
        return int(s)

def prime_number():
    c = 0
    s = int(random.randrange(0,30))
    for i in range(1, int(s/2)):
        if s % i == 0:
            c += 1
    if c == 1:
        return s
    elif s == 4:
        prime_number()
    else:
        prime_number()

# Main Program
X = set()
for i in range(0, 30):
    X.add(odd_function())
Y = set()
for i in range(0, 30):
    Y.add(prime_number())
print("X: ", X)
print("Y: ", Y)
X1 = {8456, 5646 ,54}
X.update(X1)
print("X.update(X1): ", X)
X.remove(8456)
print("X.remove(8456): ", X)
X.discard(5412)
print("X.discard(5412): ", X)
# X2 = {213, 54, 4, 5, 3, 7}
X.union(Y)
print("X.union(Y): ", X)
X.intersection(Y)
print("X.intersection(Y): ", X)
X.intersection_update(Y)
print("X.intersection_update(Y): ", X)
X.difference(Y)
print("X.difference(X2): ", X)
X.difference_update(X1)
print("X.difference_update(X1): ", X)
X3 = {4, 3, 2, 1}
X.symmetric_difference(X3)
print("X.symmetric_difference(X3): ", X)
X.symmetric_difference_update(Y)
print("X.symmetric_difference_update(Y): ", X)
print("all(Y): ", all(Y))
print("any(Y): ", any(Y))