from random import *

# Вариант 1 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))
m.reverse()

print('Полученный массив в обратном порядке:\n',m)
print('Максимальный элемент -->',max(m))

# Вариант 1 Задание 2
m = list()
cr_arifm = 0

for i in range(randint(5,10)):
    print('Введите',i+1,'действительный элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    cr_arifm += m[i]

cr_arifm /= len(m)

for i in range(len(m)):
    if m[i] == '0':
        m[i] = cr_arifm

print('Полученныый массив:\n',m)

# Вариант 2 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

print('Индекс минимального элемента:',m.index(min(m)))

# Вариант 2 Задание 2
m = list()
low = list()
up = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    if m[i] > 0:
        up.append(m[i])
    else:
        low.append(m[i])

print('Массив с элементами больше "0":',up,'\n','Массив с элементами меньше или равно "0":',low)

# Вариант 3 Задание 1
d = list()
n = int(input('Введите длину массива: '))
symm = 0

for i in range(n):
    print('Введите',i+1,'элемент массива')
    d.append(int(input()))

for i in range(n):
    if i % 2 == 1:
        symm += d[i]

print('Полученный массив:',d,'\n','Сумма элементов с нечетным индексом:',symm)

# Вариант 3 Задание 2
m = list()

for i in range(8):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    if m[i] < 15:
        m[i] **= 2
print('Полученный массив:',m)

# Вариант 4 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

print('Максимальный элемент массива:',max(m),'\n','Его порядковый номер:',(m.index(max(m)))+1)

# Вариант 4 Задание 2
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = list()

for i in range(len(m)):
    if m[i] % 2 == 1:
        n.append(m[i])

if len(n) == 0:
    print('Нечетный чисел в массиве нет!')
else:
    print('Полученный массив из нечетный чисел:\n',n)

# Вариант 5 Задание 1
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

for i in range(len(m)-1):
    if (m[i] < 0) and (m[i+1] < 0):
        print('Пара отрицательных чисел:',m[i],m[i+1])

# Вариант 5 Задание 2
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = list()

for i in range(len(m)):
    if n.count(m[i]) < 1:
        n.append(m[i])

print('Полчуенный моссив:',n,'\n',m)

# Вариант 6 Задание 1
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

b = 0
s = 0

for i in range(len(m)):
    if m[len(m)-1] < m[i]:
        b += 1
    elif m[len(m)-1] > m[i]:
        s += 1

print('Количество меньших максимального элемента:',s,'\n','Количество больших максимального элемента:',b)

# Вариант 6 Задание 2
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

symm = 0

for i in range(len(m)):
    if m[i] > 5:
        symm += m[i]
print('Сумма чисел, которые больше "5":',symm)

# Вариант 7 Задание 1
m = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

symm = 0
proisv = 1

for i in range(len(m)):
    if (i+1) % 2 == 1:
        symm += m[i]
    else:
        proisv *= m[i]

print('Сумма элементов с четными номерами:',symm,'\n','Произведение элементов с нечетными номерами:',proisv)

# Вариант 7 Задание 2
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

m[m.index(max(m))],m[m.index(min(m))] = m[m.index(min(m))],m[m.index(max(m))]

print('Полученный массив:',m)

# Вариант 8 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

symm = 0
proisv = 1

for i in range(len(m)):
    symm += m[i]
    proisv *= m[i]

print('Сумма элементов массива:',symm,'\n','Произведение элементов массива:',proisv)

# Вариант 8 Задание 2
m = list()
cr_arifm = 0

for i in range(randint(5,10)):
    print('Введите',i+1,' элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    cr_arifm += m[i]

cr_arifm /= len(m)

for i in range(len(m)):
    if m[i] == '0':
        m[i] = cr_arifm

print('Полученныый массив:\n',m)

# Вариант 9 Задание 1
m = list()

for i in range(randint(5,10)):
    print('Введите',i+1,'элемент массива')
    m.append(float(input()))

m.reverse()

print('Массив в обратном порядке:\n',m)

for i in range(len(m)):
    m[i] = abs(m[i])

print('Минимальный по модулю элемент:',min(m))

# Вариант 9 Задание 2
a = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    a.append(int(input()))

b = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    b.append(int(input()))

print('Массив А:',a,'\n','Массив B:',b)

a,b = b,a

print('Элементы преобразованного массива А:',a,'\n','Элементы преобразованного массива B:',b)

# Вариант 10 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = list()

for i in range(len(m)):
    if m.count(m[i]) > 1:
        n.append(m[i])

if len(n) > 0:
    print('В массиве есть повторяющийся элементы:',n)
else:
    print('В массиве нет повторяющийся элементов:')

# Вариант 10 Задание 2
m = list()

for i in range(15):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = m.copy()

for i in range(len(n)):
    if n[i] < 10:
        n[i] = 0
    elif n[i] > 20:
        n[i] = 1

print('Начальный массив:',m,'Преобразованный массив:',n)

# Вариант 11 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

while True:
    if (max(m) % 2) == 0:
        print(max(m))
        break
    else: m.remove(max(m))

# Вариант 11 Задание 2
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = list()

for i in range(len(m)):
    if (m[i] < 10) and ((m[i] % 2) == 0):
        n.append(m[i])

if len(n) == 0:
    print('В массиве нет четных элементов меньше 10!')
else:
    n.sort()
    print(n)

# Вариант 12 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

while True:
    if (min(m) % 2) == 1:
        print(min(m))
        break
    else: m.remove(min(m))

# Вариант 12 Задание 2
a = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    a.append(int(input()))

b = list()

for i in range(10):
    print('Введите',i+1,'элемент массива')
    b.append(int(input()))

a,b = b,a

print('Элементы преобразованного массива А:',a,'\n','Элементы преобразованного массива B:',b)

# Вариант 13 Задание 1
m = list()

for i in range(randint(4,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))


for i in range(len(m)):
    if m.count(m[i]) > 1 and (m[i+1:len(m)].count(m[i])) > 0:
        print(m[i],m.index(m[i],i+1,len(m)))

# Вариант 13 Задание 2
m = list()

for i in range(8):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

for i in range(len(m)):
    if m[i] < 15:
        m[i] *= 2

print('Преобразованный массив:',m)

# Вариант 14 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

m[m.index(max(m))],m[m.index(min(m))] = m[m.index(min(m))],m[m.index(max(m))]

print('Преобразованный массив:',m)

# Вариант 14 Задание 2
m = list(randint(1,20) for x in range(10))

cr_arifm = 0

for i in range(len(m)):
    cr_arifm += m[i]

cr_arifm /= len(m)

for i in range(len(m)):
    if m[i] > cr_arifm:
        m[i] = 1
print('Преобразованный массив:',m)

# Вариант 15 Задание 1
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))


for i in range(len(m)):
    if m.count(m[i]) > 1 and (m[i+1:len(m)].count(m[i])) > 0:
        print(m[i])

# Вариант 15 Задание 2
m = list()

for i in range(randint(2,5)):
    print('Введите',i+1,'элемент массива')
    m.append(int(input()))

n = list()

for i in range(len(m)):
    if m[i] % 2 == 1:
        n.append(m[i])

if len(n) == 0:
    print('Нечетных чисел в массиве нет!')
else:
    print(n)
