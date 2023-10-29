def zmeika_nxn(n):
    arr1 = [0] * n
    for i in range(n):
        arr1[i] = [0] * n
    for i in range(n):
        for j in range(n):
            if (i % 2 == 0):
                arr1[i][j] = n * i + j + 1
            else:
                arr1[i][j] = n * (i + 1) - j
    return arr1

def zmeika_nx2n(n, arr1):
    arr2 = [0] * n
    for i in range(n):
        arr2[i] = [0] * n * 2
    for i in range(n):
        for j in range(n):
            arr2[i][j] = arr1[i][j]
    for i in range(n):
        for j in range(n * 2):
            arr2[i][n * 2 - j - 1] = arr2[i][j]
    return arr2

def zmeika_2nx2n(n, arr2):
    arr3 = [0] * n * 2
    for i in range(n * 2):
        arr3[i] = [0] * n * 2
    for i in range(n):
        for j in range(n * 2):
            arr3[i][j] = arr2[i][j]
    for i in range(n * 2):
        for j in range(n * 2):
            arr3[n * 2 - i - 1][j] = arr3[i][j]
    return arr3

flag = 0
while flag != 1:
    n = input('Input length of double array: ')
    if (n.isdigit()):
        n = int(n)
        flag = 1
    else:
        print("Incorrect input")
        flag = 0
arrA = zmeika_nxn(n)
print("Array A= ")
for i in range(n):
    for j in range(n):
        print('%2.f' % arrA[i][j], end=' ')
    print()
arrB = zmeika_nx2n(n, arrA)
print("Array B= ")
for i in range(n):
    for j in range(n*2):
        print('%2.f' % arrB[i][j], end=' ')
    print()
arrC = zmeika_2nx2n(n, arrB)
print("Array B= ")
for i in range(n*2):
    for j in range(n*2):
        print('%2.f' % arrC[i][j], end=' ')
    print()