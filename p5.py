# Dict using two list

a = ['a', 'b', 'c']
b = [100, 200, 300]
dd = {a[i]:b[i] for i in range(0, len(a))}
print(dd)