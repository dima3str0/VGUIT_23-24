#Послнедняя цифра зачетки - 3
#Задание для самостоятельной работы из 3 пр
e = int(input('Введите e: '))
n = int(input('Введите n: '))
h = int(input('Введите h: '))
sp = list(range(1,4))
if e in sp:
	print(e)
if n in sp:
	print(n)
if h in sp:
	print(h)

#Задание №3 из 3 задания СР
a = int(input('Введите a: '))
c = ''
n = ''
for i in str(a):
	if int(i) % 2 == 0:
		c += i
	else:
		n += i
print(c,n)

#Задание №10 из 3 задания СР
d = int(input('Введите d: '))
b = int(input('Введите b: '))
c = int(input('Введите c: '))
if d == b and d == c:
	print('Числа равны')
else:
	print('Числа не равны')
