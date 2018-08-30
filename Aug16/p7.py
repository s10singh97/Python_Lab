# Operations of List, Tuple and Dict

a = [100, 200, 'a', 'b']
b = (100, 200, 's', 2, 100)
c = {'a': 1, 'b': 2, 'c': 40}

print('Operations on List')
a.append(45)
print(a)
a.clear()
print(a)
a = [100, 200, 'a', 'b']
print(a)
print(a.index(200))
a.pop(2)
print(a)
a.remove(200)
print(a)
a.reverse()
print(a)

print('Operations on Tuple')
print(b.index('s'))
print(b.count(100))

print('Operations on Dictionary')
print(c.keys())
print(c.items())