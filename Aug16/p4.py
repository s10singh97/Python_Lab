# Fibonacci Pyramid
    
a = 1
b = 2
s = a + b
m = 1
n = int(input('Enser no. of rows'))
d = n - 1
for i in range(0, n):
    for j in range(0, d):
        print(" ", end = ' ')
    for k in range(0, m):
        print(a, " ", end = ' ')
    s = a + b
    a = b
    b = s
    print()
    d -= 1
    m += 1