# Table of Symmetric Matrix

n = int(input('Enter size of matrix'))
for i in range(1, n + 1):
    for j in range(i*2, (n + i)*2, 2):
        print(j, " ", end = "")
    print()
    