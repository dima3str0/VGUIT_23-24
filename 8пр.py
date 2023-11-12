from random import *
# Вариант 1 Задание 1
symm = 0
k = 0
n = 3
a = []

for i in range(n):
    b = []
    for j in range(n):
        b.append(randint(1,10))
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()

for i in range(n):
    for j in range(n):
        if (a[i][j] > 0) and (i<j):
            symm += a[i][j]
            k += 1

print(symm,'\n',k)

# Вариант 1 Задание 2
c = 2
n = 3

a = []

for i in range(c):
    b = []
    for j in range(n):
        b.append(randint(1,10))
    a.append(b)

for i in range(c):
    for j in range(n):
        print(a[i][j],end=' ')
    print()

print()

for i in a:
    i[i.index(max(i))],i[0] = i[0],i[i.index(max(i))]
    i[i.index(min(i))],i[-1] = i[-1],i[i.index(min(i))]


for i in range(c):
    for j in range(n):
        print(a[i][j],end=' ')
    print()

# Вариант 2 Задание 1
a = list()

n = 4

for i in range(n):
    b = list()
    for j in range(n):
        b.append(5)
    a.append(b)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()


first = sum(a[0])
b = 0

for k in a:
    if sum(k) != first:
        b += 1
        break

for k in range(0, n):
    if sum([row[k] for row in a]) != first:
        b += 1
        break

if b == 0:
    print('Матрица является магическим квадратом')
else:print('Матрица не является магическим квадратом')

# Вариант 2 Задание 2
a = list()

n = 3
m = 4

for i in range(n):
    b = list()
    for j in range(m):
        b.append(randint(1,9))
    a.append(b)


for i in range(n):
    for j in range(m):
        print(a[i][j],end = ' ')
    print()

for i in a:
    i[0],i[3] = i[3],i[0]

print()

for i in range(n):
    for j in range(m):
        print(a[i][j],end = ' ')
    print()

# Вариант 3 Задание 1
a = list()
n = 3

for i in range(n):
    b = list()
    for j in range(n):
        b.append(5)
    a.append(b)

print(a)

for i in range(n):
    for j in range(n):
        print(a[i][j],end=' ')
    print()

first = list()
second = list()

for i in range(n):
    for j in range(n):
        if i > j:first.append(a[i][j])
        if i < j:second.append(a[i][j])

print(first,'\n',second)

if first == second:
    print('Матрица является симметричной')
else:
    print('Матрица не является симметричной')
