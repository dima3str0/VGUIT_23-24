# Последняя цифра зачетки - 3
# 3 задание
a = int(input('Введите число а'))
b = int(input('Введите число b'))
if a > b:
	print('Числа подобраны верно')
	sp = list(range(b,a+1))
	pp = list()
	for i in sp:
		if i % 2 == 0:
			pp.append(i)
	print(pp[::-1])
else:
	print('Число а должно быть больше числа b')


# 2 задание
a = int(input('Введите число а'))
b = int(input('Введите число b'))
if a < b:
	sp = list(range(a,b+1))
	for i in sp:
		print(i)
else:
	sp = list(range(b,a+1))
	pp = list()
	for i in sp:
		pp.append(i)
	print(pp[::-1])

# 1 задание
a = int(input('Введите число а'))
b = int(input('Введите число b'))
if a <= b:
	a = list(range(a,b+1))
	for i in a:
		print(i)
else:
	print('Число а должно быть меньше или равно числу b')

# 10 Задание
n = int(input('Введите количество чисел из ряда: '))
k = int(input('Порядковый номер в ряду: '))
feb_symm = 0
i = 1
a0,a1 = 0,1
for i in range(1,n + 1):
    if i == 1:
        a2 = 0
    else:
        a2 = a0 + a1
        a0,a1 = a1,a2
        if i>=k:
            feb_symm += a2
    i += 1
print(feb_symm)

# 9 задание
n = int(input('Введите количество чисел из ряда: '))
feb_symm = 0
i = 0
a0,a1 = 0,1
for i in range(1,n+1):
    if i == 1:
        a2 = 0
    else:
        a2 = a0 + a1
        a0,a1 = a1,a2
        feb_symm += a2
    i += 1
print(feb_symm)
